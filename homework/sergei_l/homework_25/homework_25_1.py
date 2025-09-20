from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

data = 'test'
driver.get('https://www.qa-practice.com/elements/input/simple')
text_input = driver.find_element(By.ID, 'id_text_string')
text_input.send_keys(data)
text_input.submit()
text_print = driver.find_element(By.ID, 'result-text')
print(text_print.text)
