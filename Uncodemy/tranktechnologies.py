from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://uncodemy.com/")

    # Categories
    categories_btn = page.locator("//span[@id='categoriesBtn']")

    # Full Stack Development
    full_stack_development_CTA = page.locator("//a[text()='Full-Stack-Development']")

    nodejs_full_stack_CTA = page.locator('(//a[@href="/course/full-stack-with-nodejs-training-course-in-noida"])[1]')
    python_full_stack_CTA = page.locator('(//a[@href="/course/python-full-stack-training-course-in-noida"])[1]')
    java_full_stack_react_CTA = page.locator('(//a[@href="/course/java-full-stack-using-react-training-course-in-noida"])[1]')
    web_designing_CTA = page.locator('(//a[@href="/course/web-designing-training-course-in-noida"])[1]')
    web_development_CTA = page.locator('(//a[@href="/course/web-development-training-course-in-noida"])[1]')
    frontend_full_stack_CTA = page.locator('(//a[@href="/course/frontend-development-training-course-in-noida"])[1]')
    angular_full_stack_CTA = page.locator('(//a[@href= "/course/angular-training-course-in-noida"])[1]')
    react_full_stack_CTA = page.locator('(//a[@href="/course/react-js-training-course-in-noida"])[1]')
    dsa_full_stack_CTA = page.locator('(//a[@href="/course/data-structure-and-algorithm-training-course-in-noida"])[1]')
    mean_full_stack_CTA = page.locator('(//a[@href="/course/mean-stack-development-training-course-in-noida"])[1]')
    mern_full_stack_CTA = page.locator('(//a[@href="/course/mern-stack-development-training-course-in-noida"])[1]')

    full_stack_development_options = [
        nodejs_full_stack_CTA,
        python_full_stack_CTA,
        java_full_stack_react_CTA,
        web_designing_CTA,
        web_development_CTA,
        frontend_full_stack_CTA,
        angular_full_stack_CTA,
        react_full_stack_CTA,
        dsa_full_stack_CTA,
        mean_full_stack_CTA,
        mern_full_stack_CTA
    ]

    for i in full_stack_development_options:
        categories_btn.hover()
        page.wait_for_timeout(500)
        full_stack_development_CTA.hover()
        page.wait_for_timeout(500)
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()
    print("full_stack_development done")

    # Data Science
    data_science_CTA = page.locator("//a[text()='Data Science']")

    python_training_CTA = page.locator('(//a[@href="/course/python-training-course-in-noida"])[1]')
    data_analytics_python_CTA = page.locator('(//a[@href="/course/data-analytics-using-python-training-course-in-noida"])[1]')
    data_science_ml_python_CTA = page.locator('(//a[@href="/course/data-science-machine-learning-using-python-training-course-in-noida"])[1]')
    machine_learning_python_CTA = page.locator('(//a[@href="/course/machine-learning-using-python-training-course-in-noida"])[1]')
    ai_python_python_CTA = page.locator('(//a[@href="/course/ai-using-python-training-course-in-noida"])[1]')

    data_science_options = [
        python_training_CTA,
        data_analytics_python_CTA,
        data_science_ml_python_CTA,
        machine_learning_python_CTA,
        ai_python_python_CTA

    ]

    for i in data_science_options:
        categories_btn.hover()
        data_science_CTA.hover()
        page.wait_for_timeout(500)
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()
    print("data_science done")

