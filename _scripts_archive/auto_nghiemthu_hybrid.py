import os
import subprocess
import time
from playwright.sync_api import sync_playwright

REPO_DIR = '/Users/vietmac/Documents/CODE/k'
FILE_NAME = 'logic_nghiemthu.html'
FILE_PATH = os.path.join(REPO_DIR, FILE_NAME)

URL = 'https://kho.fedu.vn/logic_nghiemthu.html'
# Hoặc URL = 'https://fedu.vn/k/logic_nghiemthu.html' - tùy vào đâu là trang thật. Sẽ thử kho.fedu.vn trước.

def run_cmd(cmd):
    print(f"Chạy lệnh: {cmd}")
    subprocess.run(cmd, shell=True, cwd=REPO_DIR, check=True)

def wait_for_deploy(seconds=60):
    print(f"Đợi deploy {seconds} giây...")
    time.sleep(seconds)

def take_screenshot(step_name, filename):
    print(f"Chụp ảnh {step_name}...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Thử URL chính, nếu 404 hoặc không thành công thử URL kia (bước 3 có thể 404)
        response = page.goto(URL, wait_until='networkidle')
        # Đợi chút để page load xong
        page.wait_for_timeout(2000)
        page.screenshot(path=filename, full_page=True)
        print(f"Đã lưu {filename}")
        browser.close()

def main():
    print("Bắt đầu quy trình NGHIEM THU Hybrid Delete...")
    
    # Bước 2: Commit & Push lần 1
    run_cmd(f"git add {FILE_NAME}")
    run_cmd('git commit -m "Thêm logic_nghiemthu.html"')
    run_cmd('git push origin main')
    wait_for_deploy(60)
    
    # Bước 3: Chụp ảnh môi trường ONLINE
    take_screenshot("Bước 3 (Khởi tạo)", "nt_step1.png")
    
    # Bước 4: Tình huống 1 (Xóa 1 câu hỏi)
    print("Mô phỏng xóa Q1...")
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Tìm và xóa đoạn Q1
    import re
    # Xoá đoạn từ <!-- Q1 --> đến hết </div> của Q1
    content_new = re.sub(r'<!-- Q1 -->.*?<!-- Q2 -->', '<!-- Q2 -->', content, flags=re.DOTALL)
    
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(content_new)
        
    run_cmd(f"git add {FILE_NAME}")
    run_cmd('git commit -m "Hybrid Delete: Xóa Q1"')
    run_cmd('git push origin main')
    wait_for_deploy(60)
    
    # Bước 5: Chụp ảnh môi trường ONLINE
    take_screenshot("Bước 5 (Xóa Q1)", "nt_step2.png")
    
    # Bước 6: Tình huống 2 (Xóa cả file)
    print("Mô phỏng xóa cả file...")
    run_cmd(f"git rm {FILE_NAME}")
    run_cmd('git commit -m "Hybrid Delete: Xóa file logic_nghiemthu.html"')
    run_cmd('git push origin main')
    wait_for_deploy(60)
    
    # Bước 7: Chụp ảnh môi trường ONLINE
    take_screenshot("Bước 7 (Xóa file)", "nt_step3.png")
    
    print("Xong!")

if __name__ == "__main__":
    main()
