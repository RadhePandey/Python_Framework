class blog:

    def __init__(self, page):

        self.page = page

        # BLOG

        self.blog_CTA = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')

        # BLOG SUBMENU OPTIONS

        self.app_development_CTA = page.locator('//a[@href="/blog/category/app-development/"]')

        self.web_development_CTA = page.locator('//a[@href="/blog/category/web-development/"]')

        self.software_development_CTA = page.locator('//a[@href="/blog/category/web-development/"]')

        self.digital_marketing_CTA = page.locator('//a[@href="/blog/category/digital-marketing/"]')

        self.email_marketing_CTA = page.locator('//a[@href="/blog/category/email-marketing/"]')

        self.artificial_intelligence_blog_CTA = page.locator('//a[@href="/blog/category/artificial-intelligence/"]')

        self.ui_ux_design_CTA = page.locator('//a[@href="/blog/category/ui-ux-design/"]')


        # BLOG OPTIONS LIST

        self.blog_options = [
            self.app_development_CTA,
            self.web_development_CTA,
            self.software_development_CTA,
            self.digital_marketing_CTA,
            self.email_marketing_CTA,
            self.artificial_intelligence_blog_CTA,
            self.ui_ux_design_CTA
        ]


    # BLOG NAVIGATION

    def blog_navigation(self):

        for i in self.blog_options:

            self.blog_CTA.click()

            i.click()

            self.page.wait_for_load_state("load")

            self.page.go_back()

        print("Blog navigation done")