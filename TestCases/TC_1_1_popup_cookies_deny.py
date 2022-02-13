

# import time
import logging 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def tc(driver): # -> bool
	# driver.get("https://auticon.de")   # Popups nach neuem Laden und Cookie auticon.de gelöscht
	# print("TC_1_1_popup_cookies_deny STUB ended")
	# return "TC_1_1_popup_cookies_deny STUB ended"
	 
	### driver.get("https://auticon.de")  
	# time.sleep(1)
		# Popups Offene Stellen nach neuem Laden kommt nicht mehr, aber Cookiedialog wohl
	# print("TC_1_1_popup_cookies_deny")
	cssSelector = '._brlbs-refuse-btn > a:nth-child(1)'

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
	
	# def isNotVisible(cssSelector, seconds): # für Promise-Lösung
	if isNotVisible(driver, cssSelector, 0.5): 
		return True  # ok-0912
	return False  # ok-0912     # hier ohne reporting... nach merge in develop
	###################
	
	# time.sleep(1) # man braucht 1 sek
	
	# # nicht: EC.presence_of_element_located
	# # geht: EC.visibility_of_element_located 
	# try:
		# acceptOnlyEssCookies = WebDriverWait(driver, 1).until(
		# EC.visibility_of_element_located((By.CSS_SELECTOR, '._brlbs-refuse-btn > a:nth-child(1)')))
	# # try: # ok
		# # acceptOnlyEssCookies = driver.find_element(By.CSS_SELECTOR, '._brlbs-refuse-btn > a:nth-child(1)')
		# # acceptOnlyEssCookies.click() # Popup ist schon weg
	# except Exception as ex:
		# # if str(ex) != 'Message: Element <a class="_brlbs-btn _brlbs-cursor" href="#"> could not be scrolled into view\n':
		# if str(ex) != 'Message: \n':
			# logging.info("Andere Exception:" + str(ex) + "!")
			# return False  # ok
		# return True # nach Klick ist Cookie-Dialog beendet      # ok
	# logging.info("Wait zu kurz -- Cookie-Dialog noch nicht weg beendet")
	# return False # ok
	
def isNotVisible(driver, cssSelector, seconds): # cssSelector weg nach max seconds -- für Promise-Lösung: verschwindet Elem nach seconds, z.B. nach click) ?; # sehr genau, bei 0.20000000000000004 False bei seconds = 0.2
	s = 0
	step = 0.01
	while s < seconds:
		try:
			elem = WebDriverWait(driver, step).until(
			EC.visibility_of_element_located((By.CSS_SELECTOR, cssSelector)))
		except Exception as ex:
			print ("TRUE elem invisible after seconds " + str(s) + " " + str(ex))
			return True   # ok-0912
		print(str(s))
		s = s + step
	print ("FALSE elem still visible after seconds " + str(s))
	return False # ok-0912

# https://stackoverflow.com/questions/43778842/python-promise-how-to-wait-for-page-load-or-webelement-using-promises	
	# # return True if element is visible within 30 seconds, otherwise False
# def is_visible(locator, timeout = 30):
    # try:
        # ui.WebDriverWait(chrome, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        # return True
    # except TimeoutException:
        # return False
	
	# Handle Idle Time During a test

# Selenium involves implicit and explicit waits. In the case of Explicit wait, the driver waits for a specific action to complete and in implicit wait, the driver waits for a particular time duration. Using WebDriverWait()function will help the WebDriver to wait for a specific time, say five seconds. Then to test for new element to load, use: .presence_of_element_located()method(belonging to expected_conditionsclass); Use By.ID.
 
  
# try:
	# element = WebDriverWait(driver, 5).until(
	# EC.presence_of_element_located((By.ID, "id-of-new-element"))
# )
# finally:
# driver.quit()



		
# 11.11 Laeuft - TODO: Wait noch mit Promises, kein sleep