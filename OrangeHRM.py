from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator("//input[@name='username']").fill("Admin")
    page.locator("//input[@type='password']").fill("admin123")
    # page.wait_for_timeout(100)
    page.screenshot(path="D://PythonPlaywright//OrangeHRM_Screenshots//loginpage-2.png")
    page.locator("//button[@type='submit']").click()
    page.wait_for_timeout(2000)
    page.screenshot(path="D://PythonPlaywright//OrangeHRM_Screenshots//dashboard.png")
    page.wait_for_timeout(1000)
    page.go_back()
    page.wait_for_timeout(1000)
    page.go_forward()
    page.wait_for_timeout(1000)
    page.reload()

    page.wait_for_timeout(1000)
    print("Done")