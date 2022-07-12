from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('https://twitter.com/jaintle/status/1526449952179855360')
sleep(5)

driver.get_screenshot_as_file("screenshot1.png")
driver.quit()
print("end...")