#working fine till here

    # Software Testing
    software_testing_CTA = page.locator("(//a[text()='Software Testing'])[1]")
    print("Software Testing clicked")

    software_testing_course_CTA = page.locator('(//a[@href="/course/software-testing-training-course-in-noida"])[1]')
    print("Software Testing course")
    automation_testing_course_CTA = page.locator('(//a[@href="/course/automation-testing-course-in-noida"])[1]')
    print("Automation Testing clicked")
    playwright_course_CTA = page.locator('(//a[@href="/course/playwright-training-course-in-noida"])[1]')
    print("Playwright testing clicked")
    manual_testing_course_CTA = page.locator('(//a[@href="/course/manual-testing-course-in-noida"])[1]')
    print("Manual Testing clicked")
    istbq_course_CTA = page.locator('(//a[@href="/course/istqb-training-course-in-noida"])[1]')
    print("ISTBQ Testing clicked")
    manualselenium_course_CTA = page.locator('(//a[@href="/course/manual-testing-course-in-noida"])[2]')
    print("Manual with Selenium Testing clicked")

    software_testing_options = [
        software_testing_course_CTA,
        automation_testing_course_CTA,
        manual_testing_course_CTA,
        playwright_course_CTA,
        istbq_course_CTA,
        manualselenium_course_CTA
    ]

    for i in software_testing_options:
        categories_btn.hover()
        page.wait_for_timeout(500)
        software_testing_CTA.hover()
        page.wait_for_timeout(500)
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()
    print("software testing done")




    # Cloud Tools
    cloud_tools_CTA = page.locator("(//a[text()='Cloud Tools'])[1]")

    azure_course_CTA = page.locator('(//a[@href="/course/microsoft-azure-training-course-in-noida"])[1]')
    devops_course_CTA = page.locator('(//a[@href="/course/devops-training-course-in-noida"])[1]')

    cloud_tools_options = [ azure_course_CTA ,
                           devops_course_CTA

    ]

    for i in cloud_tools_options:
        categories_btn.hover()
        page.wait_for_timeout(500)
        cloud_tools_CTA.hover()
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()
    print("Cloud tools done")

    # Digital Marketing
    digital_marketing_CTA = page.locator("(//a[text()='Digital Marketing'])[1]")


    digital_marketing_footer_CTA = page.locator("(//a[text()='Digital Marketing'])[2]")
    advcance_digital_marketing_CTA = page.locator('(//a[@href="/course/advance-digital-marketing-training-course-in-noida"])[1]')
    seo_training_CTA = page.locator('(//a[@href="/course/seo-training-course-in-noida"])[1]')

    digital_marketing_options = [ digital_marketing_footer_CTA,
                                 advcance_digital_marketing_CTA,
                                 seo_training_CTA

    ]

    for i in digital_marketing_options:
        categories_btn.hover()
        page.wait_for_timeout(500)
        digital_marketing_CTA.hover()
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()
    print("Digital Marketing Done")

    java_technology_CTA = page.locator('(//a[text()="Java Technology+"])[1]')

    java_course_CTA = page.locator('(//a[@href="/course/java-training-course-in-noida"])[1]')
    java_for_beginners_CTA = page.locator("//a[text()='Java For Beginners']")
    java_expert_CTA = page.locator('(//a[@href="/course/java-expert-training-course-in-noida"])[1]')
    spring_boot_CTA = page.locator('(//a[@href="/course/spring-boot-microservices-security-with-hibernate-training-course-in-noida"])[1]')

    java_technology_options = [java_course_CTA,
                               java_for_beginners_CTA,
                               java_expert_CTA,
                               spring_boot_CTA]

    for i in java_technology_options:
        categories_btn.hover()
        page.wait_for_timeout(500)
        java_technology_CTA.hover()
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()
    print("Java Technology Done")


    network_security_CTA = page.locator("//a[text()='Network & Security']")

    ethical_hacking_CTA = page.locator('(//a[@href="/course/ethical-hacking-course-in-noida"])[1]')
    cyber_security_CTA = page.locator('(//a[@href="/course/cyber-security-training-course-in-noida"])[1]')
    ccnp_CTA = page.locator('(//a[@href="/course/ccnp-training-course-in-noida"])[1]')
    mcsa_CTA = page.locator('(//a[@href="/course/mcsa-training-course-in-noida"])[1]')
    vmware_CTA = page.locator('(//a[@href="/course/vmware-training-course-in-noida"])[1]')

    network_security_options = [ethical_hacking_CTA,
                                cyber_security_CTA,
                                ccnp_CTA,
                                mcsa_CTA,
                                vmware_CTA
    ]

    for i in network_security_options:
        categories_btn.hover()
        page.wait_for_timeout(500)
        network_security_CTA.hover()
        page.wait_for_timeout(500)
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()
    print("Network Security Done")


    programming_language_CTA = page.locator('//a[text()="Programming Language"]')

    data_structure_algorithm_CTA = page.locator('(//a[@href="/course/c-with-data-structure-and-algorithm-training-course-in-noida"])[1]')
    oods_algorithum_training_CTA = page.locator('(//a[@href="/course/cpptraining-training-course-in-noida"])[1]')
    dot_net_CTA = page.locator('(//a[@href="/course/net-4-months-training-course-in-noida"])[1]')
    dot_net_fullstack_CTA = page.locator('(//a[@href="/course/dotnet-full-stack-training-course-in-noida"])[1]')
    r_programming_CTA = page.locator('(//a[@href="/course/r-programming-training-course-in-noida"])[1]')

    programming_language_options = [data_structure_algorithm_CTA,
                                    oods_algorithum_training_CTA,
                                    dot_net_CTA,
                                    dot_net_fullstack_CTA,
                                    r_programming_CTA
    ]

    for i in programming_language_options:
        categories_btn.hover()
        page.wait_for_timeout(500)
        programming_language_CTA.hover()
        page.wait_for_timeout(500)
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()
    print("Programming language done")


    cad_training_CTA = page.locator('//a[text()="CAD Training"]')

    autocad_training_CTA = page.locator('(//a[@href="/course/autocad-training-course-in-noida"])[1]')
    cnc_programming_CTA = page.locator('(//a[@href="/course/cnc-programming-training-course-in-noida"])[1]')

    cad_training_options = [autocad_training_CTA,
                            cnc_programming_CTA
    ]

    for i in cad_training_options:
        categories_btn.hover()
        page.wait_for_timeout(500)
        cad_training_CTA.hover()
        page.wait_for_timeout(500)
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()
    print("CAD Done")


    graphic_design_CTA = page.locator('(//a[text()="Graphic Designing"])[1]')

    graphic_designing_CTA = page.locator('(//a[@href="/course/graphic-designing-training-course-in-noida"])[1]')
    ui_ux_designing_CTA = page.locator('(//a[@href="/course/uiux-training-course-in-noida"])[1]')

    graphic_design_options = [
        graphic_designing_CTA,
        ui_ux_designing_CTA
    ]

    for i in graphic_design_options:
        categories_btn.hover()
        page.wait_for_timeout(500)
        graphic_design_CTA.hover()
        page.wait_for_timeout(500)
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()
    print("Graphic Design Done")
    # browser.close()