import re

from playwright.sync_api import Page, expect

from pages import CartPage, InventoryPage


def test_inventory_lists_products(inventory_page: InventoryPage) -> None:
    expect(inventory_page.heading).to_be_visible()
    assert len(inventory_page.product_names()) == 6


def test_product_details_can_be_opened(
    inventory_page: InventoryPage, page: Page
) -> None:
    inventory_page.open_product_details("Sauce Labs Backpack")

    expect(page).to_have_url(re.compile(r".*/inventory-item\.html\?id=4$"))
    expect(page.get_by_text("Sauce Labs Backpack", exact=True)).to_be_visible()
    expect(page.get_by_role("button", name="Back to products")).to_be_visible()


def test_added_product_is_visible_in_cart(
    inventory_page: InventoryPage, cart_page: CartPage
) -> None:
    inventory_page.add_product("Sauce Labs Backpack")
    inventory_page.open_cart()

    expect(cart_page.heading).to_be_visible()
    assert cart_page.item_names() == ["Sauce Labs Backpack"]


def test_product_can_be_removed_from_cart(
    inventory_page: InventoryPage, cart_page: CartPage, page: Page
) -> None:
    inventory_page.add_product("Sauce Labs Backpack")
    inventory_page.open_cart()
    cart_page.remove_item("Sauce Labs Backpack")

    expect(cart_page.heading).to_be_visible()
    assert cart_page.item_names() == []
    expect(page.get_by_role("button", name="Cart, empty")).to_be_visible()
