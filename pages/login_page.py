from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-btn")

    def navigate(self):
        self.page.goto("https://app.workflowpro.com/login", wait_until="networkidle")

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_login_success(self):
        expect(self.page).to_have_url("https://app.workflowpro.com/dashboard", timeout=10000)
        expect(self.page.locator(".welcome-message")).to_be_visible()