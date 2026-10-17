import re
from bs4 import BeautifulSoup
import sys

def clean_question(text):
    text = text.replace('<USER_REQUEST>', '').strip()
    text = re.sub(r'TEAM\s*:', '', text, flags=re.IGNORECASE).strip()
    text = re.sub(r'BẠN LÀ\s+.*?\.', '', text, flags=re.IGNORECASE).strip()
    text = re.sub(r'\[conversation://[^\]]+\]', '', text).strip()
    
    # If the text has a clear question, use that
    parts = text.split('.')
    for p in parts:
        if '?' in p:
            q = p.split('?')[0].strip() + '?'
            if len(q) > 10:
                return q
                
    # Otherwise, try to find a short first sentence or a summary
    text = re.sub(r'\s+', ' ', text)
    if len(text) > 120:
        # Take the first sentence
        first_sentence = text.split('.')[0]
        if len(first_sentence) < 120:
            return first_sentence + '...'
        else:
            return text[:117] + '...'
    return text

def summarize_answer(answer_tag, soup):
    # Check if already has ul
    if answer_tag.find('ul'):
        return
        
    paragraphs = answer_tag.find_all('p')
    if not paragraphs:
        # Maybe raw text
        text = answer_tag.get_text(separator='\n').strip()
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        if not lines:
            return
        ul = soup.new_tag('ul', style="padding-left: 20px; font-size: 15px; line-height: 1.6;")
        for line in lines:
            li = soup.new_tag('li', style="margin-bottom: 8px;")
            # Remove Markdown-like bold for HTML rendering
            line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            li.append(BeautifulSoup(line, 'html.parser'))
            ul.append(li)
        answer_tag.clear()
        answer_tag.append(ul)
        return

    # Convert paragraphs to list items
    ul = soup.new_tag('ul', style="padding-left: 20px; font-size: 15px; line-height: 1.6;")
    for p in paragraphs:
        text = p.get_text(separator='\n').strip()
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        for line in lines:
            # Skip very short lines or separators
            if len(line) < 5 or line == '---':
                continue
            li = soup.new_tag('li', style="margin-bottom: 8px;")
            line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            li.append(BeautifulSoup(line, 'html.parser'))
            ul.append(li)
            
    answer_tag.clear()
    answer_tag.append(ul)

def main():
    file_path = '/Users/vietmac/Documents/CODE/k/logickenh-xaykenh-1.0.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    faq_items = soup.find_all('div', class_='faq-item')
    for item in faq_items:
        q_tag = item.find('div', class_='faq-question')
        if q_tag:
            # Save the span icon
            icon = q_tag.find('span', class_='faq-icon')
            if icon:
                icon.extract()
            
            raw_text = q_tag.get_text().strip()
            cleaned = clean_question(raw_text)
            
            q_tag.clear()
            q_tag.append(cleaned)
            if icon:
                q_tag.append(icon)
                
        a_tag = item.find('div', class_='faq-answer')
        if a_tag:
            summarize_answer(a_tag, soup)
            
    # Add script if not exists
    script_content = """
        // Tự động mở câu hỏi đầu tiên khi tải trang
        document.querySelectorAll('.faq-item.active').forEach(item => {
          const wrapper = item.querySelector('.faq-answer-wrapper');
          const answer = item.querySelector('.faq-answer');
          if (wrapper && answer) wrapper.style.height = answer.offsetHeight + 'px';
        });

        // Event Delegation cho FAQ toggle
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
    """
    
    body = soup.find('body')
    script_exists = False
    for script in body.find_all('script'):
        if 'Event Delegation' in script.text or 'faq-item' in script.text:
            script_exists = True
            break
            
    if not script_exists:
        new_script = soup.new_tag('script')
        new_script.string = script_content
        body.append(new_script)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Done")

if __name__ == '__main__':
    main()
