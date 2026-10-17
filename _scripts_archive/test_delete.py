import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        filepath = 'file:///Users/vietmac/Documents/CODE/k/logic29.html'
        await page.goto(filepath)
        
        # Take screenshot before
        await page.screenshot(path="screenshot_before.png")
        
        # Click the first delete button
        await page.click('.delete-btn')
        
        # Wait a bit for JS to hide and fetch to complete
        await page.wait_for_timeout(1000)
        
        # Take screenshot after
        await page.screenshot(path="screenshot_after.png")
        
        await browser.close()
        
        # Verify file content
        with open('/Users/vietmac/Documents/CODE/k/logic29.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'id="q1"' not in content:
            print("Hard delete successful: q1 is removed from logic29.html")
        else:
            print("Hard delete failed: q1 is still in logic29.html")

asyncio.run(run())
