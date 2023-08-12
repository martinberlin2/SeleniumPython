
 ## TC_bahn_datepicker
## Weiterleitung bahn.de -> ? https://auticon.com/de/#


# Selenium / Python imports
# import logging 
# from selenium.common.exceptions import NoSuchElementException  
# from selenium.webdriver.common.action_chains import ActionChains

import selenium.webdriver 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from datetime import date
from Utilities.Helper import getElem
import time 

def tc(driver): # -> string
	
	driver.get('http://www.bahn.de/')
	time.sleep(5)
	# Kalender-Icon
	cssSelector = "yxfieldset.qf-fieldset:nth-child(4) > span:nth-child(3) > div:nth-child(1) > button:nth-child(1) > span:nth-child(1)"
	
	s, elem  = getElem(driver, "e", 10, cssSelector)
	print("Seconds: " + str(s))
	print(str(elem))
		
	print(len(driver.find_elements(By.CSS_SELECTOR,cssSelector)))
	for ele in driver.find_elements(By.CSS_SELECTOR,cssSelector):
		print(ele.text)
	
	# Kalender-Icon gefunden
	elem.click()	
	
	