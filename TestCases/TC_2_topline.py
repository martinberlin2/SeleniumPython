

import logging 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# TC ist abhängig davon, dass die Popups weg sind
	# TC_1_1_popup_cookies_deny
	# TC_1_2_popup_openPositions
# -- TODO Blocked TC einführen?



# title="Unsere Leistungen" 
# menu-item-70
# class="">Unsere Leistungen

def tc(driver): # -> bool
	print("TC_2_topline - Mouse over")
	elem_unsereLeistungenText = None
	try:
		elem_unsereLeistungenText = driver.find_element(By.CSS_SELECTOR, '.vc_custom_1542025788808 > figure:nth-child(1) > a:nth-child(1) > img:nth-child(1)' ) 
	except Exception as e:
		print("EXC findelem mouse over: " + str(e))
		return False
	# .vc_custom_1542025788808 > figure:nth-child(1) > a:nth-child(1) > img:nth-child(1)
	
	try:
		#object of ActionChains
		actChainObj = ActionChains(driver)
		actChainObj.move_to_element(elem_unsereLeistungenText).perform()    # mouse over 
		# action = webdriver.ActionChains(driver)
		# element = driver.find_element_by_id('your-id') # or your another selector here
		# action.move_to_element(element)
		# action.perform()
		
	
	except Exception as ex:
		print("EXC TC2: " + str(ex))
		return False

	return True
	
	# TC_2_topline
# EXC TC2: Message: Given xpath expression "//text()="Warum auticon"" is invalid: TypeError: Document.evaluate: Result type mismatch

# TC_2_topline: False

	