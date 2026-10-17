import json
import os

error_file = "error_tasks.json"
download_dir_file = os.path.expanduser("~/Downloads/error_tasks.json")

# Ưu tiên lấy file trong thư mục k, nếu không có thì tìm trong Downloads
if os.path.exists(error_file):
    target_file = error_file
elif os.path.exists(download_dir_file):
    target_file = download_dir_file
    print(f"-> Đã tự động nhận diện file lỗi tại: {target_file}")
else:
    print(f"Không tìm thấy file error_tasks.json trong thư mục hiện tại hoặc Downloads.")
    print("Vui lòng mở bảng Nghiệm Thu, đánh dấu lỗi và bấm Xuất Data Lỗi trước.")
    exit(1)

with open(target_file, "r", encoding="utf-8") as f:
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
print("1. Copy từng prompt ở trên và chạy lại vào công cụ AI để tạo ảnh mới.")
print("2. Lưu ảnh mới tải về đè lên ảnh cũ.")
print("3. Chạy lại lệnh `python3 make_audit_dashboard.py` để cập nhật bảng.")
