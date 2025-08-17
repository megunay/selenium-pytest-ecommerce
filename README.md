# selenium-pytest-ecommerce
Automate login, product search, add-to-cart, and checkout flow for an e-commerce demo site.

# Selenium + Pytest E-commerce Automation

This project automates basic workflows on [saucedemo.com](https://www.saucedemo.com) using:
- Selenium
- Pytest
- Page Object Model
- pytest-html reports

## Features
- Login tests (valid & invalid)
- Product add-to-cart test
- Checkout flow (basic)

## Run Tests
```bash
pytest --html=reports/report.html --self-contained-html
