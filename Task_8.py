# Импортируем необходимые библиотеки
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запускаем браузер Google Chrome
driver = webdriver.Chrome()

# Открываем страницу https://www.random.org/dice/
driver.get("https://www.random.org/dice/")

# Нажимаем на кнопку Roll Dice
roll_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value="Roll Dice"]'))
)
roll_button.click()

# Ожидаем, пока результаты станут видимыми
result_table = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'table.die.summary'))
)

# Закрываем браузер
driver.quit()