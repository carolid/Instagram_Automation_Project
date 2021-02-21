from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get("https://www.instagram.com/")
sleep(2)

username_input = browser.find_element_by_name("username")
username_input.click()
username_input.send_keys("toebeans_photographs")

password_input = browser.find_element_by_name("password")
password_input.click()
password_input.send_keys("photos4life")

login_button = browser.find_element_by_xpath("//button[@type = 'submit']")
login_button.click()

sleep(5)
browser.close()





