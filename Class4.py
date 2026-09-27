from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://automationexercise.com/")
    page.locator('//a[@href="/login"]').click()
    page.locator("(//input[@type='email'])[1]").fill("radhepandey08@gmail.com")
    page.locator("//input[@type='password']").fill("Admin")
    page.locator("(//button[@type='submit'])[1]").click()

    page.locator('//a[@href="/product_details/1"]').click()
    page.locator('//button[@type="button"]').click()
    page.locator('(//a[@href="/view_cart"])[2]').click()
    page.locator("//a[@class='btn btn-default check_out']").click()
    page.locator('//a[@href="/payment"]').click()
    page.locator("//input[@name='name_on_card']").fill("Radhe Pandey")
    page.locator("//input[@name='card_number']").fill("123456789123")
    page.locator("//input[@name='cvc']").fill("340")
    page.locator("//input[@name='expiry_month']").fill("02")
    page.locator("//input[@name='expiry_year']").fill("2027")
    page.locator("//button[@id='submit']").click()

    print("Congratulations! Your order has been confirmed!")
    page.locator('//a[@href="/logout"]').click()


    page.wait_for_timeout(5000)
