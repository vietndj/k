#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render Showcase Poster cho 38 Logo Gmail của anh Việt bằng Playwright.
Xuất ảnh 2x retina siêu sắc nét.
"""

import asyncio
import json
import os
from playwright.async_api import async_playwright

JSON_PATH = '/Users/vietmac/Documents/CODE/k/gmail_assets.json'
OUT_POSTER = '/Users/vietmac/Documents/CODE/k/assets/logos/gmail/gmail_showcase.png'
OUT_SINGLE_DIR = '/Users/vietmac/Documents/CODE/k/assets/logos/gmail/png'

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    items = json.load(f)

# Tạo HTML template cho Showcase Poster
cards_html = ""
for item in items:
    is_inactive = item['status'] == 'inactive'
    opacity = "0.5" if is_inactive else "1"
    border_color = "rgba(255,255,255,0.06)" if is_inactive else "rgba(255,255,255,0.12)"
    status_badge = f"<span style='font-size: 10px; color: #ef4444; background: rgba(239,68,68,0.15); padding: 2px 6px; border-radius: 4px; font-weight: 700;'>TẠM ẨN</span>" if is_inactive else ""
    
    cards_html += f"""
    <div class="card" style="opacity: {opacity}; border-color: {border_color};">
      <div class="logo-box">
        {item['svg_dark']}
      </div>
      <div class="info-box">
        <div style="display: flex; align-items: center; justify-content: space-between; gap: 6px;">
          <span class="acc-name">{item['name']}</span>
          <span class="code-pill" style="color: {item['color']}; border-color: {item['color']}40; background: {item['color']}15;">{item['code']}</span>
        </div>
        <div class="acc-desc">{item['desc'].split('•')[0].strip()}</div>
        <div class="acc-meta">
          <span style="color: {item['color']}; font-weight: 600;">{item['color_name']}</span>
          {status_badge}
        </div>
      </div>
    </div>
    """

poster_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @font-face {{
    font-family: 'FD Aeonik Extended';
    src: url('/Users/vietmac/Library/Fonts/FDAeonikExtended-Bold.ttf') format('truetype');
    font-weight: 700;
  }}
  @font-face {{
    font-family: 'FD Aeonik';
    src: url('/Users/vietmac/Library/Fonts/FDAeonikRegular.ttf') format('truetype');
    font-weight: 400;
  }}
  @font-face {{
    font-family: 'FD Anguita Sans';
    src: url('/Users/vietmac/Library/Fonts/FDAnguitaSans-Black.ttf') format('truetype');
    font-weight: 900;
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: #07090E;
    color: #F8FAFC;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    width: 1400px;
    padding: 60px 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }}

  .header {{
    text-align: center;
    margin-bottom: 44px;
    max-width: 1000px;
  }}
  .badge {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 18px;
    border-radius: 9999px;
    background: #111622;
    border: 1px solid rgba(255,255,255,0.18);
    color: #38BDF8;
    font-family: ui-monospace, monospace;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 16px;
  }}
  .title {{
    font-size: 34px;
    font-weight: 800;
    letter-spacing: 0.02em;
    color: #FFFFFF;
    text-transform: uppercase;
    margin-bottom: 12px;
    line-height: 1.2;
  }}
  .subtitle {{
    font-size: 16px;
    color: #94A3B8;
    line-height: 1.6;
  }}

  .grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 16px;
    width: 100%;
    margin-bottom: 40px;
  }}

  .card {{
    background: #0E131F;
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 16px;
    display: flex;
    align-items: center;
    gap: 14px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
  }}

  .logo-box {{
    width: 58px;
    height: 58px;
    flex-shrink: 0;
    border-radius: 14px;
    overflow: hidden;
    background: #07090E;
    border: 1px solid rgba(255,255,255,0.08);
  }}
  .logo-box svg {{
    width: 100%;
    height: 100%;
    display: block;
  }}

  .info-box {{
    flex: 1;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    gap: 3px;
  }}

  .acc-name {{
    font-size: 13.5px;
    font-weight: 700;
    color: #FFFFFF;
    font-family: ui-monospace, monospace;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}

  .code-pill {{
    font-size: 11px;
    font-weight: 800;
    font-family: ui-monospace, monospace;
    padding: 2px 7px;
    border-radius: 6px;
    border: 1px solid;
    flex-shrink: 0;
  }}

  .acc-desc {{
    font-size: 11.5px;
    color: #94A3B8;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}

  .acc-meta {{
    font-size: 10.5px;
    display: flex;
    align-items: center;
    gap: 6px;
    margin-top: 2px;
  }}

  .footer {{
    width: 100%;
    border-top: 1px solid rgba(255,255,255,0.1);
    padding-top: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #64748B;
    font-size: 13px;
  }}
</style>
</head>
<body>
  <div class="header">
    <div class="badge">FD ANGUITA SANS BLACK • SIGNATURE DOT • 38 GMAIL PROFILES</div>
    <h1 class="title">BỘ NHẬN DIỆN LOGO 38 TÀI KHOẢN GMAIL • NGUYỄN VIỆT</h1>
    <p class="subtitle">
      Định danh thị giác độc quyền theo triết lý <strong>brand.html</strong>: Monogram nét 900 Black condensed chiếm 85% khung hình, góc bo rx=16, dấu chấm nhận diện quang học cx=52, cy=13. Tối ưu cực đại từ 16px Chrome Tab đến 1024px Profile Avatar.
    </p>
  </div>

  <div class="grid">
    {cards_html}
  </div>

  <div class="footer">
    <div>🚀 <strong>Hệ Điều Hành Cổng:</strong> fedu.vn/k/gmail_brand.html • Kho Mã Nguồn: github.com/vietndj/k</div>
    <div>💎 <strong>Quản Gia AI:</strong> Closed-Loop Vector Monogram • Chuẩn Apple/Chrome 2026</div>
  </div>
</body>
</html>
"""

