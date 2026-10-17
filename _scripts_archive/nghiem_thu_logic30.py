import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # Test 1: Desktop
        print("Testing Desktop...")
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await context.new_page()
        
        js_errors = []
        page.on("pageerror", lambda err: js_errors.append(err))
        
        response = await page.goto('https://fedu.vn/k/logic30.html', wait_until='networkidle')
        print(f"Status: {response.status}")
        
        if response.status != 200:
            print("Failed to load page!")
            await browser.close()
            return
            
        await page.screenshot(path='/Users/vietmac/.gemini/antigravity/brain/58267a6f-e34f-433e-a316-1939a01b12fe/vision_logic30_desktop.png', full_page=True)
        
        # Click on an item to verify instant jump
        print("Testing Instant Jump on Desktop...")
        await page.click('a[href="#p2_q3"]')
        await page.wait_for_timeout(500)
        await page.screenshot(path='/Users/vietmac/.gemini/antigravity/brain/58267a6f-e34f-433e-a316-1939a01b12fe/vision_instant_logic30.png')
        
        if js_errors:
            print("JS Errors found on desktop:")
            for err in js_errors:
                print(err)
        else:
            print("No JS errors on desktop!")
            
        await context.close()
        
        # Test 2: Mobile
        print("Testing Mobile...")
        mobile_context = await browser.new_context(
            viewport={"width": 390, "height": 844},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
        )
        mobile_page = await mobile_context.new_page()
        await mobile_page.goto('https://fedu.vn/k/logic30.html', wait_until='networkidle')
        await mobile_page.screenshot(path='/Users/vietmac/.gemini/antigravity/brain/58267a6f-e34f-433e-a316-1939a01b12fe/vision_logic30_mobile.png', full_page=True)
        await mobile_context.close()
        
        await browser.close()
        print("Testing completed!")

asyncio.run(main())
