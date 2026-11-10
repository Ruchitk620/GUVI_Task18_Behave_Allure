"""Step definitions for GUVI Zen Portal Behave scenarios."""

from behave import given, when, then


@given("the user opens the GUVI Zen Portal login page")
def step_open_login_page(context):
    context.login_page.open(context.base_url)


@when("the user logs in with valid credentials")
def step_login_valid(context):
    assert context.valid_username and context.valid_password, (
        "Set ZEN_VALID_USERNAME and ZEN_VALID_PASSWORD environment variables."
    )
    context.login_page.login(context.valid_username, context.valid_password)


@when("the user logs in with invalid credentials")
def step_login_invalid(context):
    context.login_page.login(
        "invalid_user@example.com",
        "WrongPassword123",
    )


@then("the dashboard should be displayed")
def step_dashboard_displayed(context):
    assert context.login_page.is_dashboard_displayed(), (
        "Dashboard was not displayed after login."
    )


@then("the login error should be displayed")
def step_login_error_displayed(context):
    # The portal may show a toast or inline error. Verify the user remains
    # on the login route and the login form is still visible.
    assert "login" in context.driver.current_url.lower(), (
        "Invalid login unexpectedly navigated away from the login page."
    )
    assert context.login_page.is_email_input_visible()
    assert context.login_page.is_password_input_visible()


@then("the username and password input boxes should be visible")
def step_input_boxes_visible(context):
    assert context.login_page.is_email_input_visible(), (
        "Username/email input is not visible."
    )
    assert context.login_page.is_password_input_visible(), (
        "Password input is not visible."
    )


@then("the submit button should be visible and enabled")
def step_submit_button_visible(context):
    assert context.login_page.is_submit_button_visible_and_enabled(), (
        "Sign in button is not visible and enabled."
    )


@when("the user logs out")
def step_logout(context):
    context.login_page.logout()


@then("the login page should be displayed again")
def step_login_page_again(context):
    assert context.login_page.is_email_input_visible(), (
        "Login form did not return after logout."
    )
    assert context.login_page.is_password_input_visible(), (
        "Password input did not return after logout."
    )
