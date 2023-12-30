from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.implicitly_wait(5)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()
    browser.find_element(By.ID, "answer").send_keys(calc(browser.find_element(By.ID, "input_value").text))
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.ID, "solve"))
    browser.find_element(By.ID, "solve").click()
    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()