import pytest
from pages.login_page import LoginPage
from config.config import BASE_URL, LOGIN_USERNAME, LOGIN_PASSWORD

class TestLogin:
    """Refined Test class for login functionality"""

    def test_login_success(self, page_context):
        """Test successful login using session context from conftest"""
        login_page = LoginPage(page_context)
        
        print(f"DEBUG: Navigating to {BASE_URL}")
        login_page.navigate(BASE_URL)
        
        result = login_page.login(LOGIN_USERNAME, LOGIN_PASSWORD)
        
        assert result is not None, "Login failed - check logs for Encryption/SubtleCrypto errors"
        print(f"Login successful, environment heading: {result}")
