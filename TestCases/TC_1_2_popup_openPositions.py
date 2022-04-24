

# Selenium / Python imports
import logging 
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.by import By
import time 

def tc(driver): # -> bool	
	TC = "TC_1_2_popup_openPositions" # TODO dynamisch - als Modulname
	## print(TC + " start")
	try:
		openPositionsAlertBox = driver.find_element(By.ID, 'popmake-41440')
	except NoSuchElementException  as nsex:
		logging.info(TC + ": NoSuchElementException")
		return TC + ": Popup kommt nicht"
	except Exception as ex:
		logging.error(TC + ": " + str(ex))
		return str(ex) 
	# hier: Kasten für Offene Stellen existiert
	text1 = openPositionsAlertBox.text
	expectString = "Wir stellen ein!\nIT- und BackOffice-Mitarbeiter*innen gesucht!\nMehr Infos\nX"
	if text1 != expectString:
		logging.info("TC_1_2_popup_openPositions: anderer Text:\n" + text1)
		return ("anderer Text:\n" + text1) ## ok
	
	X_Button = openPositionsAlertBox.find_element(By.CLASS_NAME, 'pum-close')
	X_Button.click()     # Fenster incl. Button verschwindet jetzt --- WAIT !
	time.sleep(1)  # braucht 1 sek, nicht 5 --- 18.11.
	try: 
		X_Button = openPositionsAlertBox.find_element(By.CLASS_NAME, 'pum-close')
		X_Button.click()
	except Exception as nsex:
		# logging.info(str(nsex))
		if str(nsex) == 'Message: Element <button class="pum-close popmake-close" type="button"> could not be scrolled into view\n':
			logging.info("TC_1_2_popup_openPositions PASSED X beendet Popup")
			return "Passed" # ok 
		logging.error("ERROR  --andere Exception TC_1_2_popup_openPositions:" + str(nsex))
		return "ERROR  --andere Exception TC_1_2_popup_openPositions:" + str(nsex) # ok
	logging.info("TC_1_2_popup_openPositions FAILED X beendet Popup NICHT")
	return "X beendet Popup NICHT"   # ok