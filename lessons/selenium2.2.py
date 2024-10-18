from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
  
    # x = browser.find_element(By.ID, "input_value").text

    # input1 = browser.find_element(By.ID, "answer")
    # y = calc(x)
    # input1.send_keys(y)

    # select = Select(browser.find_element(By.ID, "dropdown"))
    # select.select_by_value(x)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Vadim")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Nikolaev")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("VadimN@gmail.com")

    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    ChooseFile = browser.find_element(By.ID, "file")
    ChooseFile.send_keys(file_path)

    # browser.execute_script("window.scrollBy(0, 150)", "")

    # option2 = browser.find_element(By.ID, "robotsRule")
    # # browser.execute_script("return argument[0].scrollIntoView(true);", option2)
    # option2.click()
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # browser.execute_script("return argument[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()