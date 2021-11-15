

import time
import logging 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
	
	Handle Idle Time During a test

# Selenium involves implicit and explicit waits. In the case of Explicit wait, the driver waits for a specific action to complete and in implicit wait, the driver waits for a particular time duration. Using WebDriverWait()function will help the WebDriver to wait for a specific time, say five seconds. Then to test for new element to load, use: .presence_of_element_located()method(belonging to expected_conditionsclass); Use By.ID.
 
  
try:
element = WebDriverWait(driver, 5).until(
EC.presence_of_element_located((By.ID, "id-of-new-element"))
)
finally:
driver.quit()