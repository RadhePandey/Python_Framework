from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.tranktechnologies.com")

    verticals = page.locator('(//a[text()="Verticals"])[1]')

    #menu options
    trading_CTA = page.locator('(//a[@href="#"])[3]')

    #submenu options
    stock_trading_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
    algo_trading_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
    paper_trading_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
    custom_trading_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
    cfd_trading_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1] ')
    web_portal_trading_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
    trading_app_development_trading_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')

    trading_options = [
        stock_trading_CTA,
        algo_trading_CTA,
        paper_trading_CTA,
        custom_trading_CTA,
        cfd_trading_CTA,
        web_portal_trading_CTA,
        trading_app_development_trading_CTA
    ]

    for i in trading_options:
        verticals.hover()
        trading_CTA.hover()
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()
    print("Trading done")

    #retail and e-commerce 
    retail_and_ecommerce_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
    ecommerce_website_development = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
    ecommerce_app_development = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

    retail_and_ecommerce_options = [
        ecommerce_website_development,
        ecommerce_app_development
    ]

    for i in retail_and_ecommerce_options:
        verticals.hover()
        retail_and_ecommerce_CTA.hover()
        i.click()
        page.wait_for_timeout(500)
        page.go_back()
    print("Retail and Ecommerce done")

    #healthcare
    healthcare_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/healthcare-mobile-app-development-company"])[1]')
    diet_and_nutritions_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
    health_tracking_app_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

    healthcare_options = [
        diet_and_nutritions_CTA,
        health_tracking_app_CTA
    ]

    for i in healthcare_options:
        verticals.hover()
        healthcare_CTA.hover()
        i.click()
        page.wait_for_timeout(500)
        page.go_back()
    print("healthcare done")


    #fintech
    fintech_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/fintech-mobile-app-development-company"])[1]')
    pos_software_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
    crypto_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

    fintech_options = [
        pos_software_development_CTA,
        crypto_CTA
    ]

    for i in fintech_options:
        verticals.hover()
        fintech_CTA.hover()
        i.click()
        page.wait_for_timeout(500)
        page.go_back()
    print("Fintech done")

    #custom app
    custom_app_CTA = page.locator('//strong[text()="Custom App"]')
    desktop_app_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
    crm_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
    hrm_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
    erp_app_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
    travel_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
    e_learning_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
    dating_app_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
    #real_estate_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company-in-india"])[1]')

    custom_app_options = [
        desktop_app_development_CTA,
        crm_development_CTA,
        hrm_development_CTA,
        erp_app_development_CTA,
        travel_CTA,
        e_learning_CTA,
        dating_app_development_CTA,
        #real_estate_CTA
    ]

    for i in custom_app_options:
        verticals.hover()
        custom_app_CTA.hover()
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()
    print("Custom App done")

    #technologies

    technologies_CTA = page.locator('(//a[text()="Technologies"])[1]')

    #menu
 #   ecommerce_development_CTA = page.get_by_text('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[3]')
    ecommerce_development_CTA = page.locator("//strong[normalize-space()='eCommerce Development']")
    #submenu
    magento_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
    opencart_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
    codeigniter_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
    wordpress_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
    big_commerce_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
    shopify_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
    cs_cart_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
    node_js_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
    nop_commerce_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
    woo_commerce_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
    laravel_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
    prestashop_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
    drupal_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
    wix_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
    joomla_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
    react_js_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
    express_js_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')

    ecommerce_development_options = [
        magento_development_CTA,
        opencart_development_CTA,
        codeigniter_development_CTA,
        wordpress_development_CTA,
        big_commerce_development_CTA,
        shopify_development_CTA,
        cs_cart_development_CTA,
        node_js_development_CTA,
        nop_commerce_CTA,
        woo_commerce_CTA,
        laravel_development_CTA,
        prestashop_development_CTA,
        drupal_development_CTA,
        wix_development_CTA,
        joomla_development_CTA,
        react_js_development_CTA,
        express_js_development_CTA
    ]

    for i in ecommerce_development_options:
        technologies_CTA.hover()
        ecommerce_development_CTA.hover()
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()
    print("Ecommerce development done under technologies")


    mobile_app_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/mobile-app-development-company"])[1]')
    
    #submenu
    react_native_Mobile_app_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
    enterprise_mobile_app_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
    xamarin_mobile_app_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
    kotlin_mobile_app_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
    flutter_mobile_app_CTa = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
    iconic_mobile_app_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
    swift_app_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
    appointment_booking_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

    mobile_app_development_options = [
        react_native_Mobile_app_CTA,
        enterprise_mobile_app_CTA,
        xamarin_mobile_app_CTA,
        kotlin_mobile_app_CTA,
        flutter_mobile_app_CTa,
        iconic_mobile_app_CTA,
        swift_app_CTA,
        appointment_booking_CTA
    ]

    for i in mobile_app_development_options:
        technologies_CTA.hover()
        mobile_app_development_CTA.hover()
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()
    print("Mobile app development")

    artificial_intelligence_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/artificial-intelligence-development-services-company-india"])[1]')

    artificial_intelligence_options = [artificial_intelligence_CTA]
    #here i created list just in case if we add any technologies inside this menu then we don't need to create list

    for i in artificial_intelligence_options:
        technologies_CTA.hover()
        artificial_intelligence_CTA.hover()
        i.click()
        page.wait_for_timeout(500)
        page.go_back()
    print("AI done")

#---------------------------------------------------------
    #now writing code for Blog CTA 

    blog_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')

    #submenu

    app_development_CTA = page.locator('//a[@href="/blog/category/app-development/"]')
    web_development_CTA = page.locator('//a[@href="/blog/category/web-development/"]')
    software_development_CTA = page.locator('//a[@href="/blog/category/web-development/"]')
    digital_marketing_CTA = page.locator('//a[@href="/blog/category/digital-marketing/"]')
    email_marketing_CTA = page.locator('//a[@href="/blog/category/email-marketing/"]')
    artificial_intelligence_blog_CTA = page.locator('//a[@href="/blog/category/artificial-intelligence/"]')
    ui_ux_design_CTA = page.locator('//a[@href="/blog/category/ui-ux-design/"]')


    blog_options = [
        app_development_CTA,
        web_development_CTA,
        software_development_CTA,
        digital_marketing_CTA,
        email_marketing_CTA,
        artificial_intelligence_blog_CTA,
        ui_ux_design_CTA
    ]

    for i in blog_options:
        blog_CTA.click()
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()


