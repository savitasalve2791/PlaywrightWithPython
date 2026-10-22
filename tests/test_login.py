import re

import pytest
from playwright.sync_api import Page, expect

from pages import LoginPage


def test_valid_login_opens_inventory(login_page: LoginPage, page: Page) -> None:
    # 1. Sign in with the documented SauceDemo standard test account.
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(re.compile(r".*/inventory\.html$"))
    expect(page.get_by_text("Products", exact=True)).to_be_visible()


@pytest.mark.parametrize(
    ("username", "password", "message"),
    [
        ("invalid_user", "secret_sauce", "Username and password do not match"),
        ("standard_user", "invalid_password", "Username and password do not match"),
        ("", "", "Username is required"),
    ],
    ids=("invalid-username", "invalid-password", "empty-credentials"),
)
def test_login_rejects_invalid_or_empty_credentials(
    login_page: LoginPage,
    username: str,
    password: str,
    message: str,
) -> None:
    login_page.open()
    login_page.login(username, password)

    expect(login_page.error_message()).to_contain_text(message)


def test_login_rejects_locked_out_user(login_page: LoginPage) -> None:
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    expect(login_page.error_message()).to_contain_text("user has been locked out")
