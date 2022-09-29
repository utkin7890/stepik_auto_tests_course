from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math




browser = webdriver.Chrome()

try:
    def ln(x):
        return math.log(x)
    def sin(x):
        return math.sin(x)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # Selenium will Wait until price be 100$
    button = browser.find_element(By.ID, "book")
    price_text = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()

    x = int(browser.find_element(By.ID, "input_value").text)

    # extract clean formula from text
    formula_element = browser.find_element(By.CSS_SELECTOR, "label > :nth-child(1)")
    formula = formula_element.text.split()[2].replace(",", "")
    result_formula = eval(formula)

    form_element = browser.find_element(By.ID, "answer")
    form_element.send_keys(result_formula)

    submit_buttom = browser.find_element(By.ID, "solve")
    submit_buttom.click()
finally:
    time.sleep(10)
    browser.quit()

    # add an empty line for unix system


