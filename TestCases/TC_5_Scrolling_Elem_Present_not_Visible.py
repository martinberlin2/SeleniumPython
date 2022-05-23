# TC_5_Scrolling_Elem_Present_not_Visible
# Desktop Modus, Vollbild und Teilbild 
# TC ist abhängig davon, dass die Popups weg sind
	# TC_1_1_popup_cookies_deny
	# TC_1_2_popup_openPositions	
# erstmal durch zufälliges Harness gelöst: TC_5_ ist letzter TC

# Selenium / Python imports
import logging 
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.by import By
import time 

def tc(driver): # -> bool
	TC = "TC_5_Scrolling_Elem_Present_not_Visible" # TODO dynamisch - als Modulname
	print(TC + " start")
	try:
		openPositionsAlertBox = driver.find_element(By.ID, 'popmake-41440')
	except NoSuchElementException  as nsex:
		logging.info(TC + ": NoSuchElementException")
		return TC + ": Popup kommt nicht"
	except Exception as ex:
		logging.error(TC + ": " + str(ex))
		return str(ex) 
	
	text1 = openPositionsAlertBox.text
	expectString = "Wir stellen ein!\nIT- und BackOffice-Mitarbeiter*innen gesucht!\nMehr Infos\nX"
	if text1 != expectString:
		logging.info(TC + ": anderer Text:\n" + text1)
		return ("anderer Text:\n" + text1)
	
	X_Button = openPositionsAlertBox.find_element(By.CLASS_NAME, 'pum-close')
	X_Button.click()     # Fenster incl. Button verschwindet jetzt --- WAIT !
	time.sleep(1)  # braucht 1 sek, nicht 5 --- 18.11.
	try: 
		X_Button = openPositionsAlertBox.find_element(By.CLASS_NAME, 'pum-close')
		X_Button.click()
	except Exception as nsex:
		# logging.info(str(nsex))
		if str(nsex) == 'Message: Element <button class="pum-close popmake-close" type="button"> could not be scrolled into view\n':
			logging.info(TC + ": PASSED X beendet Popup")
			return "Passed"
		logging.error("ERROR  --andere Exception " + TC + ":" + str(nsex))
		return "ERROR  --andere Exception " + TC + ":" + str(nsex)
	logging.info("" + TC + " FAILED X beendet Popup NICHT")
	return "X beendet Popup NICHT"