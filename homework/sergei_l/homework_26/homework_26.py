import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://testshop.qa-practice.com/")
    chrome_driver = webdriver.Chrome(options=chrome_options)
    return chrome_driver


@pytest.fixture()
def action(driver):
    action = ActionChains(driver)
    return action


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 5)
    return wait


def test_add_to_cart(driver, action, wait):
    driver.get('http://testshop.qa-practice.com/')
    product_names = driver.find_elements(By.CLASS_NAME, 'o_wsale_products_item_title')
    product_name = product_names[0].text
    product_cards = driver.find_elements(By.CLASS_NAME, 'oe_product_image_link')
    action.key_down(Keys.COMMAND).click(product_cards[0]).key_up(Keys.COMMAND).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    wait.until(EC.element_to_be_clickable((By.ID, 'add_to_cart')))
    atc_button = driver.find_element(By.ID, 'add_to_cart')
    atc_button.click()
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-secondary')))
    continue_button = driver.find_element(By.CLASS_NAME, 'btn-secondary')
    continue_button.click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'my_cart_quantity')))
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.refresh()
    cart_button = driver.find_element(By.CLASS_NAME, 'fa-shopping-cart')
    cart_button.click()
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h6')))
    product_name_final = driver.find_elements(By.TAG_NAME, 'h6')
    assert product_name in product_name_final[0].text


def test_hover_product(driver, action, wait):
    driver.get('http://testshop.qa-practice.com/')
    product_names = driver.find_elements(By.CLASS_NAME, 'o_wsale_products_item_title')
    product_name = product_names[0].text
    action.move_to_element(driver.find_element(By.CLASS_NAME, 'oe_product_image_link'))
    action.move_to_element(driver.find_elements(By.CLASS_NAME, 'o_wsale_product_btn')[0])
    action.click()
    action.perform()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'product-name')))
    product_name_final = driver.find_element(By.CLASS_NAME, 'product-name')
    assert product_name in product_name_final.text
