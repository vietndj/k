import json
import os

error_file = "error_tasks.json"

if not os.path.exists(error_file):
    print(f"Không tìm thấy file {error_file}. Bạn cần mở bảng Nghiệm Thu, đánh dấu lỗi và bấm Xuất file trước.")
    exit(1)

with open(error_file, "r", encoding="utf-8") as f:
    errors = json.load(f)

print("="*60)
print(f"ĐÃ TÌM THẤY {len(errors)} ẢNH LỖI MẶT CẦN SỬA")
print("="*60)

for i, task in enumerate(errors):
    print(f"[{i+1}/{len(errors)}] Phim: {task.get('movie', 'Unknown')}")
    print(f"  File HTML: {task.get('target_html', '')}")
    print(f"  Prompt: {task.get('prompt', '')}")
    print("-" * 40)

print("\nHướng dẫn Sửa & Nghiệm Thu:")
print("1. Copy từng prompt ở trên và chạy lại vào công cụ AI (Midjourney/DALL-E) để tạo ảnh mới (đảm bảo có Face DNA).")
print("2. Lưu ảnh mới tải về đè lên ảnh cũ trong thư mục (hoặc update vào thư mục assets/covers).")
print("3. Chạy lại câu lệnh `python3 make_audit_dashboard.py` để cập nhật bảng nghiệm thu mới nhất.")
