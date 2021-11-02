import logging 
from selenium.common.exceptions import NoSuchElementException  

def tc(driver): # -> bool
	print("TC_1_2_popup_openPositions")
	try:
		print(driver.title)
	except Exception as ex:
		print("EXC TC1_2: " + str(ex))
		return False

	if driver.title == "Home - auticon":
		return True
	return False
	
	# id= popmake-41440   Kasten für Offene Stellen
	
	# Schriftzug "Wir stellen ein":
	# div.pum-content:nth-child(1) > h2:nth-child(1) > strong:nth-child(1)
	
	
	
   # <button type="button" class="pum-close popmake-close" aria-label="Schließen">
 