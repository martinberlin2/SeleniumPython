

# TC_5_Scrolling_Elem_Present_not_Visible
# Desktop Modus, Vollbild und Teilbild 
# TC ist abhängig davon, dass die Popups weg sind
	# TC_1_1_popup_cookies_deny
	# TC_1_2_popup_openPositions	
# erstmal durch zufälliges Harness gelöst: TC_5_ ist letzter TC

# Selenium / Python imports
import logging 
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import selenium.webdriver 
import time 

# driver wird kein zwingender Parameter mehr sein
# hier Test mit https://dilbert.com/ , die hat Endlos-Scroll 
	
# Link: AGB , unten auf Homepage
# Link zu: https://auticon.de/allgemeine-geschaeftsbedingungen-agb/
# kein test auf Nicht-Sichtbarkeit vor Scroll, SE liest DOM
from datetime import date

def tc(driver): # -> bool
	today = date.today()
	print("Today's date:", today)
	URL = "https://dilbert.com/"
	driver.get(URL)
	lnks=driver.find_elements_by_tag_name("a")
	# traverse list
	for lnk in lnks:
		# get_attribute() to get all href
		attr = lnk.get_attribute("href")
		strattr = str(attr)
		if strattr.startswith("https://dilbert.com/strip/") :
			if strattr.endswith(str(today)):
				print(attr)
				lnk.click()
	return "passed"
	TC = "TC_5_Scrolling_Elem_Present_not_Visible" # TODO dynamisch - als Modulname
	print(TC + " start")
	cssSelector = ''
	AGB_link = None
	try:
		AGB_link = driver.find_element(By.CSS_SELECTOR, cssSelector)
	except NoSuchElementException as nsex:
		toReturn = TC + ": NoSuchElementException - vor Scroll - OK"
		logging.info(toReturn)
		return toReturn
	except Exception as ex:
		logging.error(TC + "Andere Exception: " + str(ex))
		return str(ex) 
	# AGB_link.click() # scrollt selbst und klickt. Link geht. Kein test für visible
	# if AGB_link.is_displayed(): # == True: # Kein test für visible
	# isClickable(AGB_link)  # Kein test für visible 
	# link_loc = AGB_link.location_once_scrolled_into_view   # link_loc = {'x': 309, 'y': 852}; gleich nach Scroll 
	isClickable(AGB_link)
	elemIsThere = isVisibleAfter(driver, cssSelector, 5) # Returns float seconds, or bool: cssSelector visible after seconds on loaded webpage in driver. At once visible (no wait needed): 0. After timeout not visible: False
	if elemIsThere != False:
		print("Kein test für visible" + str(elemIsThere))
	
	
	
	## print("nach Exception noch drin") -- ok
	
	# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
	# da auch "unendlicher" Scroll 
	# hover = ActionChains(driver).move_to_element(elem)
			# hover.perform()

	#    #### SCROLL ####
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(5)
	
	isClickable(AGB_link)
	elemIsThere = isVisibleAfter(driver, cssSelector, 5) # Returns float seconds, or bool: cssSelector visible after seconds on loaded webpage in driver. At once visible (no wait needed): 0. After timeout not visible: False
	if elemIsThere == False:
		print("Nach Scroll nicht da" + str(elemIsThere))
		
	# to scroll to the bottom of the page.

	# ODER
	# label.sendKeys(Keys.PAGE_DOWN);
	
	# ODER
	# from selenium.webdriver.common.keys import Keys
	# html = driver.find_element_by_tag_name('html')
	# html.send_keys(Keys.END)
	
	if driver.get_full_page_screenshot_as_file('/Screenshots/foo.png'):
		print("Screenshots/foo erstellt")
	else:
		print("Screenshots/foo IO ERROR")
	
	elemIsThere = isVisibleAfter(driver, cssSelector, 5) # Returns float seconds, or bool: cssSelector visible after seconds on loaded webpage in driver. At once visible (no wait needed): 0. After timeout not visible: False
	if elemIsThere != False:
		print("Kein test für visible" + str(elemIsThere))
	
	
	# TODO
	# selenium.webdriver.support.expected_conditions.invisibility_of_element_located(locator)
	# selenium.webdriver.support.expected_conditions.visibility_of(element)
	
	# link_loc = AGB_link.location_once_scrolled_into_view
	# print ("link_loc = " + str(link_loc))    # link_loc = {'x': 309, 'y': 852} ; gleich nach Scroll
	
	try:
		AGB_link = driver.find_element(By.CSS_SELECTOR, cssSelector)
	except NoSuchElementException as nsex:
		toReturn = TC + ": NoSuchElementException nach Scroll"
		logging.info(toReturn)
		return toReturn
	except BaseException as ex:
		logging.error(TC + "Andere Exception nach Scroll: " + str(ex))
		return str(ex) 
	
	textLink = AGB_link.text
	expectTextLink = "AGB"
	if textLink != expectTextLink:
		erg = "Scroll OK ! anderer Text:\n" + textLink
		logging.info(erg)
		return erg
	return "Passed"
	
def isVisibleAfter(driver, cssSelector, timeout): # Returns float seconds, or bool: cssSelector visible after seconds on loaded webpage in driver. At once visible (no wait needed): 0. After timeout not visible: False
	from selenium.webdriver.support import expected_conditions as EC
	s = 0
	step = 0.01
	while s < timeout:
		try:	
			elem = WebDriverWait(driver, step).until(
			EC.visibility_of_element_located((By.CSS_SELECTOR, cssSelector)))
			return s 
		except Exception as ex:
			s = s + step
	# print ("FALSE elem still visible after seconds " + str(s))
	return False 

def isClickable(elem):
	from selenium.common.exceptions import WebDriverException
	try:
		elem.click()
		print ("Element is clickable")
	except WebDriverException:
		print ("Element is not clickable")
		return False
	return True