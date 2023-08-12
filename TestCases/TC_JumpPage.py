
## TC_6_JumpPage
## Weiterleitung auticon.de -> https://auticon.com/de/#


# Selenium / Python imports
# import logging 
# from selenium.common.exceptions import NoSuchElementException  
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
import selenium.webdriver 
from datetime import date
import time 

def tc(driver): # -> string
	today = date.today()
	print("Today's date:", today)
	expected_url = "https://auticon.com/de/"
	startURL = "http://auticon.de"  # nur auticon.de geht nicht 
	driver.get(startURL)
	get_url = driver.current_url
	print("Fail - The current url is:" + str(get_url)) 
	if (get_url == expected_url):
		return "Passed"
	return result 
	# time.sleep(2)
	
	