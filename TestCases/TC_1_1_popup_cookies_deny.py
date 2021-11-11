

import time
import logging 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains


def tc(driver): # -> bool
	driver.get("https://auticon.de")  
	# time.sleep(1)
		# Popups Offene Stellen nach neuem Laden kommt nicht mehr, aber Cookiedialog wohl
	# print("TC_1_1_popup_cookies_deny")
	try:
		# acceptOnlyEssCookies = driver.find_element(By.CLASS_NAME, 'x_brlbs-refuse-btn')
		acceptOnlyEssCookies = driver.find_element(By.CSS_SELECTOR, '._brlbs-refuse-btn > a:nth-child(1)')	
	except NoSuchElementException as nse:
		logging.info ("Fehler: Keine Moeglichkeit nur essenzielle Cookies zu waehlen: " + str(nse))
		return False # ok
	except Exception as ex:
		logging.error ("EXC TC_1_1_popup_cookies_deny: " + str(ex))
		return False # ok
	# action = ActionChains(driver)
	
	acceptOnlyEssCookies.click() # geht!
	time.sleep(1) # man braucht 1 sek
	try: # ok
		acceptOnlyEssCookies = driver.find_element(By.CSS_SELECTOR, '._brlbs-refuse-btn > a:nth-child(1)')
		acceptOnlyEssCookies.click() # geht!! Popup ist schon weg
	except Exception as ex:
		if str(ex) != 'Message: Element <a class="_brlbs-btn _brlbs-cursor" href="#"> could not be scrolled into view\n':
			logging.info("Andere Exception" + str(ex))
			return False  # ok
		return True # nach Klick ist Cookie-Dialog beendet      # ok
	logging.info("Wait zu kurz -- Cookie-Dialog noch nicht weg beendet")
	return False # ok
	
	# 11.11 Laeuft - TODO: Wait noch mit Promises, kein sleep