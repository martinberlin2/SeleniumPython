

import logging 
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def tc(driver): # -> bool
	driver.get("https://auticon.de")   # Popups nach neuem Laden und Cookie auticon.de gelöscht
	print("TC_1_1_popup_cookies_deny")
	try:
		acceptOnlyEssCookies = driver.find_element(By.CLASS_NAME, '_brlbs-refuse-btn')
	except NoSuchElementException as nse:
		print("EXC Keine Möglichkeit nur essenzielle Cookies zu wählen: " + str(ex))
		return False
	except Exception as ex:
		print("EXC TC_1_1_popup_cookies_deny: " + str(ex))
		return False
	action = ActionChains(driver)
	acceptOnlyEssCookies.click()
	try:
		acceptOnlyEssCookies = driver.find_element(By.CLASS_NAME, '_brlbs-refuse-btn')
		text = acceptOnlyEssCookies.text 
		print("acceptOnlyEssCookies.text :" + text)
	except NoSuchElementException as nse:
		return True # nach Klick ist Cookie-Dialog beendet
	
	return False
	
   # <button type="button" class="pum-close popmake-close" aria-label="Schließen">
   
   # <a class="_brlbs-btn _brlbs-cursor" href="#" tabindex="0" role="button" data-cookie-refuse="">
                                         #   Nur essenzielle Cookies akzeptieren                                        </a>