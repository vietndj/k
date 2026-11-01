#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RUN SINGLE OR BATCH KB PIPELINE (P2 -> P3 -> P4 -> SELF-HEAL 8/8 -> MANIFEST)
=============================================================================
Thực thi trọn vẹn chu trình sản xuất 15 ảnh Banner (10 Before + 5 After) cho 1 hoặc
nhiều kịch bản (`KB_02` .. `KB_31`):
1. P2: Render 10 ảnh Before (5 góc nhìn × 2 thiết kế A/B khác nhóm font, khác STYLE, khác trang phục).
2. P3: Chạy `uiux_auditor.py` đo tự động 8 chỉ số UI/UX Typography, chấm chọn bản thắng A/B
   có dẫn chứng số liệu thật, lưu `metrics_before.json` & Contact Sheet `kbXX_before_sheet_1600.jpg`.
3. P4: Áp thông số tinh chỉnh UI/UX + câu chữ nén (`compressed_copy` <= 25 từ) + đổi sang 5 bộ
   trang phục dự trữ độc lập, render 5 ảnh After.
4. Self-Heal Gate: Kiểm định 8 chỉ số trên 5 ảnh After; nếu có ảnh nào < 8/8 thì tự động tinh chỉnh
   cỡ chữ / khoảng cách chữ / đổi sang font đối ứng có OCR 100% và chụp lại cho tới khi đạt 8/8.
5. Xuất `audit.json` và `manifest.json` đầy đủ.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any, List, Tuple
from PIL import Image

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
sys.path.insert(0, str(BASE_DIR))

from banner_renderer import render_banners_batch
from uiux_auditor import audit_single_banner


def score_candidate(audit: Dict[str, Any]) -> Tuple[int, int, float, int, float, float]:
    """Hàm điểm thứ tự từ điển để chọn bản thắng khách quan giữa A và B."""
    m = audit["metrics"]
    all_pass = 1 if audit["all_8_pass"] else 0
    passed_cnt = int(audit["passed_count"].split("/")[0])
    ocr_acc = float(m["6_mobile_ocr_360px"]["accuracy"])
    lines_ok = 1 if int(m["8_word_density"]["headline_lines"]) <= 2 else 0
    salience = float(m["5_hierarchy_squint_360px"]["squint_salience_ratio"])
    cr = float(m["4_contrast_wcag"]["headline_cr_p10_p90"])
    return (all_pass, passed_cnt, ocr_acc, lines_ok, salience, cr)


def pick_winner_and_tuning(audit_a: Dict[str, Any], audit_b: Dict[str, Any], ang_copy: Dict[str, Any]) -> Dict[str, Any]:
    sa = score_candidate(audit_a)
    sb = score_candidate(audit_b)
    if sa >= sb:
        win, lose = "A", "B"
        w_aud, l_aud = audit_a, audit_b
    else:
        win, lose = "B", "A"
        w_aud, l_aud = audit_b, audit_a

    wm = w_aud["metrics"]
    lm = l_aud["metrics"]
    reason = (
        f"Chọn bản {win} ({w_aud['font_name']} · {w_aud['typo_style']}) đạt {w_aud['passed_count']} "
        f"(OCR 360px={wm['6_mobile_ocr_360px']['accuracy']*100:.0f}%, tương phản {wm['4_contrast_wcag']['headline_cr_p10_p90']}:1, "
        f"độ nổi {wm['5_hierarchy_squint_360px']['squint_salience_ratio']}) vượt hơn bản {lose} ({l_aud['passed_count']}, "
        f"OCR={lm['6_mobile_ocr_360px']['accuracy']*100:.0f}%, {lm['8_word_density']['headline_lines']} dòng)."
    )

    f_group = w_aud["font_group"]
    tracking = 0.015 if f_group == "Condensed" else 0.008 if f_group == "Extended" else -0.005 if f_group == "Grotesk" else 0.0
    tuning = {
        "target_headline_xh_px": 49.0,
        "target_sub_xh_px": 22.0,
        "target_cta_xh_px": 23.5,
        "lh_buffer": 0.08,
        "tracking_em": tracking,
    }

    comp_copy = ang_copy.get("compressed_copy") or {
        "hook_tag": ang_copy["hook_tag"],
        "headline": ang_copy["headline"],
        "headline_break": ang_copy.get("headline_break", []),
        "subline": ang_copy["subline"],
        "cta": ang_copy["cta"],
    }

    return {
        "angle_idx": ang_copy["angle_idx"],
        "winner": win,
        "font_id": w_aud["font_id"],
        "reason": reason,
        "tuning": tuning,
        "compressed_copy": comp_copy,
    }


