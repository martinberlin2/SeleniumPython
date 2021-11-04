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
		return False
	except Exception as ex:
		logging.error("EXC TC1_2: " + str(ex))
		return False
	# hier: Kasten für Offene Stellen existiert
	text1 = openPositionsAlertBox.text
	expectString = "Wir stellen ein!\nIT- und BackOffice-Mitarbeiter*innen gesucht!\nMehr Infos\nX"
	if text1 != expectString:
		logging.info("TC_1_2_popup_openPositions: anderer Text:\n" + Text1)
		return False 
	logging.info("TC_1_2_popup_openPositions PASSED Popup + Text ")
	
	X_Button = openPositionsAlertBox.find_element(By.CLASS_NAME, 'pum-close')
	text2 = X_Button.text
	print("text2 " + text2)
	X_Button.click()
	sleep(5)
	try: 
		X_Button = openPositionsAlertBox.find_element(By.CLASS_NAME, 'pum-close')
	except NoSuchElementException as nsex:
		logging.info("TC_1_2_popup_openPositions PASSED X beendet Popup")
		return True
	logging.info("TC_1_2_popup_openPositions FAILED X beendet Popup NICHT")
	return False

	# Nur Klick auf X macht es weg, keine anderen Funktionen
	# button.pum-close:nth-child(2)

	# id= popmake-41440   Kasten für Offene Stellen
	
	# Schriftzug "Wir stellen ein":
	# div.pum-content:nth-child(1) > h2:nth-child(1) > strong:nth-child(1)
	
	
   # <button type="button" class="pum-close popmake-close" aria-label="Schließen">
 