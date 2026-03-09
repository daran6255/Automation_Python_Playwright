import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from config.config import BASE_URL, LOGIN_USERNAME, LOGIN_PASSWORD

@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                '--disable-blink-features=AutomationControlled',
            ]
        )
        yield browser
        browser.close()

@pytest.fixture
def page_context(browser_instance):
    context = browser_instance.new_context(
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        viewport={'width': 1920, 'height': 1080},
        ignore_https_errors=True
    )
    
    # Crucial for hiding automation from some bots
    context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => false})")
    
    page = context.new_page()
    yield page
    context.close()