from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Установим драйвер
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 1. Открываем сайт
driver.get('https://www.saucedemo.com/')

# 2. Авторизация
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# 3. Добавляем товар в корзину
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# 4. Переходим в корзину
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# 5. Проверяем, что товар добавлен
item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
assert item_name == "Sauce Labs Backpack", f"Ожидался 'Sauce Labs Backpack', но был '{item_name}'"

# 6. Оформляем покупку
driver.find_element(By.ID, "checkout").click()

# 7. Заполняем данные для покупки
driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()

# 8. Завершаем покупку
driver.find_element(By.ID, "finish").click()

# 9. Проверяем, что покупка завершена успешно
success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
assert success_message == "Thank you for your order!", "Покупка не завершена успешно."

# Закрываем браузер
driver.quit()
