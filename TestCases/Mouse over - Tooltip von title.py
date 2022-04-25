

import logging 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

# TC ist abhängig davon, dass die Popups weg sind
	# TC_1_1_popup_cookies_deny
	# TC_1_2_popup_openPositions
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
			time.sleep(2)  # zeigt Tooltip an ! manuell sichtbar
			# für title - Abfrage aber egal
			# # if elem == None: 
				# # print(TC_name + ": elem == None")
		except NoSuchElementException as nsee:
			toReturn = "FAILED: NSE EXC " + TC_name + ": " + str(nsee)
			# print(toReturn)
			return toReturn
		except Exception as e: 
			toReturn = "FAILED: EXC findelem mouse over: " + str(e)
			logging.error(toReturn)
			return toReturn
		
		actualResult = elem.get_attribute("title")
		
		# evalTest(expectedResult, actualResult)
		if expectedResult == actualResult:
			return "PASSED"
		return "FAILED: Result = " + str(actualResult)
	
	except Exception as ex:
		toReturn = "FAILED: EXC " + TC_name + ": " + str(ex)
		# print(toReturn)
		return toReturn
	return "PASSED"
