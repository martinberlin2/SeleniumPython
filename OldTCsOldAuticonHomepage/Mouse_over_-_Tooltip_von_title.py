

import logging 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

# TC ist abhängig davon, dass die Popups weg sind
	# TC_1_1_popup_cookies_deny
	# TC_1_2_popup_openPositions
	# Und der TC darf nicht vorher schon mal gelaufen sein, so dass die Maus schon da ist 
# -- TODO Blocked TC einführen

# title="Home_1_DE" 
# elem.get_attribute("title")
# angezeigt bei mouse over (elem)

def tc(driver): # -> bool
	TC_name = "Mouse over - Tooltip von title"
	expectedResult = "Home_1_DE"
	# print(TC_name)
	try:
		elem = None
		try: 
			elem = driver.find_element(By.CSS_SELECTOR, '.vc_custom_1542025788808 > figure:nth-child(1) > a:nth-child(1) > img:nth-child(1)' ) 
			# mouse-over
			hover = ActionChains(driver).move_to_element(elem)
			hover.perform()
			time.sleep(5)  # zeigt Tooltip an ! manuell sichtbar
			# !!! vor Firefox-Update nicht sichtbar ! danach auch nicht ! 
			# für title - Abfrage aber egal
			if elem == None: 
				print(TC_name + ": elem == None")
		except NoSuchElementException as nsee:
			toReturn = "FAILED: NSE EXC " + TC_name + ": " + str(nsee)
			logging.error(toReturn)
			# print(toReturn)
			return toReturn
		except Exception as e: 
			toReturn = "FAILED: EXC findelem mouse over: " + str(e)
			logging.error(toReturn)
			return toReturn
		
		actualResult = elem.get_attribute("title")
		
		# evalTest(expectedResult, actualResult)
		if expectedResult == actualResult:
			return "Passed"
		return "FAILED: Result = " + str(actualResult)
	
	except Exception as ex:
		toReturn = "FAILED: EXC " + TC_name + ": " + str(ex)
		# print(toReturn)
		return toReturn
	return "Passed, but dead code here!"
