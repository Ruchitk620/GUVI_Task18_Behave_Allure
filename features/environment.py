"""Behave hooks: create and close one browser session per scenario."""

import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage


def before_scenario(context, scenario):
    options = Options()
    # Set HEADLESS=true in the environment to run without a visible browser.
    if os.getenv("HEADLESS", "false").lower() == "true":
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    context.driver = webdriver.Chrome(options=options)
    context.login_page = LoginPage(context.driver)
    context.base_url = os.getenv(
        "ZEN_PORTAL_URL",
        "https://v2.zenclass.in/login",
    )
    context.valid_username = os.getenv("ZEN_VALID_USERNAME")
    context.valid_password = os.getenv("ZEN_VALID_PASSWORD")


def after_scenario(context, scenario):
    driver = getattr(context, "driver", None)
    if driver:
        driver.quit()
