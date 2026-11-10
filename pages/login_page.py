
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    WebDriverException,
)


class LoginPage:

    # Login page locators
    EMAIL_INPUT = (
        By.CSS_SELECTOR,
        'input[placeholder="Enter your mail"]'
    )

    PASSWORD_INPUT = (
        By.CSS_SELECTOR,
        'input[placeholder="Enter your password "]'
    )

    SUBMIT_BUTTON = (
        By.XPATH,
        '//button[@type="submit"]'
    )

    # Dashboard profile menu
    PROFILE_MENU = (
        By.CSS_SELECTOR,
        '.avatar-main-div'
    )

    # Actual logout element
    LOGOUT_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "user-avatar-menu") and normalize-space(.)="Log out"]'
    )

    # Popup close locators
    CERTIFICATE_POPUP_CLOSE = (
        By.CSS_SELECTOR,
        'img[src*="commonPopupCloseIcon.svg"]'
    )

    REFERRAL_POPUP_CLOSE = (
        By.CSS_SELECTOR,
        'button.custom-close-button'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Open login page
    def open(self, url):
        self.driver.get(url)

    # Enter username
    def enter_username(self, username):
        email_field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        email_field.clear()
        email_field.send_keys(username)

    # Enter password
    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_field.clear()
        password_field.send_keys(password)

    # Click submit button
    def click_submit(self):
        submit_button = self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )
        submit_button.click()

    # Login
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()

    # Check dashboard
    def is_dashboard_displayed(self):
        try:
            self.wait.until(
                lambda driver: (
                    "login" not in driver.current_url.lower()
                    and "sign-in" not in driver.current_url.lower()
                )
            )
            return True
        except TimeoutException:
            return False

    # Check email input visibility
    def is_email_input_visible(self):
        try:
            email = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.EMAIL_INPUT)
            )
            return email.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    # Check password input visibility
    def is_password_input_visible(self):
        try:
            password = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.PASSWORD_INPUT)
            )
            return password.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    # Check both input boxes
    def is_input_boxes_visible(self):
        return (
            self.is_email_input_visible()
            and self.is_password_input_visible()
        )

    # Check submit button visibility and enabled state
    def is_submit_button_visible_and_enabled(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SUBMIT_BUTTON)
            )
            return button.is_displayed() and button.is_enabled()
        except (TimeoutException, NoSuchElementException):
            return False

    # Compatibility method for existing step definitions
    def is_submit_button_enabled(self):
        return self.is_submit_button_visible_and_enabled()

    # Check invalid login remains on login page
    def is_login_error_displayed(self):
        return (
            self.is_email_input_visible()
            and self.is_password_input_visible()
        )

    # Close an individual popup
    def close_one_popup(self, locator, popup_name):
        try:
            close_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(locator)
            )
            close_button.click()

            print(f"[POPUP] {popup_name} closed successfully.")

            time.sleep(1)
            return True

        except TimeoutException:
            print(f"[POPUP] {popup_name} not displayed.")
            return False

        except WebDriverException as error:
            print(f"[POPUP] Could not close {popup_name}: {error}")
            return False

    # Close both popups
    def close_popups_if_present(self):
        self.close_one_popup(
            self.CERTIFICATE_POPUP_CLOSE,
            "Certificate popup"
        )

        self.close_one_popup(
            self.REFERRAL_POPUP_CLOSE,
            "Referral popup"
        )

    # Logout
    def logout(self):
        try:
            print("[LOGOUT] Closing popups...")
            self.close_popups_if_present()

            print("[LOGOUT] Opening profile menu...")
            profile = self.wait.until(
                EC.element_to_be_clickable(self.PROFILE_MENU)
            )
            profile.click()

            print("[LOGOUT] Waiting for Log out element...")
            logout_element = self.wait.until(
                EC.element_to_be_clickable(self.LOGOUT_BUTTON)
            )

            print("[LOGOUT] Clicking Log out...")
            logout_element.click()

            print("[LOGOUT] Verifying login page...")
            self.wait.until(
                EC.visibility_of_element_located(self.EMAIL_INPUT)
            )

            print("[LOGOUT] Successfully logged out.")
            return True

        except (
            TimeoutException,
            NoSuchElementException,
            WebDriverException
        ) as error:
            raise AssertionError(f"Logout failed: {error}")
