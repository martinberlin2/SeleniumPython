import logging 
from selenium.common.exceptions import NoSuchElementException  

def tc(driver): # -> bool
	driver.get("https://auticon.de")   # Popups nach neuem Laden und Cookie auticon.de gelöscht
	print("TC_1_1_popup_cookies_deny")
	try:
		onlyEssCookies = driver.find_elements(By.CLASS_NAME, '_brlbs-refuse-btn')
	except NoSuchElementException as nse:
		print("EXC Keine Möglichkeit nur essenzielle Cookies zu wählen: " + str(ex))
		return False
	except Exception as ex:
		print("EXC TC1: " + str(ex))
		return False
	action = ActionChains(driver)
	onlyEssCookies.click()
	try:
		onlyEssCookies = driver.find_elements(By.CLASS_NAME, '_brlbs-refuse-btn')
	except NoSuchElementException as nse:
		return True # nach Klick ist Cookie-Dialog beendet
	
	return False
	
   # <button type="button" class="pum-close popmake-close" aria-label="Schließen">
   
   # <a class="_brlbs-btn _brlbs-cursor" href="#" tabindex="0" role="button" data-cookie-refuse="">
                                         #   Nur essenzielle Cookies akzeptieren                                        </a>