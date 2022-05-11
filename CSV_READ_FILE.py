# CSV READ FILE
import csv 
import pandas as pd
from time import sleep
from selenium import webdriver

csv_file = pd.read_csv('Book1.csv', index_col=False)
for key,value in csv_file.iterrows()
    account = value['Accounts']
    accounts = account.split(':')
    driver = webdriver.Chrome('chromedriver_path')
    driver.get("https://www.reddit.com/")
    driver.find_element_by_xpath("//div//fieldset//input[@id='loginUsername']").send_keys(accounts[0])
    sleep(5)
    driver.find_element_by_xpath("//div//fieldset//input[@id='loginPassword']").send_keys(accounts[1])
    sleep(5)
    driver.find_element_by_xpath("//div//button[contains(text(),'Log In')]").click()
    sleep(2)
