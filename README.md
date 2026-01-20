# WorkFlow Pro - QA Automation Framework

## 🚀 Overview
This repository contains the automated test suite for WorkFlow Pro, a multi-tenant B2B SaaS platform. 
The framework is designed using **Python**, **Pytest**, and **Playwright**, with **BrowserStack** integration for mobile testing.

## 🛠️ Tech Stack
- **Language:** Python
- **Test Runner:** Pytest
- **Web Automation:** Playwright (Synchronous API)
- **API Testing:** Requests
- **Mobile Testing:** BrowserStack / Playwright

## 📂 Key Features
- **Page Object Model (POM):** For clean, maintainable code.
- **Tenant Isolation Testing:** Verifying security boundaries between Company1 and Company2.
- **Hybrid Integration:** Combining API data seeding with UI verification.

## 🏃 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Install Playwright browsers: `playwright install`
3. Run all tests: `pytest --html=reports/report.html`