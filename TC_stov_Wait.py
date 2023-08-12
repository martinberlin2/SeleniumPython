geloescht - ich bin da weiter
 ## TC_popup_cookies_deny
## Weiterleitung bahn.de -> ? https://auticon.com/de/#


# Selenium / Python imports
# import logging 
# from selenium.common.exceptions import NoSuchElementException  
# from selenium.webdriver.common.action_chains import ActionChains

import selenium.webdriver 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from datetime import date
from Utilities.Helper import VisibleAfter
import time 

def tc(driver): # -> string

	driver.get('https://osf.io/preprints/discover?subject=bepress%7CSocial%20and%20Behavioral%20Sciences')
	
	# driver.get('http://www.bahn.de/')

	cssSelector = "div.flex-item:nth-child(2) > button:nth-child(1)"
	
	s, elem  = VisibleAfter(driver, cssSelector)
	# print("print (str(tmp)):")
	# print (str(tmp))
	
	# print("VisibleAfter done")
	# s = tmp.seconds
	# elem = tmp.elem 
	 
	# def VisibleAfter(driver, cssSelector): # -> (seconds, elem) : cssSelector visible after seconds, returns elem, too
	print("Seconds: " + str(s))
	print(str(elem))
		
	print(len(driver.find_elements(By.CSS_SELECTOR,cssSelector)))
	for ele in driver.find_elements(By.CSS_SELECTOR,cssSelector):
		print(ele.text)
		