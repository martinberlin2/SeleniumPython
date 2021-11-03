import logging 
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.by import By

def tc(driver): # -> bool
	print("TC_1_2_popup_openPositions")
	try:
		openPositionsAlertBox = driver.find_element(By.ID, 'popmake-41440')
		# openPositionsAlertBox = driver.find_element_by_id ( 'popmake-41440') # geht auch
		# text = openPositionsAlertBox.text 
	except NoSuchElementException  as nsex:
		logging.info("TC_1_2_popup_openPositions: NoSuchElementException ")
		print("TC_1_2_popup_openPositions: NoSuchElementException ")
		return False
	except Exception as ex:
		print("EXC TC1_2: " + str(ex))
		return False
	# hier: Kasten für Offene Stellen existiert
	text1 = openPositionsAlertBox.text
	expectString = "Wir stellen ein!\nIT- und BackOffice-Mitarbeiter*innen gesucht!\nMehr Infos\nX"
	print(expectString)
	if text1 != expectString:
		print(text1)
		return False 
	return True
	
	
	# id= popmake-41440   Kasten für Offene Stellen
	
	# Schriftzug "Wir stellen ein":
	# div.pum-content:nth-child(1) > h2:nth-child(1) > strong:nth-child(1)
	
	
   # <button type="button" class="pum-close popmake-close" aria-label="Schließen">
 