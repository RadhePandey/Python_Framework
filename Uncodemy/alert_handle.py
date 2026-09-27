from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demo.automationtesting.in/Alerts.html")
    page.once("dialog", lambda dialog: dialog.accept())
    page.locator('//button[@onclick="alertbox()"]').click()
    page.wait_for_timeout(2000)
    #alert open with Ok CTA

    #click on   Alert with Ok and Cancel CTA 
    page.locator('//a[@href="#CancelTab"]').click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator('//button[@onclick="confirmbox()"]').click()
    page.wait_for_timeout(2000)

    #click on Alert with Text 
    page.locator('//a[@href="#Textbox"]').click()
    page.once("dialog", lambda dialog: dialog.accept("Radhe"))
    page.locator('//button[@onclick="promptbox()"]').click()
    page.wait_for_timeout(5000)

