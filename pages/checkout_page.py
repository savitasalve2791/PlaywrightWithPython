from playwright.sync_api import Locator, Page


class CheckoutPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.first_name = page.get_by_role("textbox", name="First Name")
        self.last_name = page.get_by_role("textbox", name="Last Name")
        self.postal_code = page.get_by_role("textbox", name="Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.finish_button = page.get_by_role("button", name="Finish")
        self.error_alert = page.get_by_role("alert")

    def fill_information(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_to_overview(self) -> None:
        self.continue_button.click()

    def error_message(self) -> Locator:
        return self.error_alert

    def finish_order(self) -> None:
        self.finish_button.click()
