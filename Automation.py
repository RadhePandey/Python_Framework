from playwright.sync_api import sync_playwright
with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://automationexercise.com/login")

    page.locator("//a[@href='/login']").click()
    page.locator("//input[@type='text']").fill("Radhe")
    page.locator("(//input[@placeholder='Email Address'])[2]").fill("radhepandey08@gmail.com")
    page.locator("(//button[@type='submit'])[2]").click()

    page.locator("//input[@id='id_gender1']").click()
    page.locator("//input[@type='password']").fill("Admin")
    page.locator("//input[@id='first_name']").fill("Radhe")
    page.locator("//input[@id='last_name']").fill("Pandey")
    page.locator("//input[@id='address1']").fill("Mayur Vihar-1")

    page.wait_for_timeout(5000)