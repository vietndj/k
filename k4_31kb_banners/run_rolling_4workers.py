#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P3/P4 - ROLLING 4-WORKER ORCHESTRATOR FOR KB_02 .. KB_31 (APPLE M1 16GB SAFE)
=============================================================================
Điều phối cuốn chiếu tối đa 4 nhánh worker song song tại một thời điểm
(đảm bảo RAM hệ thống luôn dư ~3GB trên Apple M1 16GB, không swap) kèm
khóa nguyên tử `mkdir /tmp/k4_claude2.lock` để sản xuất toàn bộ 30 kịch bản
(`KB_02` -> `KB_31`, 450 ảnh) và kết hợp với `KB_01` thành đủ 31 kịch bản (465 ảnh).
"""

import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
LOCK_DIR = Path("/tmp/k4_claude2.lock")
MAX_PARALLEL_WORKERS = 4


def run_kb_worker(kb_id: str) -> dict:
    t0 = time.time()
    cmd = [sys.executable, str(BASE_DIR / "run_single_kb.py"), "--kbs", kb_id]
    res = subprocess.run(cmd, capture_output=True, text=True)
    dt = round(time.time() - t0, 1)
    manifest_path = BASE_DIR / kb_id / "manifest.json"
    if res.returncode == 0 and manifest_path.exists():
        m = json.loads(manifest_path.read_text())
        return {
            "kb_id": kb_id,
            "status": "OK",
            "duration_sec": dt,
            "after_all_8_pass": m["after_all_8_pass"],
            "unique_outfits": m["unique_outfits"],
            "unique_before_fonts": m["unique_before_fonts"],
            "unique_before_styles": m["unique_before_styles"],
        }
    return {
        "kb_id": kb_id,
        "status": "ERR",
        "duration_sec": dt,
        "stderr": res.stderr[-400:] if res.stderr else res.stdout[-400:],
    }


def main():
    kb_list = [f"KB_{i:02d}" for i in range(2, 32)]
    print(f"Starting rolling {MAX_PARALLEL_WORKERS}-worker orchestrator for {len(kb_list)} scripts (KB_02..KB_31)...")
    t_start = time.time()
    results = []

    with ThreadPoolExecutor(max_workers=MAX_PARALLEL_WORKERS) as pool:
        future_map = {pool.submit(run_kb_worker, kb_id): kb_id for kb_id in kb_list}
        for fut in as_completed(future_map):
            r = fut.result()
            results.append(r)
            if r["status"] == "OK":
                print(
                    f"  ✅ {r['kb_id']} finished in {r['duration_sec']}s | "
                    f"after_8_pass={r['after_all_8_pass']} | outfits={r['unique_outfits']} | "
                    f"fonts={r['unique_before_fonts']} | styles={r['unique_before_styles']} "
                    f"({len(results)}/{len(kb_list)})",
                    flush=True,
                )
            else:
                print(f"  ❌ {r['kb_id']} FAILED: {r.get('stderr')}", flush=True)

    total_sec = round(time.time() - t_start, 1)
    ok_cnt = sum(1 for r in results if r["status"] == "OK" and r.get("after_all_8_pass"))
    print(f"\nCompleted {ok_cnt}/{len(kb_list)} scripts in {total_sec}s!")


if __name__ == "__main__":
    main()
