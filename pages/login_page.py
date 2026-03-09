from playwright.sync_api import sync_playwright

class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#email")
        self.password_input = page.locator("#pswrd")
        self.login_button = page.locator("button[type='submit']")
        self.environment_button = page.locator("xpath=//app-environment//h3")

    def navigate(self, url):
        self.page.goto(url)
        self.page.wait_for_load_state('networkidle')

    def enter_username(self, username):
        self.username_input.fill(username)

    def enter_password(self, password):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.wait_for(state='visible', timeout=10000)
        self.login_button.click()

    def get_environment_heading(self):
        self.environment_button.wait_for(state='visible', timeout=10000)
        text = self.environment_button.inner_text()
        return text

    def login(self, username, password):
        try:
            self.enter_username(username)
            self.enter_password(password)
            self.click_login()
            
            # Wait for dashboard URL to confirm navigation
            self.page.wait_for_url(lambda url: "dashboard" in url, timeout=30000)
            
            heading = self.get_environment_heading()
            return heading
        except Exception as e:
            print(f"Login failed: {e}")
            return None