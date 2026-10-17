from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    page = browser.new_page()
    
    # Bypass gatekeeper via local storage
    page.goto('file://' + os.path.abspath('index.html'))
    page.evaluate("localStorage.setItem('fedu_vault_auth_v1', '71ffe84afd528a0365d6ec95c89a64cd6979b4a15730649feddf2dc390db9e3c');")
    
    # Reload and collect console errors
    errors = []
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
    page.on("pageerror", lambda err: errors.append(str(err)))
    
    page.goto('file://' + os.path.abspath('index.html'), wait_until="networkidle")
    
    if errors:
        print("RUNTIME ERRORS FOUND:")
        for e in errors:
            print("-", e)
    else:
        print("No runtime errors.")
        
    page.screenshot(path="screenshot_real.png", full_page=True)
    browser.close()
