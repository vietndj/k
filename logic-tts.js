(function () {
  if (typeof window === 'undefined' || typeof document === 'undefined') return;
  if (window.__FEDU_LOGIC_TTS_INIT__) return;
  window.__FEDU_LOGIC_TTS_INIT__ = true;

  var MEDIA_TTS_BASE = 'https://media.fedu.vn/tts';
  var GTX_BASE = 'https://translate.googleapis.com/translate_tts?client=gtx&ie=UTF-8&tl=vi&q=';
  var RATES = [1, 1.25, 1.5, 1.75];

  function ensureNoReferrerMeta() {
    var m = document.querySelector('meta[name="referrer"]');
    if (!m) {
      m = document.createElement('meta');
      m.name = 'referrer';
      m.content = 'no-referrer';
      (document.head || document.documentElement).appendChild(m);
    } else if (m.content !== 'no-referrer') {
      m.content = 'no-referrer';
    }
  }

  function injectStyles() {
    if (document.getElementById('fedu-logic-tts-css')) return;
    var st = document.createElement('style');
    st.id = 'fedu-logic-tts-css';
    st.textContent = [
      '.logic-tts-hero-btn{background:#059669;color:#fff;border:none;padding:10px 16px;border-radius:6px;font-family:system-ui,-apple-system,sans-serif;font-size:13px;font-weight:600;cursor:pointer;display:inline-flex;align-items:center;gap:6px;transition:background .15s ease;}',
      '.logic-tts-hero-btn:hover{background:#047857;}',
      '.logic-tts-hero-btn.is-playing{background:#0f172a;}',
      '.logic-tts-inline-btn{margin-left:10px;padding:3px 10px;border-radius:999px;border:1px solid #cbd5e1;background:#fff;color:#0f172a;font-family:system-ui,-apple-system,sans-serif;font-size:12px;font-weight:600;cursor:pointer;vertical-align:middle;display:inline-flex;align-items:center;gap:4px;line-height:1.4;}',
      '.logic-tts-inline-btn:hover{border-color:#059669;color:#059669;}',
      '.logic-tts-inline-btn.is-playing{background:#059669;color:#fff;border-color:#059669;}',
      '.is-tts-reading{outline:2px solid #10b981;outline-offset:6px;border-radius:10px;background:rgba(16,185,129,0.03);}',
      '.logic-tts-bar{position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:9999;width:min(640px,calc(100vw - 24px));background:#0f172a;color:#f8fafc;border-radius:14px;padding:10px 14px;box-shadow:0 12px 32px rgba(15,23,42,.35);display:flex;align-items:center;justify-content:space-between;gap:10px;font-family:system-ui,-apple-system,sans-serif;}',
      '.logic-tts-bar[hidden]{display:none !important;}',
      '.logic-tts-info{min-width:0;flex:1;}',
      '.logic-tts-meta{font-size:11px;color:#94a3b8;display:flex;align-items:center;gap:6px;margin-bottom:2px;}',
      '.logic-tts-badge{background:#059669;color:#fff;padding:1px 6px;border-radius:999px;font-weight:600;font-size:10px;}',
      '.logic-tts-badge.is-gtx{background:#334155;}',
      '.logic-tts-title{font-size:13px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}',
      '.logic-tts-controls{display:flex;align-items:center;gap:6px;flex-shrink:0;}',
      '.logic-tts-ctrl{background:#1e293b;color:#f8fafc;border:1px solid #334155;border-radius:8px;padding:6px 10px;font-size:13px;font-weight:600;cursor:pointer;line-height:1;}',
      '.logic-tts-ctrl:hover{background:#334155;}',
      '.logic-tts-ctrl.is-primary{background:#10b981;color:#052e16;border-color:#10b981;}',
      '@media(max-width:600px){.logic-tts-bar{bottom:10px;padding:8px 10px;gap:8px;}.logic-tts-ctrl{padding:6px 8px;font-size:12px;}}'
    ].join('');
    (document.head || document.documentElement).appendChild(st);
  }

  function normalizeTtsText(raw) {
    var t = String(raw || '');
    if (t.normalize) t = t.normalize('NFC');
    t = t.replace(/https?:\/\/\S+/g, ' ');
    t = t.replace(/\[?\b\d{1,2}:\d{2}(?::\d{2})?\b\]?/g, ' ');
    t = t.replace(/[❓🎯🔬⚡💡📜📌🧭🔄▶↗▾★☆📋🔍📑💬🎙️📍🗺️🔥]+/g, ' ');
    t = t.replace(/\bv\.v\.?/gi, 'vân vân').replace(/\bTP\./g, 'thành phố ').replace(/\bK4\b/g, 'ca bốn').replace(/\bBĐS\b/g, 'bất động sản');
    t = t.replace(/[ \t\r]+/g, ' ');
    var lines = t.split('\n').map(function (ln) {
      return ln.replace(/^[ \t•-]+|[ \t•-]+$/g, '');
    }).filter(function (ln) {
      return ln && !/^[\W_]+$/.test(ln);
    });
    return lines.join('\n').trim();
  }

  function extractTextFromNodes(nodes) {
    var parts = [];
    for (var i = 0; i < nodes.length; i++) {
      var clone = nodes[i].cloneNode(true);
      if (clone.querySelectorAll) {
        var skip = clone.querySelectorAll('.ink-provenance,.ink-prov-row,.ink-ts-pill,.ink-meta-badge,.ink-meta,.ink-top-actions,.logic-tts-inline-btn,script,style');
        for (var j = 0; j < skip.length; j++) skip[j].remove();
        var brs = clone.querySelectorAll('br');
        for (var b = 0; b < brs.length; b++) brs[b].replaceWith(document.createTextNode('\n'));
        var blocks = clone.querySelectorAll('p,li,h1,h2,h3,h4,blockquote,tr,div');
        for (var k = 0; k < blocks.length; k++) blocks[k].appendChild(document.createTextNode('\n'));
      }
      parts.push(clone.textContent || '');
    }
    return normalizeTtsText(parts.join('\n'));
  }

  function splitGtxChunks(text, maxLen) {
    maxLen = maxLen || 168;
    var lines = String(text || '').split('\n');
    var out = [];
    function pushPiece(piece) {
      var s = piece.trim();
      if (!s) return;
      if (s.length <= maxLen) {
        out.push(s);
        return;
      }
      var sentences = s.split(/(?<=[.!?;,])\s+/);
      var buf = '';
      for (var i = 0; i < sentences.length; i++) {
        var w = sentences[i].trim();
        if (!w) continue;
        if (w.length > maxLen) {
          if (buf) { out.push(buf); buf = ''; }
          var words = w.split(/\s+/);
          for (var wi = 0; wi < words.length; wi++) {
            var cand = buf ? buf + ' ' + words[wi] : words[wi];
            if (cand.length > maxLen && buf) { out.push(buf); buf = words[wi]; }
            else buf = cand;
          }
        } else {
          var next = buf ? buf + ' ' + w : w;
          if (next.length > maxLen && buf) { out.push(buf); buf = w; }
          else buf = next;
        }
      }
      if (buf) out.push(buf);
    }
    for (var i = 0; i < lines.length; i++) pushPiece(lines[i]);
    return out;
  }

  function collectSections() {
    var sections = [];
    var p1 = document.getElementById('phan-1-ban-do');
    if (p1) {
      var h2s = p1.querySelectorAll('h2');
      if (h2s.length > 0) {
        var nodesMap = {};
        var curKey = 0;
        var children = Array.from(p1.children);
        for (var i = 0; i < children.length; i++) {
          var ch = children[i];
          if (ch.tagName === 'H2') curKey += 1;
          var keyIdx = curKey === 0 ? 1 : curKey;
          if (!nodesMap[keyIdx]) nodesMap[keyIdx] = [];
          nodesMap[keyIdx].push(ch);
        }
        for (var idx = 1; idx <= h2s.length; idx++) {
          var h2El = h2s[idx - 1];
          var txt = extractTextFromNodes(nodesMap[idx] || [h2El]);
          if (txt) {
            sections.push({
              id: 'p1-' + idx,
              title: normalizeTtsText(h2El.textContent),
              anchorEl: h2El,
              highlightEls: nodesMap[idx] || [h2El],
              btnHost: h2El,
              text: txt
            });
          }
        }
      } else {
        var p1Txt = extractTextFromNodes([p1]);
        if (p1Txt) {
          sections.push({ id: 'p1-1', title: 'Phần 1: Bản đồ nhận thức', anchorEl: p1, highlightEls: [p1], btnHost: p1.querySelector('h3') || null, text: p1Txt });
        }
      }
    }

    var p2 = document.getElementById('phan-2-bo-the') || document.querySelector('.ink-content') || document.body;
    var turns = p2.querySelectorAll('.dialogue-turn');
    for (var t = 0; t < turns.length; t++) {
      var turn = turns[t];
      var secId = turn.id || ('q' + (t + 1));
      var qHead = turn.querySelector('.dialogue-prompt');
      var turnTxt = extractTextFromNodes([turn]);
      if (turnTxt) {
        sections.push({
          id: secId,
          title: qHead ? normalizeTtsText(qHead.textContent) : ('Câu ' + (t + 1)),
          anchorEl: turn,
          highlightEls: [turn],
          btnHost: qHead,
          text: turnTxt
        });
      }
    }
    return sections;
  }

  function buildPlayerBar() {
    var bar = document.createElement('div');
    bar.className = 'logic-tts-bar';
    bar.hidden = true;
    bar.innerHTML = [
      '<div class="logic-tts-info">',
      '  <div class="logic-tts-meta"><span class="logic-tts-badge" data-el="badge">Đọc tự động</span><span data-el="pos">Phần 1/1</span></div>',
      '  <div class="logic-tts-title" data-el="title">Đang chuẩn bị...</div>',
      '</div>',
      '<div class="logic-tts-controls">',
      '  <button type="button" class="logic-tts-ctrl" data-act="prev" title="Phần trước">⏮</button>',
      '  <button type="button" class="logic-tts-ctrl is-primary" data-act="toggle" title="Phát hoặc tạm dừng">⏸</button>',
      '  <button type="button" class="logic-tts-ctrl" data-act="next" title="Phần tiếp theo">⏭</button>',
      '  <button type="button" class="logic-tts-ctrl" data-act="rate" title="Tốc độ đọc">1x</button>',
      '  <button type="button" class="logic-tts-ctrl" data-act="close" title="Đóng trình phát">✕</button>',
      '</div>'
    ].join('');
    document.body.appendChild(bar);
    return bar;
  }

  function initTtsEngine() {
    ensureNoReferrerMeta();
    injectStyles();
    var sections = collectSections();
    if (!sections.length) return;

    for (var i = 0; i < sections.length; i++) {
      sections[i].gtxChunks = splitGtxChunks(sections[i].text, 168);
      sections[i].gtxUrls = sections[i].gtxChunks.map(function (c) { return GTX_BASE + encodeURIComponent(c); });
      sections[i].aiAudioUrl = '';
    }

    var savedRate = parseFloat(localStorage.getItem('fedu_tts_rate') || '1');
    if (RATES.indexOf(savedRate) < 0) savedRate = 1;

    var state = {
      active: false,
      playing: false,
      secIdx: 0,
      chunkIdx: 0,
      rate: savedRate,
      usingSpeech: false,
      manifestLoaded: false
    };

    var audio = document.createElement('audio');
    audio.preload = 'auto';
    audio.setAttribute('playsinline', '');
    audio.setAttribute('referrerpolicy', 'no-referrer');
    audio.style.display = 'none';
    document.body.appendChild(audio);

    var bar = buildPlayerBar();
    var elBadge = bar.querySelector('[data-el="badge"]');
    var elPos = bar.querySelector('[data-el="pos"]');
    var elTitle = bar.querySelector('[data-el="title"]');
    var btnToggle = bar.querySelector('[data-act="toggle"]');
    var btnRate = bar.querySelector('[data-act="rate"]');
    btnRate.textContent = state.rate + 'x';

    var heroBtn = null;
    var topActions = document.querySelector('.ink-top-actions');
    if (topActions) {
      heroBtn = document.createElement('button');
      heroBtn.type = 'button';
      heroBtn.className = 'logic-tts-hero-btn';
      heroBtn.textContent = '🎧 Nghe cẩm nang';
      topActions.insertBefore(heroBtn, topActions.firstChild);
    }

    for (var s = 0; s < sections.length; s++) {
      (function (idx) {
        var sec = sections[idx];
        if (!sec.btnHost) return;
        var b = document.createElement('button');
        b.type = 'button';
        b.className = 'logic-tts-inline-btn';
        b.textContent = '🔊 Nghe';
        b.title = 'Nghe từ phần này và tự chuyển phần tiếp theo';
        b.addEventListener('click', function (ev) {
          ev.stopPropagation();
          if (state.active && state.secIdx === idx) {
            togglePlayPause();
          } else {
            playAt(idx, 0, true);
          }
        });
        sec.inlineBtn = b;
        sec.btnHost.appendChild(b);
      })(s);
    }

    function updateUi() {
      var cur = sections[state.secIdx];
      bar.hidden = !state.active;
      if (state.active && cur) {
        elPos.textContent = 'Phần ' + (state.secIdx + 1) + '/' + sections.length;
        elTitle.textContent = cur.title || ('Phần ' + (state.secIdx + 1));
        elBadge.textContent = cur.aiAudioUrl ? 'AI Studio' : (state.usingSpeech ? 'Giọng máy' : 'Đọc tự động');
        elBadge.className = 'logic-tts-badge' + (cur.aiAudioUrl ? '' : ' is-gtx');
        btnToggle.textContent = state.playing ? '⏸' : '▶';
      }
      if (heroBtn) {
        heroBtn.classList.toggle('is-playing', state.active && state.playing);
        heroBtn.textContent = (state.active && state.playing) ? '⏸ Tạm dừng nghe' : '🎧 Nghe cẩm nang';
      }
      for (var i = 0; i < sections.length; i++) {
        var sec = sections[i];
        var isCur = state.active && i === state.secIdx;
        for (var h = 0; h < sec.highlightEls.length; h++) {
          sec.highlightEls[h].classList.toggle('is-tts-reading', isCur);
        }
        if (sec.inlineBtn) {
          sec.inlineBtn.classList.toggle('is-playing', isCur && state.playing);
          sec.inlineBtn.textContent = (isCur && state.playing) ? '⏸ Đang đọc' : '🔊 Nghe';
        }
      }
    }

    function updateMediaSession(sec) {
      if (!('mediaSession' in navigator) || !sec) return;
      try {
        navigator.mediaSession.metadata = new MediaMetadata({
          title: sec.title,
          artist: document.title || 'Kho Logic FEDU',
          album: 'Cẩm nang nhận thức'
        });
        navigator.mediaSession.playbackState = state.playing ? 'playing' : 'paused';
        navigator.mediaSession.setActionHandler('play', function () { togglePlayPause(); });
        navigator.mediaSession.setActionHandler('pause', function () { togglePlayPause(); });
        navigator.mediaSession.setActionHandler('previoustrack', function () { stepSection(-1); });
        navigator.mediaSession.setActionHandler('nexttrack', function () { stepSection(1); });
      } catch (e) {}
    }

    function prefetchNext(secIdx, chunkIdx) {
      var cur = sections[secIdx];
      var nextUrl = '';
      if (cur && !cur.aiAudioUrl && chunkIdx + 1 < cur.gtxUrls.length) {
        nextUrl = cur.gtxUrls[chunkIdx + 1];
      } else if (secIdx + 1 < sections.length) {
        var nxt = sections[secIdx + 1];
        nextUrl = nxt.aiAudioUrl || (nxt.gtxUrls && nxt.gtxUrls[0]) || '';
      }
      if (nextUrl) {
        try { fetch(nextUrl, { mode: 'no-cors', referrerPolicy: 'no-referrer' }).catch(function () {}); } catch (e) {}
      }
    }

    function speakFallbackChunk(secIdx, chunkIdx) {
      var sec = sections[secIdx];
      if (!sec || !('speechSynthesis' in window)) return stopAll();
      state.usingSpeech = true;
      window.speechSynthesis.cancel();
      var txt = (sec.gtxChunks && sec.gtxChunks[chunkIdx]) || sec.text;
      var u = new SpeechSynthesisUtterance(txt);
      u.lang = 'vi-VN';
      u.rate = state.rate;
      u.onend = function () {
        if (!state.active || !state.playing) return;
        advanceFrom(secIdx, chunkIdx);
      };
      u.onerror = function () {
        if (state.active && state.playing) advanceFrom(secIdx, chunkIdx);
      };
      window.speechSynthesis.speak(u);
      updateUi();
    }

    function playAt(secIdx, chunkIdx, shouldScroll) {
      if (secIdx >= sections.length) return stopAll();
      if (secIdx < 0) secIdx = 0;
      var sec = sections[secIdx];
      state.active = true;
      state.playing = true;
      state.secIdx = secIdx;
      state.chunkIdx = chunkIdx || 0;
      state.usingSpeech = false;
      if ('speechSynthesis' in window) window.speechSynthesis.cancel();

      if (shouldScroll && sec.anchorEl && sec.anchorEl.scrollIntoView) {
        sec.anchorEl.scrollIntoView({ behavior: 'auto', block: 'start' });
      }
      var tocLinks = document.querySelectorAll('.ink-toc-link');
      for (var t = 0; t < tocLinks.length; t++) {
        var href = tocLinks[t].getAttribute('href') || '';
        tocLinks[t].classList.toggle('is-active', href === '#' + sec.id);
      }

      var targetSrc = sec.aiAudioUrl ? sec.aiAudioUrl : (sec.gtxUrls[state.chunkIdx] || '');
      if (!targetSrc) return stepSection(1);
      audio.src = targetSrc;
      audio.playbackRate = state.rate;
      var p = audio.play();
      if (p && p.catch) {
        p.catch(function () { speakFallbackChunk(secIdx, state.chunkIdx); });
      }
      prefetchNext(secIdx, state.chunkIdx);
      updateUi();
      updateMediaSession(sec);
    }

    function advanceFrom(secIdx, chunkIdx) {
      var cur = sections[secIdx];
      if (!cur) return stopAll();
      if (!cur.aiAudioUrl && chunkIdx + 1 < cur.gtxUrls.length) {
        playAt(secIdx, chunkIdx + 1, false);
      } else if (secIdx + 1 < sections.length) {
        playAt(secIdx + 1, 0, true);
      } else {
        stopAll();
      }
    }

    function stepSection(delta) {
      var next = state.secIdx + delta;
      if (next < 0) next = 0;
      if (next >= sections.length) return stopAll();
      playAt(next, 0, true);
    }

    function togglePlayPause() {
      if (!state.active) return playAt(0, 0, true);
      if (state.playing) {
        state.playing = false;
        audio.pause();
        if ('speechSynthesis' in window) window.speechSynthesis.cancel();
      } else {
        state.playing = true;
        if (state.usingSpeech) {
          speakFallbackChunk(state.secIdx, state.chunkIdx);
        } else {
          audio.playbackRate = state.rate;
          audio.play().catch(function () { speakFallbackChunk(state.secIdx, state.chunkIdx); });
        }
      }
      updateUi();
      updateMediaSession(sections[state.secIdx]);
    }

    function stopAll() {
      state.active = false;
      state.playing = false;
      state.usingSpeech = false;
      audio.pause();
      audio.removeAttribute('src');
      if ('speechSynthesis' in window) window.speechSynthesis.cancel();
      updateUi();
    }

    audio.addEventListener('loadedmetadata', function () {
      audio.playbackRate = state.rate;
    });
    audio.addEventListener('ended', function () {
      if (!state.active || !state.playing) return;
      advanceFrom(state.secIdx, state.chunkIdx);
    });
    audio.addEventListener('error', function () {
      if (!state.active || !state.playing) return;
      speakFallbackChunk(state.secIdx, state.chunkIdx);
    });

    if (heroBtn) {
      heroBtn.addEventListener('click', function () { togglePlayPause(); });
    }
    bar.addEventListener('click', function (ev) {
      var btn = ev.target && ev.target.closest ? ev.target.closest('[data-act]') : null;
      if (!btn) return;
      var act = btn.getAttribute('data-act');
      if (act === 'toggle') togglePlayPause();
      else if (act === 'prev') stepSection(-1);
      else if (act === 'next') stepSection(1);
      else if (act === 'close') stopAll();
      else if (act === 'rate') {
        var nxtIdx = (RATES.indexOf(state.rate) + 1) % RATES.length;
        state.rate = RATES[nxtIdx];
        localStorage.setItem('fedu_tts_rate', String(state.rate));
        btnRate.textContent = state.rate + 'x';
        audio.playbackRate = state.rate;
      }
    });

    var mDoc = (location.pathname || '').match(/(logic\d+)\.html/i);
    if (mDoc) {
      var docId = mDoc[1].toLowerCase();
      fetch(MEDIA_TTS_BASE + '/index.json')
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (idxData) {
          if (!idxData || !Array.isArray(idxData.docs) || idxData.docs.indexOf(docId) < 0) return null;
          return fetch(MEDIA_TTS_BASE + '/' + docId + '/manifest.json').then(function (r2) { return r2.ok ? r2.json() : null; });
        })
        .then(function (mf) {
          if (!mf || !mf.sections) return;
          for (var i = 0; i < sections.length; i++) {
            var info = mf.sections[sections[i].id];
            if (info && info.url) sections[i].aiAudioUrl = info.url;
          }
          state.manifestLoaded = true;
          updateUi();
        })
        .catch(function () {});
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTtsEngine);
  } else {
    initTtsEngine();
  }
})();
