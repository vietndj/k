import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        errors = []
        page.on("pageerror", lambda err: errors.append(err.message))
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        
        url = "https://fedu.vn/k/anh.html"
        print(f"Loading {url}...")
        
        # We will loop in case the CDN is cached or building
        max_retries = 3
        for i in range(max_retries):
            errors.clear()
            await page.goto(url)
            await page.wait_for_timeout(3000)
            
            # Check if it has the new header "THƯ VIỆN POSTER"
            header_text = await page.evaluate("() => { const h1 = document.querySelector('h1'); return h1 ? h1.innerText : ''; }")
            print(f"Attempt {i+1}: Header found: '{header_text}'")
            
            if "THƯ VIỆN POSTER" in header_text:
                print("Deploy successful! New UI detected.")
                break
            else:
                print("Still showing old UI or cache. Waiting 10 seconds before retry...")
                await page.wait_for_timeout(10000)
        
        # Capture screenshot
        await page.screenshot(path="nghiem_thu_online.jpg", full_page=False)
        print("Screenshot saved to nghiem_thu_online.jpg")
        
        if errors:
            print("JS Errors found:")
            for e in errors:
                print(" -", e)
        else:
            print("No JS errors detected.")
            
        await browser.close()
        
asyncio.run(main())
