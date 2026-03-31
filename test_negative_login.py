from playwright.sync_api import Playwright, sync_playwright


def test_negative_login(playwright: Playwright) -> None:
    # Запуск браузера (видимый режим)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Открываем сайт
    page.goto("https://www.saucedemo.com/")

    # Негативный сценарий логина: верный логин, неверный пароль
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("wrong_password")
    page.locator("[data-test='login-button']").click()

    # Проверяем, что появилось сообщение об ошибке
    error_text = page.locator("[data-test='error']").inner_text()
    assert "Username and password do not match" in error_text, \
        "Ошибка: сообщение о неверном логине/пароле не появилось"

    # Закрываем браузер
    context.close()
    browser.close()


# Запуск теста
with sync_playwright() as playwright:
    test_negative_login(playwright)
