
import time
import logging 
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains


def tc(driver): # -> bool
	driver.get("https://auticon.de")   # Popups Offene Stellen nach neuem Laden und Cookie auticon.de gelöscht
	print("TC_1_1_popup_cookies_deny")
	try:
		acceptOnlyEssCookies = driver.find_element(By.CLASS_NAME, '_brlbs-refuse-btn')
	except NoSuchElementException as nse:
		print("EXC Keine Möglichkeit nur essenzielle Cookies zu wählen: " + str(ex))
		return False
	except Exception as ex:
		print("EXC TC_1_1_popup_cookies_deny: " + str(ex))
		return False
	# action = ActionChains(driver)
	
	time.sleep(1) # Sleep for 3 seconds
	acceptOnlyEssCookies.click() # geht!
	time.sleep(5) # Sleep for 3 seconds
	try: 
		acceptOnlyEssCookies.click() # geht!! Popup ist schon weg
	except Exception as ex:
		print(str(ex))

	try:
		acceptOnlyEssCookies = driver.find_element(By.CLASS_NAME, '_brlbs-refuse-btn')
		text = acceptOnlyEssCookies.text 
		if text == "":
			text = "LEER"
		print("acceptOnlyEssCookies.text :" + text)
	except NoSuchElementException as nse:
		return True # nach Klick ist Cookie-Dialog beendet
	
	return False
	
   # <button type="button" class="pum-close popmake-close" aria-label="Schließen">
   
   # <a class="_brlbs-btn _brlbs-cursor" href="#" tabindex="0" role="button" data-cookie-refuse="">
                                         #   Nur essenzielle Cookies akzeptieren                                        </a>