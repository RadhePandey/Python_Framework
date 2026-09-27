from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

categories = page.locator("//span[@id='categoriesBtn']")

FullStackDevelopment= page.locator("//a[text()='Full-Stack-Development']")
#options inside FullStackDevelopment
FullStackWithNodeJS = page.locator('(//a[@href="/course/full-stack-with-nodejs-training-course-in-noida"])[1]')
PythonFullStack = page.locator('(//a[@href="/course/python-full-stack-training-course-in-noida"])[1]')
JavaFullStackWithReact = page.locator('(//a[@href="/course/java-full-stack-using-react-training-course-in-noida"])[1]')
WebDesigning = page.locator('(//a[@href="/course/web-designing-training-course-in-noida"])[1]')
WebDevelopment = page.locator('(//a[@href="/course/web-development-training-course-in-noida"])[1]')


DataScience = page.locator("//a[text()='Data Science']")
Python = page.locator('(//a[@href="/course/python-training-course-in-noida"])[1]')
DataAnalyticsPython = page.locator('(//a[@href="/course/data-analytics-using-python-training-course-in-noida"])[1]')
DataSciencePython = page.locator('(//a[@href="/course/data-science-machine-learning-using-python-training-course-in-noida"])[1]')
MachinePython = page.locator('(//a[@href="/course/machine-learning-using-python-training-course-in-noida"])[1]') 



SoftwareTesting = page.locator("(//a[text()='Software Testing'])[1]")
CloudTools = page.locator("(//a[text()='Cloud Tools'])[1]")
DigitalMarketing = page.locator("(//a[text()='Digital Marketing'])[1]")

