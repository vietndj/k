from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    page = browser.new_page()
    page.set_viewport_size({"width": 1440, "height": 900})
    
    file_path = 'file://' + os.path.abspath('/Users/vietmac/Desktop/Bill_Ackman_Full_Tap_Ho_So.html')
    
    # Reload and collect console errors
    errors = []
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
    page.on("pageerror", lambda err: errors.append(str(err)))
    
    page.goto(file_path)
    # Bypass PIN
    page.evaluate("localStorage.setItem('fedu_vault_auth_v1', 'ok');")
    page.reload(wait_until="networkidle")
    
    if errors:
        print("RUNTIME ERRORS FOUND:")
        for e in errors:
            print("-", e)
    else:
        print("No runtime errors.")
        
    page.screenshot(path="screenshot_dual_column.png", full_page=True)
    browser.close()
    print("Screenshot saved to screenshot_dual_column.png")
