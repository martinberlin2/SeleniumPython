

# import time
import logging 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def tc(driver): # -> bool
	# driver.get("https://auticon.de")   # Popups nach neuem Laden und Cookie auticon.de gelöscht
	### driver.get("https://auticon.de")  
	# time.sleep(1)
		# Popups Offene Stellen nach neuem Laden kommt nicht mehr, aber Cookiedialog wohl
	cssSelector = '._brlbs-refuse-btn > a:nth-child(1)'

# p._brlbs-refuse-btn > a:nth-child(1)

	try:
		# acceptOnlyEssCookies = driver.find_element(By.CLASS_NAME, 'x_brlbs-refuse-btn')
		acceptOnlyEssCookies = driver.find_element(By.CSS_SELECTOR, cssSelector)	
	except NoSuchElementException as nse:
		logging.info ("Fehler: Keine Moeglichkeit nur essenzielle Cookies zu waehlen: " + str(nse))
		return False  # ok-0912
	except Exception as ex:
		logging.error ("EXC TC_1_1_popup_cookies_deny: " + str(ex))
		return False  # ok-0912
	# action = ActionChains(driver)
	
	acceptOnlyEssCookies.click() # geht! Popup muss dann weg sein
	# return 
	# def isNotVisible(cssSelector, seconds): # für Promise-Lösung
	if isNotVisible(driver, cssSelector, 0.5): 
		return True  # ok-0912
	return False  # ok-0912     # hier ohne reporting... nach merge in develop

	
def isNotVisible(driver, cssSelector, seconds): # cssSelector weg nach max seconds -- für Promise-Lösung: verschwindet Elem nach seconds, z.B. nach click) ?; # sehr genau, bei 0.20000000000000004 False bei seconds = 0.2
	s = 0
	step = 0.01
	while s < seconds:
		try:
			elem = WebDriverWait(driver, step).until(
			EC.visibility_of_element_located((By.CSS_SELECTOR, cssSelector)))
		except Exception as ex:
			# print ("TRUE elem invisible after seconds " + str(s) + " " + str(ex))
			return True   
		# print(str(s))
		s = s + step
	# print ("FALSE elem still visible after seconds " + str(s))
	return False 
