import pytest
import os
from playwright.sync_api import sync_playwright

# This fixture allows you to switch between local and BrowserStack testing
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, pytestconfig):
    # You can extend this to include BrowserStack credentials from environment variables
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720}, # Default Desktop
    }

@pytest.fixture(scope="function")
def mobile_page():
    """Fixture to simulate a mobile device for Part 3 of the case study"""
    with sync_playwright() as p:
        # Simulate an iPhone 13 for BrowserStack/Mobile testing requirements
        device = p.devices['iPhone 13']
        browser = p.chromium.launch()
        context = browser.new_context(**device)
        page = context.new_page()
        yield page
        browser.close()