async def main():
    print("🎨 Đang khởi động Playwright để render Showcase Poster...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 1800}, device_scale_factor=2)
        await page.set_content(poster_html)
        await page.wait_for_timeout(1000)
        
        # Chụp toàn màn hình poster
        await page.screenshot(path=OUT_POSTER, full_page=True)
        print(f"✅ Đã chụp thành công Showcase Poster: {OUT_POSTER}")
        
        print("📸 Bắt đầu render 1024px PNG cho tất cả 38 tài khoản (cả dark và solid)...")
        if not os.path.exists(OUT_SINGLE_DIR):
            os.makedirs(OUT_SINGLE_DIR)
            
        for acc in items:
            key = acc['id']
            spage = await browser.new_page(viewport={"width": 1024, "height": 1024}, device_scale_factor=1)
            
            # Dark
            html_dark = f'<!DOCTYPE html><html><head><style>svg{{width:1024px!important;height:1024px!important;}}</style></head><body style="margin: 0; padding: 0; background: transparent; display: flex; align-items: center; justify-content: center; width: 1024px; height: 1024px;"><div style="width: 1024px; height: 1024px;">{acc["svg_dark"]}</div></body></html>'
            await spage.set_content(html_dark)
            await spage.wait_for_timeout(50)
            await spage.screenshot(path=os.path.join(OUT_SINGLE_DIR, f"{key}_dark_1024.png"), omit_background=True)
            
            # Solid
            html_solid = f'<!DOCTYPE html><html><head><style>svg{{width:1024px!important;height:1024px!important;}}</style></head><body style="margin: 0; padding: 0; background: transparent; display: flex; align-items: center; justify-content: center; width: 1024px; height: 1024px;"><div style="width: 1024px; height: 1024px;">{acc["svg_solid"]}</div></body></html>'
            await spage.set_content(html_solid)
            await spage.wait_for_timeout(50)
            await spage.screenshot(path=os.path.join(OUT_SINGLE_DIR, f"{key}_solid_1024.png"), omit_background=True)
            
            await spage.close()
            print(f"  ✓ Rendered 1024px PNG: {key}")
            
        await browser.close()
    print("🎉 Hoàn tất render toàn bộ ảnh!")

if __name__ == '__main__':
    asyncio.run(main())
