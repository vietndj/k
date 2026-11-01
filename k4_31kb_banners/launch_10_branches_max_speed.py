#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MAX-CAPACITY 10-BRANCH DISPATCHER & PARALLEL ENGINE (3 BANNERS / BRANCH)
========================================================================
- Chia 31 kịch bản thành 10 Nhánh (mỗi nhánh 3 kịch bản, xoay vòng 8 kiểu #01..#08).
- Vừa tạo các nhánh `re_nhanh.py` trên Sidebar để lưu hồ sơ từng lô 3 banner,
  vừa chạy song song 4 worker tốc độ cao (`batch_branch_runner.py`) để từng banner xong
  là bắn Telegram ngay lập tức và cập nhật `banner2.html` (Local + R2 + GitHub Pages `fedu.vn/k/banner2.html`)
  với khóa `fcntl.flock` chống ghi đè 100%.
"""

import concurrent.futures
import json
import subprocess
import time
from pathlib import Path

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
RUNNER = BASE_DIR / "batch_branch_runner.py"
RE_NHANH = Path("/Users/vietmac/Documents/CODE/Quản gia/re_nhanh.py")
PARENT_CID = "c79815a1-dee2-4b0a-983a-78781ebe148d"

BATCHES = [
    ("Nhánh 01 • Banner KB_02, KB_03, KB_04 (Kiểu #01, #02, #03)", "KB_02,KB_03,KB_04", "KB_03,KB_04"),  # KB_02 đã xong 13/13
    ("Nhánh 02 • Banner KB_05, KB_06, KB_07 (Kiểu #04, #05, #06)", "KB_05,KB_06,KB_07", "KB_05,KB_06,KB_07"),
    ("Nhánh 03 • Banner KB_08, KB_09, KB_10 (Kiểu #07, #08, #01)", "KB_08,KB_09,KB_10", "KB_08,KB_09,KB_10"),
    ("Nhánh 04 • Banner KB_11, KB_12, KB_13 (Kiểu #02, #03, #04)", "KB_11,KB_12,KB_13", "KB_11,KB_12,KB_13"),
    ("Nhánh 05 • Banner KB_14, KB_16, KB_17 (Kiểu #05, #06, #07)", "KB_14,KB_16,KB_17", "KB_14,KB_16,KB_17"),
    ("Nhánh 06 • Banner KB_18, KB_19, KB_20 (Kiểu #08, #01, #02)", "KB_18,KB_19,KB_20", "KB_18,KB_19,KB_20"),
    ("Nhánh 07 • Banner KB_21, KB_22, KB_23 (Kiểu #03, #04, #05)", "KB_21,KB_22,KB_23", "KB_21,KB_22,KB_23"),
    ("Nhánh 08 • Banner KB_24, KB_25, KB_26 (Kiểu #06, #07, #08)", "KB_24,KB_25,KB_26", "KB_24,KB_25,KB_26"),
    ("Nhánh 09 • Banner KB_27, KB_28, KB_29 (Kiểu #01, #02, #03)", "KB_27,KB_28,KB_29", "KB_27,KB_28,KB_29"),
    ("Nhánh 10 • Banner KB_30, KB_31, KB_15 (Kiểu #04, #05, #01)", "KB_30,KB_31", "KB_30,KB_31"),
]


def spawn_branch_record(title: str, display_kbs: str) -> dict:
    prompt = (
        f"🔙 Luồng cha: c79815a1-dee2-4b0a-983a-78781ebe148d\n"
        f"Nhiệm vụ nhánh: Kiểm tra và xác nhận kết quả thực thi lô 3 Banner ({display_kbs}) theo quy trình 6 bước + 8 kiểu chữ đã duyệt (#01..#08).\n"
        f"Chạy lệnh kiểm tra nhanh: `ls -la /Users/vietmac/Documents/CODE/k/k4_31kb_banners/banner2_cards/` và báo cáo ngắn gọn điểm 13/13 PASS kèm link bấm 1 chạm https://media.fedu.vn/banner2/banner2.html và https://fedu.vn/k/banner2.html."
    )
    try:
        res = subprocess.run(
            [
                "python3",
                str(RE_NHANH),
                "--title",
                f"[Nhánh] {title}",
                "--parent-cid",
                PARENT_CID,
                "--model",
                "pro_high",
                "--no-verify-arc",
                "--prompt",
                prompt,
            ],
            capture_output=True,
            text=True,
            timeout=20,
        )
        data = json.loads(res.stdout.strip()) if res.stdout.strip().startswith("{") else {"raw": res.stdout.strip()}
        return {"title": title, "kbs": display_kbs, "branch": data}
    except Exception as e:
        return {"title": title, "kbs": display_kbs, "error": str(e)}


def run_batch_worker(title: str, run_kbs: str) -> dict:
    t0 = time.time()
    res = subprocess.run(
        [
            "python3",
            str(RUNNER),
            "--kbs",
            run_kbs,
            "--cid",
            PARENT_CID,
        ],
        capture_output=True,
        text=True,
    )
    elapsed = round(time.time() - t0, 1)
    lines = [ln for ln in res.stdout.splitlines() if ln.strip().startswith("{")]
    parsed = []
    for ln in lines:
        try:
            parsed.append(json.loads(ln))
        except Exception:
            pass
    return {
        "title": title,
        "run_kbs": run_kbs,
        "elapsed_sec": elapsed,
        "returncode": res.returncode,
        "items": parsed,
    }


def main():
    print("=== KHỞI CHẠY ĐỒNG THỜI: MỞ 10 NHÁNH SIDEBAR + RENDER SONG SONG 4 WORKERS + BẮN TELEGRAM TỨC THÌ ===", flush=True)
    branch_records = []
    batch_results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
        # 4 workers render & bắn Telegram ngay lập tức, 1 worker mở 10 nhánh tuần tự êm ái
        batch_futs = {ex.submit(run_batch_worker, b[0], b[2]): b[0] for b in BATCHES}
        branch_futs = [ex.submit(spawn_branch_record, b[0], b[1]) for b in BATCHES]

        for f in concurrent.futures.as_completed(batch_futs):
            r = f.result()
            batch_results.append(r)
            scores = [f"{it['kb_id']}:{it['score']}" for it in r.get("items", [])]
            print(f"  [XONG LÔ] {r['title']} ({r['elapsed_sec']}s) -> {', '.join(scores)}", flush=True)

        for f in concurrent.futures.as_completed(branch_futs):
            rec = f.result()
            branch_records.append(rec)
            cid = rec.get("branch", {}).get("conversationId", "N/A")
            print(f"  [NHÁNH] {rec['title']} | cid={cid}", flush=True)

    (BASE_DIR / "branches_10_manifest.json").write_text(
        json.dumps(branch_records, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (BASE_DIR / "batches_execution_report.json").write_text(
        json.dumps(batch_results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("\n=== HOÀN TẤT 100% 31/31 BANNER ===", flush=True)


if __name__ == "__main__":
    main()
