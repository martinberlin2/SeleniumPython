

# TC_4_menuLinksObenSort
import logging 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Äußeren Knoten kopieren

# BurgerMenu: <i class="mob-icon-menu mob-menu-icon"></i>
# klick ->
# <div class="mob-menu-left-bg-holder"></div> muss existieren
# <ul id="mobmenuleft" role="navigation" aria-label="Main navigation for mobile devices">
# ... TODO dann Liste als xpath oder Elems einzeln

# ----

def tc(driver): # -> bool
	logging.info("TC_4_menuLinksObenSort deaktiviert")
	return "at the moment disabled, has never worked yet"
	try:
		burger = driver.find_elements(By.CLASS_NAME, 'mob-icon-menu')		
		#object of ActionChains
		actChainObj = ActionChains(driver)
		burger.click()
		subelem = driver.find_elements(By.CLASS_NAME, 'mob-menu-left-bg-holder')
		subelem.click()   # -- NPE ?
		# --> ERROR:root:EXC TC4: 'list' object has no attribute 'click'
	except Exception as ex:
		logging.error("EXC TC4: " + str(ex))
		return False

	return True

	