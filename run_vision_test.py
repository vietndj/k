import asyncio
from playwright.async_api import async_playwright
import json

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # Desktop
        context_desktop = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page_desktop = await context_desktop.new_page()
        
        console_errors = []
        page_errors = []
        page_desktop.on('console', lambda msg: console_errors.append(f"{msg.type}: {msg.text}") if msg.type == 'error' else None)
        page_desktop.on('pageerror', lambda err: page_errors.append(f"{err.name}: {err.message}"))
        
        print("Navigating to Desktop URL...")
        await page_desktop.goto("https://fedu.vn/k/anh.html", wait_until='networkidle')
        await page_desktop.evaluate('() => document.fonts.ready')
        await page_desktop.wait_for_timeout(2000)
        
        if page_errors:
            print("❌ FATAL JS ERRORS DETECTED ON DESKTOP:")
            for err in page_errors:
                print(f"  {err}")
        
        dom_report = await page_desktop.evaluate('''() => {
            const checks = {};
            checks.consoleErrors = window.__capturedErrors || [];
            const targets = document.querySelectorAll('[data-qa], header, nav, footer, h1, h2, .logo, img, button, a.cta, .carousel-stack, .video-wrap, iframe, video');
            checks.elements = [...targets].map(el => {
                const rect = el.getBoundingClientRect();
                const style = getComputedStyle(el);
                return {
                    tag: el.tagName, id: el.id || el.dataset?.qa || '',
                    classes: el.className,
                    text: el.textContent?.slice(0, 80) || '',
                    src: el.src || el.getAttribute('src') || '',
                    visible: rect.width > 0 && rect.height > 0 
                             && style.display !== 'none' 
                             && style.visibility !== 'hidden'
                             && parseFloat(style.opacity) > 0,
                    rect: {x: Math.round(rect.x), y: Math.round(rect.y), w: Math.round(rect.width), h: Math.round(rect.height)}
                };
            });
            return checks;
        }''')
        
        with open("dom_probe_desktop.json", "w") as f:
            json.dump(dom_report, f, indent=2)
            
        await page_desktop.screenshot(path="vision_report_desktop.png", full_page=True)
        print("Desktop screenshot saved.")
        
        # Mobile
        context_mobile = await browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True)
        page_mobile = await context_mobile.new_page()
        
        page_mobile.on('console', lambda msg: console_errors.append(f"Mobile {msg.type}: {msg.text}") if msg.type == 'error' else None)
        page_mobile.on('pageerror', lambda err: page_errors.append(f"Mobile {err.name}: {err.message}"))
        
        print("Navigating to Mobile URL...")
        await page_mobile.goto("https://fedu.vn/k/anh.html", wait_until='networkidle')
        await page_mobile.evaluate('() => document.fonts.ready')
        await page_mobile.wait_for_timeout(2000)
        
        if page_errors:
            print("❌ FATAL JS ERRORS DETECTED ON MOBILE:")
            for err in page_errors:
                print(f"  {err}")
                
        dom_report_mobile = await page_mobile.evaluate('''() => {
            const checks = {};
            checks.consoleErrors = window.__capturedErrors || [];
            const targets = document.querySelectorAll('[data-qa], header, nav, footer, h1, h2, .logo, img, button, a.cta, .carousel-stack, .video-wrap, iframe, video');
            checks.elements = [...targets].map(el => {
                const rect = el.getBoundingClientRect();
                const style = getComputedStyle(el);
                return {
                    tag: el.tagName, id: el.id || el.dataset?.qa || '',
                    classes: el.className,
                    text: el.textContent?.slice(0, 80) || '',
                    src: el.src || el.getAttribute('src') || '',
                    visible: rect.width > 0 && rect.height > 0 
                             && style.display !== 'none' 
                             && style.visibility !== 'hidden'
                             && parseFloat(style.opacity) > 0,
                    rect: {x: Math.round(rect.x), y: Math.round(rect.y), w: Math.round(rect.width), h: Math.round(rect.height)}
                };
            });
            return checks;
        }''')
        
        with open("dom_probe_mobile.json", "w") as f:
            json.dump(dom_report_mobile, f, indent=2)
            
        await page_mobile.screenshot(path="vision_report_mobile.png", full_page=True)
        print("Mobile screenshot saved.")
        
        with open("js_errors.txt", "w") as f:
            f.write("\\n".join(page_errors))
            
        await browser.close()

asyncio.run(run())
