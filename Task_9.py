# Импортируем необходимые модули из Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запускаем браузер Google Chrome
driver = webdriver.Chrome()

# Открываем страницу https://www.random.org/coins/
driver.get("https://www.random.org/coins/")

# Ждем, пока выпадающий список с именем "num" не станет кликабельным
num_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "num"))
)

# Создаем объект Select из выпадающего списка с именем "num"
num_select = Select(num_dropdown)

# Выбираем опцию с value="2" в выпадающем списке
num_select.select_by_value("1")

# Ждем, пока выпадающий список с именем "cur" не станет кликабельным
cur_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "cur"))
)

# Создаем объект Select из выпадающего списка с именем "cur"
cur_select = Select(cur_dropdown)

# Выбираем опцию с текстом "AUD (Australian Dollar)" в выпадающем списке
cur_select.select_by_visible_text("East German 1 Mark")

# Нажимаем кнопку "Flip Coin(s)"
# flip_button = driver.find_element_by_css_selector('input[value="Flip Coin(s)"]')
# flip_button.click()

roll_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value="Flip Coin(s)"]'))
)
roll_button.click()

# Ожидаем, пока результаты станут видимыми
result_table = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'table.die.summary'))
)

# Закрываем браузер
driver.quit()