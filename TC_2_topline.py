import logging 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# title="Unsere Leistungen" 
# menu-item-70
# class="">Unsere Leistungen

def tc(driver): # -> bool
	print("TC_2_topline")
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

	