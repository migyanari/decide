from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(executable_path="/home/migyanari/01enwindows/decide/decide/geckodriver", options=options)
driver.get("https://www.google.com/")
print('Title: %s' % driver.title)
driver.quit()
