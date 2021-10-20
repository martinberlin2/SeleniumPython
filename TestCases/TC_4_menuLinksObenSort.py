

# TC_4_menuLinksObenSort
import logging 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Äußeren Knoten kopieren

BurgerMenu: <i class="mob-icon-menu mob-menu-icon"></i>
klick ->
<ul id="mobmenuleft" role="navigation" aria-label="Main navigation for mobile devices">
... dann Liste als xpath oder Elems einzeln

def tc(driver): # -> bool
	logging.info("TC_4_menuLinksObenSort")
	try:
		elem = driver.find_elements(By.CLASS_NAME, 'Unsere Leistungen')		# no exc 
		#object of ActionChains
		actChainObj = ActionChains(driver)
		subelem = driver.find_element(By.XPATH, '//text()="Warum auticon"') # sollte failen
		actChainObj.move_to_element(elem).perform()    # mouse over 
		
		# subelem = driver.find_elements(By.  Warum auticon
		subelem = driver.find_element(By.XPATH, '//text()="Warum auticon"')
		
	except Exception as ex:
		print("EXC TC2: " + str(ex))
		return False

	return True

	