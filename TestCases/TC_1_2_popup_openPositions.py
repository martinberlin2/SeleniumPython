import logging 
from selenium.common.exceptions import NoSuchElementException  

def tc(driver): # -> bool
	print("TC_1_title")
	try:
		print(driver.title)
	except Exception as ex:
		print("EXC TC1: " + str(ex))
		return False

	if driver.title == "Home - auticon":
		return True
	return False
	
   # <button type="button" class="pum-close popmake-close" aria-label="Schließen">
 