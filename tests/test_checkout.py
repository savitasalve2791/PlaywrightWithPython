import pytest
from playwright.sync_api import Page, expect

from pages import CheckoutPage


@pytest.mark.parametrize(
    ("first_name", "last_name", "postal_code", "message"),
    [
        ("", "Automation", "12345", "First Name is required"),
        ("Test", "", "12345", "Last Name is required"),
        ("Test", "Automation", "", "Postal Code is required"),
    ],
    ids=("missing-first-name", "missing-last-name", "missing-postal-code"),
)
def test_checkout_requires_all_information(
    checkout_page: CheckoutPage,
    first_name: str,
    last_name: str,
    postal_code: str,
    message: str,
) -> None:
    checkout_page.fill_information(first_name, last_name, postal_code)
    checkout_page.continue_to_overview()

    expect(checkout_page.error_message()).to_contain_text(message)


def test_checkout_completes_with_valid_information(
    checkout_page: CheckoutPage, page: Page
) -> None:
    # 1. Use synthetic test data and complete the SauceDemo test checkout.
    checkout_page.fill_information("Test", "Automation", "12345")
    checkout_page.continue_to_overview()
    expect(page.get_by_text("Checkout: Overview", exact=True)).to_be_visible()
    expect(page.get_by_text("Total: $32.39")).to_be_visible()

    checkout_page.finish_order()

    expect(page.get_by_text("Checkout: Complete!", exact=True)).to_be_visible()
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()
