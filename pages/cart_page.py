from playwright.sync_api import Locator, Page


class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.heading = page.get_by_text("Your Cart", exact=True)
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.get_by_role("button", name="Checkout")
        self.continue_shopping_button = page.get_by_role(
            "button", name="Continue Shopping"
        )

    def item_names(self) -> list[str]:
        return self.page.locator(".cart_item .inventory_item_name").all_text_contents()

    def item(self, name: str) -> Locator:
        return self.cart_items.filter(has_text=name)

    def remove_item(self, name: str) -> None:
        self.item(name).get_by_role("button", name="Remove").click()

    def start_checkout(self) -> None:
        self.checkout_button.click()