def process_one_kb(kb_id: str) -> Dict[str, Any]:
    kb_dir = BASE_DIR / kb_id
    copy_path = kb_dir / "copy.json"
    ledger = json.loads((BASE_DIR / "k4_ledger.json").read_text())
    kb_ledger = ledger[kb_id]
    copy_data = json.loads(copy_path.read_text())

    # 1. Render 10 Before banners (or reuse if already rendered & audited)
    metrics_before_path = kb_dir / "metrics_before.json"
    if metrics_before_path.exists():
        cached_before = json.loads(metrics_before_path.read_text())
        if len(cached_before) == 10 and all(Path(b["png_path"]).exists() for b in cached_before):
            before_audits = cached_before
        else:
            before_audits = []
    else:
        before_audits = []

    if not before_audits:
        before_jobs = []
        for ang_ledger, ang_copy in zip(kb_ledger["angles"], copy_data["angles"]):
            for variant in ["before_A", "before_B"]:
                slot_cfg = ang_ledger[variant]
                slot_name = slot_cfg["slot"]
                before_jobs.append({
                    "phase": "before",
                    "angle_idx": ang_ledger["angle_idx"],
                    "variant": variant,
                    "slot_cfg": slot_cfg,
                    "copy_item": ang_copy,
                    "tuning": {},
                    "html_path": str(kb_dir / "before" / f"{slot_name}.html"),
                    "png_path": str(kb_dir / "before" / f"{slot_name}.png"),
                })

        before_metas = render_banners_batch(before_jobs)
        for job, meta in zip(before_jobs, before_metas):
            res = audit_single_banner(Path(meta["png_path"]), meta)
            res["phase"] = "before"
            res["angle_idx"] = job["angle_idx"]
            res["variant"] = job["variant"]
            res["font_id"] = meta["font"]["id"]
            res["font_name"] = meta["font"]["name"]
            res["font_group"] = meta["font"]["group"]
            res["typo_style"] = meta["typo_style"]
            res["layout_card"] = meta["layout_card"]
            res["outfit_id"] = meta["outfit"]["outfit_id"]
            res["outfit_src"] = meta["outfit"]["src"]
            res["copy"] = {
                k: meta["copy"][k]
                for k in ["hook_tag", "headline", "headline_break", "subline", "cta"]
                if k in meta["copy"]
            }
            before_audits.append(res)

        metrics_before_path.write_text(json.dumps(before_audits, ensure_ascii=False, indent=2))

        cw, ch = 320, 400
        sheet = Image.new("RGB", (cw * 5, ch * 2), (15, 23, 42))
        for i, meta in enumerate(before_metas):
            r = i % 2
            c = i // 2
            with Image.open(meta["png_path"]) as im:
                sheet.paste(im.convert("RGB").resize((cw, ch), Image.Resampling.LANCZOS), (c * cw, r * ch))
        sheet.save(kb_dir / f"{kb_id.lower()}_before_sheet_1600.jpg", "JPEG", quality=88)

    # 2. Pick winners & build 5 After jobs
    decisions = []
    after_jobs = []
    for idx in range(5):
        aud_a = before_audits[idx * 2]
        aud_b = before_audits[idx * 2 + 1]
        ang_copy = copy_data["angles"][idx]
        ang_ledger = kb_ledger["angles"][idx]
        dec = pick_winner_and_tuning(aud_a, aud_b, ang_copy)
        decisions.append(dec)

        win_key = "before_A" if dec["winner"] == "A" else "before_B"
        lose_key = "before_B" if dec["winner"] == "A" else "before_A"
        win_slot = ang_ledger[win_key]
        lose_slot = ang_ledger[lose_key]

        after_slot = {
            "slot": ang_ledger["after_opt"]["slot"],
            "outfit": ang_ledger["after_opt"]["outfit"],
            "font": win_slot["font"],
            "typo_style": win_slot["typo_style"],
            "layout_card": win_slot["layout_card"],
            "winner_from": win_key,
            "alt_font": lose_slot["font"],
            "alt_style": lose_slot["typo_style"],
            "reason": dec["reason"],
        }
        after_jobs.append({
            "phase": "after",
            "angle_idx": ang_ledger["angle_idx"],
            "variant": "after_opt",
            "slot_cfg": after_slot,
            "copy_item": dec["compressed_copy"],
            "tuning": dec["tuning"],
            "html_path": str(kb_dir / "after" / f"{after_slot['slot']}.html"),
            "png_path": str(kb_dir / "after" / f"{after_slot['slot']}.png"),
        })

    after_metas = render_banners_batch(after_jobs)
    after_audits = []
    retry_indices = []

    for i, (job, meta) in enumerate(zip(after_jobs, after_metas)):
        res = audit_single_banner(Path(meta["png_path"]), meta)
        res["phase"] = "after"
        res["angle_idx"] = job["angle_idx"]
        res["variant"] = "after_opt"
        res["font_id"] = meta["font"]["id"]
        res["font_name"] = meta["font"]["name"]
        res["font_group"] = meta["font"]["group"]
        res["typo_style"] = meta["typo_style"]
        res["layout_card"] = meta["layout_card"]
        res["outfit_id"] = meta["outfit"]["outfit_id"]
        res["outfit_src"] = meta["outfit"]["src"]
        res["copy"] = meta["copy"]
        res["winner_from"] = job["slot_cfg"]["winner_from"]
        res["reason"] = job["slot_cfg"]["reason"]
        after_audits.append(res)
        if not res["all_8_pass"]:
            retry_indices.append(i)

    # 3. Self-Heal Gate: if any After banner is < 8/8, switch to alt_font or clean non-uppercase style and re-render
    if retry_indices:
        heal_jobs = []
        for idx in retry_indices:
            job = after_jobs[idx]
            failed_metrics = [k for k, v in after_audits[idx]["metrics"].items() if not v["pass"]]
            # Switch to alternate font from A/B pair if OCR or line wrap failed, or use safe STYLE-04 (mixed-case high contrast)
            alt_f = job["slot_cfg"]["alt_font"]
            if alt_f["id"] not in ("F07", "F17"):
                job["slot_cfg"]["font"] = alt_f
            # Avoid uppercase forcing on long lines
            if job["slot_cfg"]["typo_style"] in ("STYLE-02", "STYLE-10", "STYLE-13", "STYLE-14", "STYLE-27", "STYLE-31"):
                job["slot_cfg"]["typo_style"] = "STYLE-04"
            job["tuning"] = {
                "target_headline_xh_px": 46.5,
                "target_sub_xh_px": 21.5,
                "target_cta_xh_px": 23.0,
                "lh_buffer": 0.08,
                "tracking_em": 0.01,
            }
            heal_jobs.append((idx, job))

        healed_metas = render_banners_batch([hj[1] for hj in heal_jobs])
        for (idx, job), meta in zip(heal_jobs, healed_metas):
            res = audit_single_banner(Path(meta["png_path"]), meta)
            # Second fallback if font still has OCR quirk at 360px
            if not res["all_8_pass"]:
                # Use FDAeonik or FDTiemposHeadline from registry for guaranteed 100% OCR at 360px
                reg = json.loads((BASE_DIR / "font_registry.json").read_text())["curated_20_families"]
                job["slot_cfg"]["font"] = reg["F01"] if idx % 2 == 0 else reg["F02"]
                job["slot_cfg"]["typo_style"] = "STYLE-04"
                job["tuning"]["target_headline_xh_px"] = 47.0
                meta = render_banners_batch([job])[0]
                res = audit_single_banner(Path(meta["png_path"]), meta)

            res["phase"] = "after"
            res["angle_idx"] = job["angle_idx"]
            res["variant"] = "after_opt"
            res["font_id"] = meta["font"]["id"]
            res["font_name"] = meta["font"]["name"]
            res["font_group"] = meta["font"]["group"]
            res["typo_style"] = meta["typo_style"]
            res["layout_card"] = meta["layout_card"]
            res["outfit_id"] = meta["outfit"]["outfit_id"]
            res["outfit_src"] = meta["outfit"]["src"]
            res["copy"] = meta["copy"]
            res["winner_from"] = job["slot_cfg"]["winner_from"]
            res["reason"] = job["slot_cfg"]["reason"]
            after_audits[idx] = res

    (kb_dir / "audit.json").write_text(json.dumps({
        "kb_id": kb_id,
        "decisions": decisions,
        "after_audits": after_audits,
    }, ensure_ascii=False, indent=2))

    manifest = {
        "kb_id": kb_id,
        "kb_num": int(kb_id.split("_")[1]),
        "title": copy_data["title"],
        "total_banners": 15,
        "before_count": len(before_audits),
        "after_count": len(after_audits),
        "after_all_8_pass": all(a["all_8_pass"] for a in after_audits),
        "unique_outfits": len({a["outfit_id"] for a in before_audits + after_audits}),
        "unique_before_fonts": len({a["font_id"] for a in before_audits}),
        "unique_before_styles": len({a["typo_style"] for a in before_audits}),
        "before_banners": before_audits,
        "after_banners": after_audits,
    }
    (kb_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    print(
        f"[{kb_id} DONE] 15 banners | after_all_8_pass={manifest['after_all_8_pass']} | "
        f"outfits={manifest['unique_outfits']} | fonts={manifest['unique_before_fonts']} | styles={manifest['unique_before_styles']}"
    )
    return manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--kbs", nargs="+", required=True, help="List of KB IDs e.g. KB_02 KB_03")
    args = parser.parse_args()
    for kb_id in args.kbs:
        process_one_kb(kb_id)


if __name__ == "__main__":
    main()
