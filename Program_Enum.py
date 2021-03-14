from selenium import webdriver
import time
import random

urls= {"https://hackerone.com/directory/programs?asset_type=CIDR&order_direction=DESC&order_field=started_accepting_at", "https://hackerone.com/directory/programs?asset_type=URL&order_direction=DESC&order_field=started_accepting_at"}

driver = webdriver.Firefox('./')

def query(url):
    driver.get(url)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(6.0,11.0))
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    program = driver.find_elements_by_xpath('//a[@class="daisy-link routerlink daisy-link daisy-link--major spec-profile-name"]')
    for x in range (len(program)):
        print(program[x].text)

for x in urls:
    query(x)

   
