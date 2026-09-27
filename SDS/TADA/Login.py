from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://test.rajyasabha.digital/mpa/login?login=email")
    print("URL launch")

    #page.locator("//input[@fdprocessedid='c94t2d']").fill("surbhi@gmail.com")
    page.locator("//input[@type='text']").fill("surbhi@gmail.com")
    print("Email entered")
    page.locator("//button[text()=' Send OTP ']").click()
    page.wait_for_timeout(1000)

    # page.locator("//input[@placeholder='Enter registered mobile/email number']").fill("surbhi@gmail.com")

    page.locator("(//input[@type='text'])[1]").fill("1")
    page.locator("(//input[@type='text'])[2]").fill("2")
    page.locator("(//input[@type='text'])[3]").fill("3")
    page.locator("(//input[@type='text'])[4]").fill("4")
    page.locator("(//input[@type='text'])[5]").fill("5")
    page.locator("(//input[@type='text'])[6]").fill("6")

    page.locator("//button[text()=' Verify OTP ']").click()
    title = page.title()
    print(title)
    page.wait_for_timeout(1000)
    page.locator("your_hamburger_locator").hover()
    page.locator("(//div[@class='text-box flex-grow'])[3]").click()
    page.wait_for_timeout(1000)
    page.locator("(//div[@class='h-full flex flex-col items-center justify-center'])[1]").click()
    page.wait_for_timeout(1000)

    # page.locator("(//div[@class='flex flex-col items-center text-center'])[1]").set_input_files(r"C:\Users\Radhe\OneDrive\Desktop\Test_Data_Upload\Test_Data1.jpeg")
    
    # page.locator("input[type='file']").set_input_files(
    # r"C:\Users\Radhe\OneDrive\Desktop\Test_Data_Upload\Test_Data1.jpeg")
    # page.wait_for_timeout(5000)
    # browser.close()