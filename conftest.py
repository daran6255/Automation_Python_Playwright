from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=[
            '--disable-blink-features=AutomationControlled',
            '--disable-web-resources',
            '--no-default-browser-check',
        ]
    )
    
    context = browser.new_context(
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    )
    
    page = context.new_page()
        
    login_page = LoginPage(page)
    login_page.navigate("https://staging.onlygood.world./auth/login")
    result = login_page.login("dharanipathy.r@winvinaya.com", "Esg@1234")
    
    browser.close()