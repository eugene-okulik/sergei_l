from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 5)

driver.get('https://demoqa.com/automation-practice-form')
form_first_name = driver.find_element(By.ID, 'firstName')
form_first_name.send_keys('test first name')

form_last_name = driver.find_element(By.ID, 'lastName')
form_last_name.send_keys('test last name')

form_email = driver.find_element(By.ID, 'userEmail')
form_email.send_keys('test@email.fun')

form_gender = driver.find_elements(By.CSS_SELECTOR, '.custom-control.custom-radio')
form_gender[0].click()

form_mobile = driver.find_element(By.ID, 'userNumber')
form_mobile.send_keys('1232343455')

form_dob = driver.find_element(By.ID, 'dateOfBirthInput')
form_dob.click()
form_dob_year = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
select_year = Select(form_dob_year)
select_year.select_by_value('1996')
form_dob_month = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
select_month = Select(form_dob_month)
select_month.select_by_value('2')
form_dob_day = driver.find_element(By.CLASS_NAME, 'react-datepicker__day--012')
form_dob_day.click()

subjects_list = ['English', 'Physics', 'Arts']
form_subjects = driver.find_element(By.ID, 'subjectsInput')
for subject in subjects_list:
    form_subjects.send_keys(subject)
    form_subjects.send_keys(Keys.ENTER)
    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'subjects-auto-complete__value-container'), subject)
    )

driver.execute_script("window.scrollBy(0, 250);")
form_hobbies = driver.find_element(By.CSS_SELECTOR, '.custom-control-label[for="hobbies-checkbox-2"]')
form_hobbies.click()

form_address = driver.find_element(By.ID, 'currentAddress')
form_address.send_keys('Better place palace, 29/3')

form_state = driver.find_element(By.ID, 'react-select-3-input')
form_state.send_keys('ncr')
form_state.send_keys(Keys.ENTER)

form_city = driver.find_element(By.ID, 'react-select-4-input')
form_city.send_keys('delhi')
form_city.send_keys(Keys.ENTER)
form_submit = driver.find_element(By.ID, 'userForm')
form_submit.submit()

send_data_table = driver.find_element(By.CLASS_NAME, 'table')
print(send_data_table.text)
