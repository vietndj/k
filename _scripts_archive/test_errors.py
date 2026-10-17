import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        page.on("console", lambda msg: print(f"Browser Console: {msg.text}"))
        page.on("pageerror", lambda err: print(f"Browser Error: {err.message}"))
        
        await page.goto("http://localhost:8000/anh.html")
        await page.wait_for_timeout(2000)
        
        print("Typing in search...")
        await page.fill('#searchInput', 'google flow')
        await page.wait_for_timeout(1000)
        
        await browser.close()
        
asyncio.run(main())
