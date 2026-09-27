# from playwright.sync_api import sync_playwright
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()

#     page.goto("https://demo.automationtesting.in/Register.html")

#     page.locator("//input[@placeholder='First Name']").fill("Radhe")
#     page.locator("//input[@placeholder='Last Name']").fill("Pandey")
#     page.locator("//textarea[@rows='3']").fill("P67 Mayur Vihar 1 Delhi")
#     page.locator("//input[@type='email']").fill("radhepandey08@gmail.com")
#     page.locator("//input[@type='tel']").fill("9721707235")

#     page.locator("//input[@value='Male']").click()
#     page.locator("//input[@id='checkbox1']").click()

#     page.locator("//select[@id='Skills']").select_option("Android") #here we can select dropdown values
#     page.locator("//select[@id='yearbox']").select_option("1997")
#     page.locator("//select[@placeholder='Month']").select_option("July")
#     page.locator("//select[@placeholder='Day']").select_option("8")
#     page.wait_for_timeout(2000)

#     page.set_input_files('//input[@id="imagesrc"]',"D://PythonPlaywright//OrangeHRM_Screenshots//dashboard.png")
#     page.wait_for_timeout(4000)

    

#     page.locator('//div[@id="msdd"]').click()
#     english = page.locator('//a[text()="English"]')
#     estonian = page.locator('//a[text()="Estonian"]')
#     italian = page.locator('//a[text()="Italian"]')
#     polish = page.locator('//a[text()="Polish"]')

#     select_language = [english,estonian,polish,italian]
#     for i in select_language:
#         i.click()

#     page.locator('//label[text()="Skills"]').click()
#     page.locator('//span[@class="select2-selection select2-selection--single"]').click()
#     page.wait_for_timeout(1000)

#     page.locator('//input[@type="search"]').click()
#     page.locator('//input[@type="search"]').type("India")
#     page.locator('//input[@type="search"]').press("Enter")
#     page.wait_for_timeout(2000)

    

    

#     # page.wait_for_timeout(1000)

#     # #page.locator("//div[@id='msdd']").fill("English")

#     # page.locator("//input[@id='firstpassword']").fill("Admin")
#     # page.locator("//input[@id='secondpassword']").fill("Admin")

#     # #page.locator("//button[@id='submitbtn']").click()

#     # page.wait_for_timeout(5000)

#     # print("Registration Done")



from pathlib import Path
from playwright.sync_api import sync_playwright

download_folder = Path(__file__).parent / "downloads"
download_folder.mkdir(exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False)
    page = browser.new_page(accept_downloads=True)

    page.goto("https://demo.automationtesting.in/FileDownload.html#google_vignette")

    with page.expect_download() as download_info:
        page.locator("a[href*='samplefile.pdf']").click()

    download = download_info.value
    file_path = download_folder / download.suggested_filename
    download.save_as(file_path)

    print(f"Downloaded file: {file_path}")

    browser.close()