from datetime import datetime
import logging
import os
from pathlib import Path
import re

import pytest
from playwright.sync_api import Page

from pages import CartPage, CheckoutPage, InventoryPage, LoginPage


REPORTS_DIR = Path(__file__).resolve().parents[1] / "reports"
BASE_URL = os.environ.get("SAUCEDEMO_BASE_URL", "https://www.saucedemo.com")
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
logger = logging.getLogger("saucedemo")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session: pytest.Session) -> None:
    # 1. Keep shared diagnostics in one project-local folder for each run.
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    handler = logging.FileHandler(REPORTS_DIR / "saucedemo.log", encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.info("Test session started")


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page, BASE_URL)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    # 2. Start each workflow from an independently authenticated browser page.
    login = LoginPage(page, BASE_URL)
    login.open()
    login.login(USERNAME, PASSWORD)
    inventory = InventoryPage(page)
    inventory.heading.wait_for()
    return inventory


@pytest.fixture
def cart_page(page: Page, inventory_page: InventoryPage) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_page(
    page: Page, inventory_page: InventoryPage
) -> CheckoutPage:
    inventory_page.add_product("Sauce Labs Backpack")
    inventory_page.open_cart()
    CartPage(page).start_checkout()
    checkout = CheckoutPage(page)
    checkout.first_name.wait_for()
    return checkout


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item: pytest.Item, call: pytest.CallInfo[object]
):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return

    page = item.funcargs.get("page")
    if page is None:
        logger.error("Failed test %s has no page fixture for a screenshot", item.nodeid)
        return

    # 3. Preserve the original test failure if diagnostic capture itself fails.
    test_id = re.sub(r"[^A-Za-z0-9_-]+", "_", item.name).strip("_")
    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    screenshot = REPORTS_DIR / f"TC_{test_id}_STEP_call_{timestamp}.png"
    try:
        page.screenshot(path=str(screenshot), full_page=True)
        logger.error("Failure screenshot for %s: %s", item.nodeid, screenshot)
    except Exception:
        logger.exception("Could not capture failure screenshot for %s", item.nodeid)


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    reporter = session.config.pluginmanager.get_plugin("terminalreporter")
    if reporter is not None:
        counts = {
            outcome: len(reporter.stats.get(outcome, []))
            for outcome in ("passed", "failed", "skipped", "deselected")
        }
        logger.info("Test session finished with exit status %s: %s", exitstatus, counts)
    else:
        logger.info("Test session finished with exit status %s", exitstatus)
