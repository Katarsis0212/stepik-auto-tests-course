from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
book = browser.find_element(By.ID, "book")
book.click()

import math
def calc(x): return str(math.log(abs(12*math.sin(int(x)))))

x_elem = browser.find_element_by_id("input_value")
x = x_elem.text
y = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(y)

solve = browser.find_element(By.ID, "solve")
solve.click()

time.sleep(10)
browser.quit()
