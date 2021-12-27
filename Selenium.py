from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service('/Users/gautam/Desktop/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get(url='https://orteil.dashnet.org/experiments/cookie/')
time.sleep(3)

cookie = driver.find_element(By.ID, 'cookie')


while True:
    cookie.click()

    cursor = driver.find_element(By.ID, 'buyCursor')
    grandma = driver.find_element(By.ID, 'buyGrandma')
    factory = driver.find_element(By.ID, 'buyFactory')
    mine = driver.find_element(By.ID, 'buyMine')
    alchemy = driver.find_element(By.ID, 'buyAlchemy lab')
    portal = driver.find_element(By.ID, 'buyPortal')

    time_machine = driver.find_element(By.ID, 'buyTime machine')
    money = int(driver.find_element(By.ID, 'money').text.replace(",",''))
    cursor_cost = int(driver.find_element(By.CSS_SELECTOR, '#buyCursor b').text.split('-')[1].replace(",",''))
    grandma_cost = int(driver.find_element(By.CSS_SELECTOR, '#buyGrandma b').text.split('-')[1].replace(",",''))
    factory_cost = int(driver.find_element(By.CSS_SELECTOR, '#buyFactory b').text.split('-')[1].replace(",",''))
    mine_cost = int(driver.find_element(By.CSS_SELECTOR, '#buyMine b').text.split('-')[1].replace(",",''))
    alchemy_cost = int(driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b').text.split('-')[1].replace(",",''))
    portal_cost = int(driver.find_element(By.CSS_SELECTOR, '#buyPortal b').text.split('-')[1].replace(",",''))
    time_machine_cost = int(driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b').text.split('-')[1].replace(",",''))

    if money >= cursor_cost:
        cursor.click()
    elif money >= grandma_cost:
        grandma.click()
    elif money >= factory_cost:
        factory.click()
    elif money >= mine_cost:
        mine.click()
    elif money >= alchemy_cost:
        alchemy.click()
    elif money >= portal_cost:
        portal.click()
    elif money >= time_machine_cost:
        time_machine.click()