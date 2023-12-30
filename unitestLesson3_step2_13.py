import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test(unittest.TestCase):

    def test_one(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys("mm@molensk.hvh")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_two(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys("mm@molensk.hvh")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
if __name__ == "__main__":
    unittest.main()
