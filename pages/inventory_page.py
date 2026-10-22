import re

from playwright.sync_api import Locator, Page


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.heading = page.get_by_text("Products", exact=True)
        self.product_cards = page.locator(".inventory_item")
        self.cart_button = page.get_by_role("button", name=re.compile(r"^Cart(?:,|$)"))

    def product_names(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_text_contents()

    def product_card(self, name: str) -> Locator:
        return self.product_cards.filter(has_text=name)

    def add_product(self, name: str) -> None:
        self.product_card(name).get_by_role("button", name="Add to cart").click()

    def open_product_details(self, name: str) -> None:
        detail_button = self.product_card(name).get_by_role(
            "button", name=f"View details for {name}"
        ).filter(has_text=name)
        detail_button.click()

    def open_cart(self) -> None:
        self.cart_button.click()
