from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    optimalPrice = WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book = browser.find_element(By.ID, "book")
    book.click()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    inputh1 = browser.find_element(By.ID, "answer")
    inputh1.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

    # message = browser.find_element(By.ID, "verify_message")
    # assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()