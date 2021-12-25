from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def main():
    PATH ="/home/uliana/Документы/chromedriver"
    s = Service(PATH)
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.fb.com")
    url = driver.current_url
    if url == "https://www.facebook.com/":
        link = driver.find_element(By.LINK_TEXT, "Создать новый аккаунт")
        link.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "reg_box")))
        sign_up(driver)
    else:
        print("not redirected")


    time.sleep(20)

def sign_up(driver):
    name = driver.find_element(By.NAME, "firstname")
    name.send_keys("Jane")
    surname = driver.find_element(By.NAME, "lastname")
    surname.send_keys("Smith")
    email = driver.find_element(By.NAME, "reg_email__")
    email.send_keys("tardis62@rmune.com")
    email2 = driver.find_element(By.NAME, "reg_email_confirmation__")
    email2.send_keys("tardis62@rmune.com")
    password = driver.find_element(By.NAME, "reg_passwd__")
    password.send_keys("12345qwerty")
    day = Select(driver.find_element(By.ID, "day"))
    day.select_by_visible_text('1')
    month = Select(driver.find_element(By.ID, "month"))
    month.select_by_visible_text('янв')
    year = Select(driver.find_element(By.ID, "year"))
    year.select_by_visible_text('2001')

    gender = driver.find_element(By.CSS_SELECTOR, "input[name='sex'][value='1']")
    gender.click()

    time.sleep(2)
    button = driver.find_element(By.NAME, "websubmit")
    button.click()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
