import logging 
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.by import By
import time 

def tc(driver): # -> bool
	try:
		openPositionsAlertBox = driver.find_element(By.ID, 'popmake-41440')
		# openPositionsAlertBox = driver.find_element_by_id ( 'popmake-41440') # geht auch
		# text = openPositionsAlertBox.text 
	except NoSuchElementException  as nsex:
		logging.info("TC_1_2_popup_openPositions: NoSuchElementException ")
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
	X_Button.click()     # Fenster incl. Button verschwindet jetzt
	# time.sleep(5)
	try: 
		X_Button = openPositionsAlertBox.find_element(By.CLASS_NAME, 'pum-close')
		X_Button.click()
		# time.sleep(5)
	except Exception as nsex:
		logging.info(str(nsex))
		if str(nsex) == ' Message: Element <button class="pum-close popmake-close" type="button"> could not be scrolled into view\n':
			logging.info("TC_1_2_popup_openPositions PASSED X beendet Popup")
		return True  ## ok
		logging.error("--andere Exception TC_1_2_popup_openPositions:" + str(nsex))
	logging.info("TC_1_2_popup_openPositions FAILED X beendet Popup NICHT")
	return False ## ok 

	# Nur Klick auf X macht es weg, keine anderen Funktionen
	# button.pum-close:nth-child(2)

	# id= popmake-41440   Kasten für Offene Stellen
	
	# Schriftzug "Wir stellen ein":
	# div.pum-content:nth-child(1) > h2:nth-child(1) > strong:nth-child(1)
	
	
   # <button type="button" class="pum-close popmake-close" aria-label="Schließen">
 