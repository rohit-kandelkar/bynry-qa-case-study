import pytest
from pages.login_page import LoginPage

def test_user_login_flow(page):
    login_page = LoginPage(page)
    
    # 1. Navigate to site
    login_page.navigate()
    
    # 2. Perform login
    # In a real scenario, these would come from your 'data/' folder
    login_page.login("admin@company1.com", "password123")
    
    # 3. Verify success (Fixes the flakiness mentioned in Part 1)
    login_page.verify_login_success()