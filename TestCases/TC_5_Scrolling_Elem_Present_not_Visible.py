

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
import time 

# #text-2 > div:nth-child(1) > p:nth-child(1) > a:nth-child(1)
# Link: AGB , unten auf Homepage
# Link zu: https://auticon.de/allgemeine-geschaeftsbedingungen-agb/
# ohne Scrollen: NoSuchElementException

def tc(driver): # -> bool
	TC = "TC_5_Scrolling_Elem_Present_not_Visible" # TODO dynamisch - als Modulname
	print(TC + " start")
	cssSelector = 'text-2 > div:nth-child(1) > p:nth-child(1) > a:nth-child(1)'
	try:
		AGB_link = driver.find_element(driver.find_element(By.CSS_SELECTOR, cssSelector))
	except NoSuchElementException as nsex:
		toReturn = TC + ": NoSuchElementException - jetzt Scroll"
		logging.info(toReturn)
		# return toReturn
	except Exception as ex:
		logging.error(TC + "Andere Exception: " + str(ex))
		return str(ex) 
	print("nach Exception noch drin")
	
	# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
	# da auch "unendlicher" Scroll 
	# hover = ActionChains(driver).move_to_element(elem)
			# hover.perform()

	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	# to scroll to the bottom of the page.

	# ODER
	# label.sendKeys(Keys.PAGE_DOWN);
	
	# ODER
	# from selenium.webdriver.common.keys import Keys
	# html = driver.find_element_by_tag_name('html')
	# html.send_keys(Keys.END)
	
	try:
		AGB_link = driver.find_element(driver.find_element(By.CSS_SELECTOR, cssSelector))
	except NoSuchElementException as nsex:
		toReturn = TC + ": NoSuchElementException nach Scroll"
		logging.info(toReturn)
		return toReturn
	except Exception as ex:
		logging.error(TC + "Andere Exception nach Scroll: " + str(ex))
		return str(ex) 
	
	textLink = AGB_link.text
	expectTextLink = "AGB"
	if text1 != expectString:
		logging.info(TC + ": anderer Text:\n" + text1)
		return ("Scroll OK ! anderer Text:\n" + text1)
	return "Passed"