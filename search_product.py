from playwright.sync_api import Page, expect


def test_search_for_laptop_displays_product(page: Page) -> None:
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("#small-searchterms").fill("Laptop")
    page.locator("input.button-1.search-box-button").click()

    laptop_result = page.locator(".product-title").filter(has_text="Laptop").first
    expect(laptop_result).to_be_visible()
