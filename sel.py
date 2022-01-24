from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()

driver.get("http://localhost/testing/")
fnameku = 'Rahma'
lasnameku = 'Syndu Grananta'
emailku = 'syndu@gov.il'
phoneku = '+6213371337133' 
negaraku = 'Indonesia'
pesanku = 'Nama Rahma Syndu Grananta'

fname = driver.find_element_by_name('fname')
fname.send_keys(fnameku)
lname = driver.find_element_by_name('lname')
lname.send_keys(lasnameku)
email = driver.find_element_by_name('email')
email.send_keys(emailku)
phone = driver.find_element_by_name('phone')
phone.send_keys(phoneku)
country = driver.find_element_by_id('country')
dropdown = Select(country)
dropdown.select_by_visible_text(negaraku)

phone = driver.find_element_by_name('message')
phone.send_keys(pesanku)

time.sleep(7)
submit_button = driver.find_elements_by_xpath('/html/body/div/section/form/button')[0]
submit_button.click()