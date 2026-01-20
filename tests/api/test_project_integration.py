import pytest
from utils.api_client import APIClient
from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_project_creation_and_tenant_isolation(page):
    # 1. SETUP: API Data Seeding
    api = APIClient("https://api.workflowpro.com", "TEST_TOKEN_123")
    project_name = "Bynry_Automation_Project"
    
    # Create project for Company1
    response = api.create_project("Company1", project_name, "Integration Test Project")
    assert response.status_code == 201 
    project_id = response.json().get("id")

    # 2. VERIFY: Web UI display for Company1
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("admin@company1.com", "password123")
    
    # Verify the project appears (searching by the ID returned from API)
    project_locator = page.locator(f".project-card:has-text('{project_name}')")
    expect(project_locator).to_be_visible(timeout=10000)

    # 3. SECURITY: Tenant Isolation (Company2 should NOT see it)
    # Log out or clear cookies to switch tenants
    page.context.clear_cookies()
    login_page.navigate()
    login_page.login("user@company2.com", "password123")
    
    # Assert the project created by Company1 is hidden from Company2
    expect(page.locator(f".project-card:has-text('{project_name}')")).to_be_hidden()
