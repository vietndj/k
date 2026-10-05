import re

def clean_question(text):
    # Remove wrappers
    text = text.replace('&lt;USER_REQUEST&gt;', '').replace('<USER_REQUEST>', '')
    text = re.sub(r'TEAM\s*:', '', text, flags=re.IGNORECASE)
    text = re.sub(r'BẠN LÀ\s+.*?\.', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\[conversation://[^\]]+\]', '', text)
    text = re.sub(r'@[a-zA-Z0-9_"\-\[\]\s]+', '', text)
    text = text.strip()
    
    # Try to find a question mark
    parts = text.split('.')
    for p in parts:
        if '?' in p:
            q = p.split('?')[0].strip() + '?'
            if len(q) > 10:
                return q
                
    # Otherwise just take the first short sentence or substring
    text = re.sub(r'\s+', ' ', text)
    if len(text) > 150:
        first_sentence = text.split('.')[0]
        if len(first_sentence) < 150:
            return first_sentence + '...'
        else:
            return text[:147] + '...'
    return text

def process_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Fix Questions
    def repl_question(m):
        raw_text = m.group(1).strip()
        cleaned = clean_question(raw_text)
        return f'<div class="faq-question">{cleaned}<span class="faq-icon">+</span></div>'

    html = re.sub(r'<div class="faq-question">(.*?)<span class="faq-icon">\+</span></div>', repl_question, html, flags=re.DOTALL)

    # 2. Fix Answers
    def repl_answer(m):
        inner = m.group(1)
        # If it already has <ul> or <li>, leave it alone
        if '<ul' in inner or '<li' in inner:
            return m.group(0)
            
        # Convert <p> to <li>
        if '<p' in inner:
            items = re.findall(r'<p.*?>(.*?)</p>', inner, flags=re.DOTALL)
            if items:
                lis = []
                for item in items:
                    # check if the item is basically empty
                    if len(item.strip()) < 3:
                        continue
                    lis.append(f'<li style="margin-bottom: 8px;">{item.strip()}</li>')
                
                if lis:
                    ul_content = '\n'.join(lis)
                    new_inner = f'<ul style="padding-left: 20px; font-size: 15px; line-height: 1.6;">\n{ul_content}\n</ul>'
                    return f'<div class="faq-answer">\n{new_inner}\n</div>'
        
        # If no <p>, try splitting by newline
        lines = [l.strip() for l in inner.split('\n') if l.strip()]
        if lines:
            lis = [f'<li style="margin-bottom: 8px;">{l}</li>' for l in lines if len(l) > 3]
            if lis:
                ul_content = '\n'.join(lis)
                new_inner = f'<ul style="padding-left: 20px; font-size: 15px; line-height: 1.6;">\n{ul_content}\n</ul>'
                return f'<div class="faq-answer">\n{new_inner}\n</div>'
                
        return m.group(0)

    html = re.sub(r'<div class="faq-answer">(.*?)</div>', repl_answer, html, flags=re.DOTALL)
    
    # 3. Add JS Script at the very end
    script_content = """
      <script>
        // Tự động mở câu hỏi đầu tiên khi tải trang
        document.querySelectorAll('.faq-item.active').forEach(item => {
          const wrapper = item.querySelector('.faq-answer-wrapper');
          const answer = item.querySelector('.faq-answer');
          if(wrapper && answer) wrapper.style.height = answer.offsetHeight + 'px';
        });

        // Event Delegation
        document.addEventListener('click', function(e) {
          const question = e.target.closest('.faq-question');
          if (!question) return;
          
          const item = question.closest('.faq-item');
          if (!item) return;
          
          const wrapper = item.querySelector('.faq-answer-wrapper');
          const answer = item.querySelector('.faq-answer');
          
          // Đóng các câu khác
          document.querySelectorAll('.faq-item.active').forEach(other => {
            if (other !== item) {
              other.classList.remove('active');
              const w = other.querySelector('.faq-answer-wrapper');
              if (w) w.style.height = '0';
            }
          });
          
          // Toggle câu hiện tại
          if (item.classList.contains('active')) {
            item.classList.remove('active');
            if (wrapper) wrapper.style.height = '0';
          } else {
            item.classList.add('active');
            if (wrapper && answer) wrapper.style.height = answer.offsetHeight + 'px';
          }
        });
      </script>
"""
    # Remove existing script if any that matches faq
    html = re.sub(r'<script>[^<]*faq-item[^<]*</script>', '', html, flags=re.DOTALL)
    
    if "document.addEventListener('click'" not in html:
        html = html.replace('</body>', script_content + '\n</body>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    process_html('/Users/vietmac/Documents/CODE/k/logickenh-xaykenh-1.0.html')
    print("Processed safely.")
