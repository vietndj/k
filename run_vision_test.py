import asyncio
from playwright.async_api import async_playwright
import json

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # Desktop
        context_desktop = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page_desktop = await context_desktop.new_page()
        
        print("Navigating to Desktop URL...")
        await page_desktop.goto("https://fedu.vn/k/anh.html", wait_until='networkidle')
        await page_desktop.evaluate('() => document.fonts.ready')
        await page_desktop.wait_for_timeout(3000)
        
        await page_desktop.screenshot(path="vision_report_desktop.png", full_page=True)
        print("Desktop screenshot saved.")
        
        # Mobile
        context_mobile = await browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True)
        page_mobile = await context_mobile.new_page()
        
        print("Navigating to Mobile URL...")
        await page_mobile.goto("https://fedu.vn/k/anh.html", wait_until='networkidle')
        await page_mobile.evaluate('() => document.fonts.ready')
        await page_mobile.wait_for_timeout(3000)
        
        await page_mobile.screenshot(path="vision_report_mobile.png", full_page=True)
        print("Mobile screenshot saved.")
        
        await browser.close()

asyncio.run(run())
