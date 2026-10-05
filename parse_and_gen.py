import json

with open('/Users/vietmac/Documents/CODE/k/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

gatekeeper = "".join(lines[:268])
auth_js = """
        const AUTH_STORAGE_KEY = 'fedu_vault_auth_v1';
        const PASSCODE_PLAIN = '0070';
        const PASSCODE_HASH = '71ffe84afd528a0365d6ec95c89a64cd6979b4a15730649feddf2dc390db9e3c';

        async function sha256Hex(str) {
            try {
                const buffer = new TextEncoder().encode(str);
                const hash = await crypto.subtle.digest('SHA-256', buffer);
                return Array.from(new Uint8Array(hash)).map(b => b.toString(16).padStart(2, '0')).join('');
            } catch (e) {
                return '';
            }
        }

        function isUserUnlocked() {
            return localStorage.getItem(AUTH_STORAGE_KEY) === PASSCODE_HASH;
        }

        let feedInitialized = false;
        function unlockVault() {
            localStorage.setItem(AUTH_STORAGE_KEY, PASSCODE_HASH);
            const gate = document.getElementById('gatekeeper-screen');
            const app = document.getElementById('app-view');
            if (gate) gate.style.display = 'none';
            if (app) app.style.display = 'flex';
            if (!feedInitialized) {
                feedInitialized = true;
                initFeed();
            }
        }

        function lockVault() {
            localStorage.removeItem(AUTH_STORAGE_KEY);
            window.location.reload();
        }

        async function verifyPasscode(rawPin) {
            const pin = (rawPin || '').trim();
            const pinCard = document.getElementById('pin-card');
            const pinFeedback = document.getElementById('pin-feedback');
            const pinInput = document.getElementById('pin-input');

            if (!pin) {
                if (pinFeedback) {
                    pinFeedback.textContent = 'Vui lòng nhập mật khẩu';
                    pinFeedback.className = 'text-xs min-h-[18px] text-amber-400 font-mono';
                }
                return;
            }

            let isCorrect = (pin === PASSCODE_PLAIN);
            if (!isCorrect) {
                const hash = await sha256Hex(pin);
                if (hash === PASSCODE_HASH) isCorrect = true;
            }

            if (isCorrect) {
                if (pinFeedback) {
                    pinFeedback.textContent = '✅ Mật khẩu chính xác! Đang mở khóa...';
                    pinFeedback.className = 'text-xs min-h-[18px] text-emerald-400 font-mono font-semibold';
                }
                if (pinCard) pinCard.classList.remove('animate-shake');
                setTimeout(() => {
                    unlockVault();
                }, 200);
            } else {
                if (pinCard) {
                    pinCard.classList.remove('animate-shake');
                    void pinCard.offsetWidth; // trigger reflow
                    pinCard.classList.add('animate-shake');
                }
                if (pinFeedback) {
                    pinFeedback.textContent = '❌ Mật khẩu không đúng. Vui lòng thử lại!';
                    pinFeedback.className = 'text-xs min-h-[18px] text-rose-400 font-mono font-semibold';
                }
                if (pinInput) {
                    pinInput.value = '';
                    pinInput.focus();
                }
            }
        }
"""
