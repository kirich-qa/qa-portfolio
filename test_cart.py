from playwright.sync_api import Playwright, sync_playwright


def test_add_to_cart(playwright: Playwright) -> None:
    # Запуск браузера (видимый режим)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Открываем сайт
    page.goto("https://www.saucedemo.com/")

    # Авторизация
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    # Проверяем, что вход выполнен успешно
    assert page.url.endswith("/inventory.html"), "Ошибка: логин не выполнен"

    # Добавление товара в корзину
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    # Переходим в корзину
    page.locator("[data-test='shopping-cart-link']").click()

    # Проверяем, что товар появился в корзине
    item_name = page.locator(".inventory_item_name").inner_text()
    assert item_name == "Sauce Labs Backpack", "Ошибка: товар не найден в корзине"

    # Закрываем браузер
    context.close()
    browser.close()


# Запуск теста
with sync_playwright() as playwright:
    test_add_to_cart(playwright)
