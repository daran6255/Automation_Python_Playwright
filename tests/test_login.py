import pytest
from playwright.sync_api import sync_playwright
import time
from pages.login_page import LoginPage

class TestLogin:
    """Test class for login functionality"""
    
    @pytest.fixture
    def browser_setup(self):
        """Setup browser for each test"""
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=False,
                args=[
                    '--disable-blink-features=AutomationControlled',
                    '--disable-web-resources',
                ]
            )
            
            context = browser.new_context(
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            )
            
            page = context.new_page()
            
            # Hide automation detection
            page.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => false,
                });
            """)
            
            yield page, browser
            
            browser.close()