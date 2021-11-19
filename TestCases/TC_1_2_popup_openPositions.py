

# Selenium / Python imports
import logging 
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.by import By
import time 
# Eigene Module  
from Utilities import Reporter as reporter


def tc(driver): # -> bool

	# reporter.report("TC1", str(True), "Laeuft")
	TC = "TC_1_2_popup_openPositions" # TODO dynamisch - als Modulname
	try:
		openPositionsAlertBox = driver.find_element(By.ID, 'popmake-41440')
		# openPositionsAlertBox = driver.find_element_by_id ( 'popmake-41440') # geht auch
	except NoSuchElementException  as nsex:
		logging.info("TC_1_2_popup_openPositions: NoSuchElementException ")
		result = "Failed"
		reason = "Popup kommt nicht "
		reporter
		return False ## ok
	except Exception as ex:
		logging.error("EXC TC1_2: " + str(ex))
		return False ## ok
	# hier: Kasten für Offene Stellen existiert
	text1 = openPositionsAlertBox.text
	expectString = "Wir stellen ein!\nIT- und BackOffice-Mitarbeiter*innen gesucht!\nMehr Infos\nX"
	if text1 != expectString:
		logging.info("TC_1_2_popup_openPositions: anderer Text:\n" + text1)
		return False ## ok
	## logging.info("TC_1_2_popup_openPositions PASSED Popup + Text ")
	
	X_Button = openPositionsAlertBox.find_element(By.CLASS_NAME, 'pum-close')
	## text2 = X_Button.text
	## print("text2 " + text2)
	X_Button.click()     # Fenster incl. Button verschwindet jetzt --- WAIT !
	time.sleep(1)  # braucht 1 sek, nicht 5 --- 18.11.
	try: 
		X_Button = openPositionsAlertBox.find_element(By.CLASS_NAME, 'pum-close')
		X_Button.click()
	except Exception as nsex:
		# logging.info(str(nsex))
		if str(nsex) == 'Message: Element <button class="pum-close popmake-close" type="button"> could not be scrolled into view\n':
			logging.info("TC_1_2_popup_openPositions PASSED X beendet Popup")
			return True # ok 
		logging.error("--andere Exception TC_1_2_popup_openPositions:" + str(nsex))
		return False # ok
	logging.info("TC_1_2_popup_openPositions FAILED X beendet Popup NICHT")
	return False   # ok