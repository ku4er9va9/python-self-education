from selenium import webdriver
from selenium.webdriver.common.by import By
import time

USER_INFO = {
    'name': 'Your Name',
    'last_name': 'Your Last Name',
    'number': '0980000000',
    'email': 'your_email@example.com',
    'password': 'qazWSX123'
}

driver = webdriver.Chrome()
driver.get("https://rozetka.com.ua/")

time.sleep(2)
login_button = driver.find_element(By.CSS_SELECTOR, 'body > app-root > div > div > rz-header > rz-main-header > header > div > div > ul > li.header-actions__item.header-actions__item--user > rz-user > button > svg > use')
login_button.click()

time.sleep(2)
register_button = driver.find_element(By.CSS_SELECTOR, 'body > app-root > rz-single-modal-window > div.modal__holder.modal__holder_show_animation.modal__holder--medium > div.modal__content > rz-user-identification > rz-auth > div > form > fieldset > div.form__row.auth-modal__form-bottom > button.auth-modal__register-link.button.button--link.ng-star-inserted')
register_button.click()

name = driver.find_element(By.CSS_SELECTOR, '#registerUserName')
name.send_keys(USER_INFO['name'])


last_name = driver.find_element(By.CSS_SELECTOR, '#registerUserSurname')
last_name.send_keys(USER_INFO['last_name'])

number = driver.find_element(By.CSS_SELECTOR, '#registerUserPhone')
number.send_keys(USER_INFO['number'])

email = driver.find_element(By.CSS_SELECTOR, '#registerUserEmail')
email.send_keys(USER_INFO['email'])

password = driver.find_element(By.CSS_SELECTOR, '#registerUserPassword')
password.send_keys(USER_INFO['password'])

register_submit_button = driver.find_element(By.CSS_SELECTOR, 'body > app-root > rz-single-modal-window > div.modal__holder.modal__holder_show_animation.modal__holder--medium > div.modal__content > rz-user-identification > rz-register > div > form > fieldset > div.form__row.auth-modal__form-bottom > button.button.button--large.button--green.auth-modal__submit')
register_submit_button.click()

time.sleep(2)
driver.close()
driver.quit()