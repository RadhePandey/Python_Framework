from config import Base_URL

class vertical:

    def __init__(self, page):

        self.page = page
        # VERTICALS
        self.ver = page.locator('(//a[text()="Verticals"])[1]')

        # TRADING
        self.trading_CTA = page.locator('(//a[@href="#"])[3]')

        # Submenu options
        self.stock_trading_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.algo_trading_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.paper_trading_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.custom_trading_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.cfd_trading_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.web_portal_trading_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.trading_app_development_trading_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')

        self.trading_options = [
            self.stock_trading_CTA,
            self.algo_trading_CTA,
            self.paper_trading_CTA,
            self.custom_trading_CTA,
            self.cfd_trading_CTA,
            self.web_portal_trading_CTA,
            self.trading_app_development_trading_CTA
        ]


       # RETAIL AND E-COMMERCE

        self.retail_and_ecommerce_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.ecommerce_website_development = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.ecommerce_app_development = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

        self.retail_and_ecommerce_options = [
            self.ecommerce_website_development,
            self.ecommerce_app_development
        ]

# HEALTHCARE

        self.healthcare_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/healthcare-mobile-app-development-company"])[1]')
        self.diet_and_nutritions_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.health_tracking_app_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        self.healthcare_options = [
            self.diet_and_nutritions_CTA,
            self.health_tracking_app_CTA
        ]


        # FINTECH

        self.fintech_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/fintech-mobile-app-development-company"])[1]')
        self.pos_software_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

        self.fintech_options = [
            self.pos_software_development_CTA,
            self.crypto_CTA
        ]

        # CUSTOM APP

        self.custom_app_CTA = page.locator('//strong[text()="Custom App"]')
        self.desktop_app_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.crm_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.hrm_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.erp_app_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.travel_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.e_learning_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.dating_app_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')

        self.custom_app_options = [
            self.desktop_app_development_CTA,
            self.crm_development_CTA,
            self.hrm_development_CTA,
            self.erp_app_development_CTA,
            self.travel_CTA,
            self.e_learning_CTA,
            self.dating_app_development_CTA
        ]


   # TRADING NAVIGATION

    def trading_navigation(self):

        for i in self.trading_options:
            
            self.page.goto(Base_URL)
            self.ver.hover()
            self.trading_CTA.hover()

            i.click()

            self.page.wait_for_load_state("load")

            self.page.go_back()

        print("Trading done")


    # RETAIL AND E-COMMERCE NAVIGATION

    def retail_and_ecommerce_navigation(self):

        for i in self.retail_and_ecommerce_options:
            self.page.goto(Base_URL)
            self.ver.hover()
            self.retail_and_ecommerce_CTA.hover()

            i.click()

            self.page.wait_for_load_state("load")

            self.page.go_back()

        print("Retail and Ecommerce done")


    # HEALTHCARE NAVIGATION

    def healthcare_navigation(self):

        for i in self.healthcare_options:
            self.page.goto(Base_URL)
            self.ver.hover()
            self.healthcare_CTA.hover()

            i.click()

            self.page.wait_for_load_state("load")

            self.page.go_back()

        print("Healthcare done")


    # FINTECH NAVIGATION

    def fintech_navigation(self):

        for i in self.fintech_options:
            self.page.goto(Base_URL)
            self.ver.hover()
            self.fintech_CTA.hover()

            i.click()

            self.page.wait_for_load_state("load")

            self.page.go_back()

        print("Fintech done")


    # CUSTOM APP NAVIGATION

    def custom_app_navigation(self):

        for i in self.custom_app_options:
            self.page.goto(Base_URL)
            self.ver.hover()
            self.custom_app_CTA.hover()

            i.click()

            self.page.wait_for_load_state("load")

            self.page.go_back()

        print("Custom App done")