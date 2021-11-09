
import time
import logging 
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains


def tc(driver): # -> bool
	driver.get("https://auticon.de")  
	# time.sleep(1)
		# Popups Offene Stellen nach neuem Laden kommt nicht mehr, aber Cookiedialog wohl
	print("TC_1_1_popup_cookies_deny")
	try:
		# acceptOnlyEssCookies = driver.find_element(By.CLASS_NAME, 'x_brlbs-refuse-btn')
		acceptOnlyEssCookies = driver.find_element(By.CSS_SELECTOR, '._brlbs-refuse-btn > a:nth-child(1)')	
	except NoSuchElementException as nse:
		logging.info ("Fehler: Keine Möglichkeit nur essenzielle Cookies zu wählen: " + str(nse))
		return False
	except Exception as ex:
		logging.error ("EXC TC_1_1_popup_cookies_deny: " + str(ex))
		return False
	# action = ActionChains(driver)
	
	acceptOnlyEssCookies.click() # geht!
	time.sleep(1) # man braucht 1 sek
	try: 
		acceptOnlyEssCookies = driver.find_element(By.CLASS_NAME, '_brlbs-refuse-btn')
		acceptOnlyEssCookies.click() # geht!! Popup ist schon weg
	except Exception as ex:
		if str(ex) != 'Message: Element <p class="_brlbs-refuse-btn"> could not be scrolled into view':
			logging.info("Andere Exception" + str(ex))
			return False
		return True # nach Klick ist Cookie-Dialog beendet
	print("TC_1_1 Error")
	return False
	
	# 0911 sollte so laufen -- alle Zweige testen, dann nochmal committen