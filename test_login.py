import time
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    # Запуск браузера в видимом режиме
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Открываем сайт
    page.goto("https://www.saucedemo.com/")
    time.sleep(1)  # пауза для визуального наблюдения

    # Ввод username
    page.locator("[data-test='username']").click()
    time.sleep(0.5)
    page.locator("[data-test='username']").fill("standard_user")
    time.sleep(0.5)

    # Ввод password
    page.locator("[data-test='password']").click()
    time.sleep(0.5)
    page.locator("[data-test='password']").fill("secret_sauce")
    time.sleep(0.5)

    # Нажатие кнопки login
    page.locator("[data-test='login-button']").click()
    time.sleep(1)

    # Ждём нажатия Enter, чтобы браузер не закрылся сразу
    print("Авторизация завершена. Нажмите Enter, чтобы закрыть браузер.")
    input()

    # Закрытие браузера
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
