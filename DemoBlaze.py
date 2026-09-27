from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.demoblaze.com/index.html")

    page.locator("//a[@id='login2']").click()

    page.locator("//input[@id='loginusername']").fill("radhepandey08@gmail.com")
    page.locator("//input[@id='loginpassword']").fill("Admin")

    page.locator("//button[@onclick='logIn()']").click()

    page.locator('(//a[@href="prod.html?idp_=1"])[2]').click()

    page.once("dialog", lambda dialog: dialog.accept())
    page.wait_for_timeout(1000)
    page.locator('//a[@onclick="addToCart(1)"]').click()

    page.locator('//a[@href="cart.html"]').click()

    #page.locator('(//a[@href="#"])[9]').click()
    #page.wait_for_timeout(2000)
    # page.locator('(//a[@href="#"])[10]').click()
    # page.wait_for_timeout(1000)

     #doubts : 
        #If i use on click for xpath for delete CTA - getting error because of i think ' & "" both available in xpath --- 
        #how can i delete complete products except one left in card

    page.locator('//button[text()="Place Order"]').click()

    #Billing address form open 

    page.locator('//input[@id="name"]').fill("Radhe Pandey")
    page.locator('//input[@id="country"]').fill("India")
    page.locator('//input[@id="city"]').fill("Noida")
    page.locator('//input[@id="card"]').fill("1234 5678 9213")
    page.locator('//input[@id="month"]').fill("June")
    page.locator('//input[@id="year"]').fill('2028')
    page.wait_for_timeout(2000)

    page.locator('//button[@onclick="purchaseOrder()"]').click()
    page.wait_for_timeout(6000)
