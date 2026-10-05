import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page = await context.new_page()
        
        await page.goto("https://vietndj.github.io/k/anh.html", wait_until='networkidle')
        await page.wait_for_timeout(3000)
        
        first_img_src = await page.evaluate("() => document.querySelector('.card img').src")
        print(f"FIRST IMAGE SRC: {first_img_src}")
        
        await browser.close()

asyncio.run(main())
