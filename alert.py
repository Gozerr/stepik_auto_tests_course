import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    # Ваш код, который заполняет обязательные поля
    pirce_correct = WebDriverWait(browser, 12).until(
       EC.text_to_be_present_in_element((By.ID, "price"), "$100")       
    )
    book_btn = browser.find_element(By.ID, "book")
    book_btn.click()

    value1 = browser.find_element(By.ID, "input_value")
    value_text = value1.text
    x = int(value_text)
    y = calc(x)

    field_answer = browser.find_element(By.ID, "answer")
    field_answer.send_keys(y)


    sub_button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", sub_button)
    sub_button.click()

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()