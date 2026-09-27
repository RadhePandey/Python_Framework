from config import Base_URL


class technology:

    def __init__(self, page):

        self.page = page
        # TECHNOLOGIES

        self.technologies_CTA = page.locator('(//a[text()="Technologies"])[1]')

        # E-COMMERCE DEVELOPMENT


        self.ecommerce_development_CTA = page.locator("//strong[normalize-space()='eCommerce Development']")

        # Submenu options
        self.magento_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')

        self.opencart_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')

        self.codeigniter_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')

        self.wordpress_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')

        self.big_commerce_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')

        self.shopify_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')

        self.cs_cart_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')

        self.node_js_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')

        self.nop_commerce_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')

        self.woo_commerce_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')

        self.laravel_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')

        self.prestashop_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')

        self.drupal_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')

        self.wix_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')

        self.joomla_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')

        self.react_js_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')

        self.express_js_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')

        self.ecommerce_development_options = [
            self.magento_development_CTA,
            self.opencart_development_CTA,
            self.codeigniter_development_CTA,
            self.wordpress_development_CTA,
            self.big_commerce_development_CTA,
            self.shopify_development_CTA,
            self.cs_cart_development_CTA,
            self.node_js_development_CTA,
            self.nop_commerce_CTA,
            self.woo_commerce_CTA,
            self.laravel_development_CTA,
            self.prestashop_development_CTA,
            self.drupal_development_CTA,
            self.wix_development_CTA,
            self.joomla_development_CTA,
            self.react_js_development_CTA,
            self.express_js_development_CTA
        ]

        # MOBILE APP DEVELOPMENT

        self.mobile_app_development_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/mobile-app-development-company"])[1]')

        # Submenu options
        self.react_native_Mobile_app_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')

        self.enterprise_mobile_app_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')

        self.xamarin_mobile_app_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')

        self.kotlin_mobile_app_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')

        self.flutter_mobile_app_CTa = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')

        self.iconic_mobile_app_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')

        self.swift_app_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')

        self.appointment_booking_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

        self.mobile_app_development_options = [
            self.react_native_Mobile_app_CTA,
            self.enterprise_mobile_app_CTA,
            self.xamarin_mobile_app_CTA,
            self.kotlin_mobile_app_CTA,
            self.flutter_mobile_app_CTa,
            self.iconic_mobile_app_CTA,
            self.swift_app_CTA,
            self.appointment_booking_CTA
        ]

        # ARTIFICIAL INTELLIGENCE
      
        self.artificial_intelligence_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/artificial-intelligence-development-services-company-india"])[1]')

        # Created as a list so additional AI options
        # can be added later without changing navigation logic
        self.artificial_intelligence_options = [
            self.artificial_intelligence_CTA
        ]

    # E-COMMERCE DEVELOPMENT NAVIGATION
   

    def ecommerce_development_navigation(self):

        for i in self.ecommerce_development_options:
            self.page.goto(Base_URL)
            self.technologies_CTA.hover()
            self.ecommerce_development_CTA.hover()

            i.click()

            self.page.wait_for_load_state("load")

            self.page.go_back()

        print("Ecommerce development done under technologies")

    # MOBILE APP DEVELOPMENT NAVIGATION

    def mobile_app_development_navigation(self):

        for i in self.mobile_app_development_options:
            self.page.goto(Base_URL)
            self.technologies_CTA.hover()
            self.mobile_app_development_CTA.hover()

            i.click()

            self.page.wait_for_load_state("load")

            self.page.go_back()

        print("Mobile app development done")

    # ARTIFICIAL INTELLIGENCE NAVIGATION

    def artificial_intelligence_navigation(self):

        for i in self.artificial_intelligence_options:
            self.page.goto(Base_URL)
            self.technologies_CTA.hover()
            self.artificial_intelligence_CTA.hover()

            i.click()

            self.page.wait_for_load_state("load")

            self.page.go_back()

        print("AI done")