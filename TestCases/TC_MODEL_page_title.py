import logging 

def tc(driver): # -> bool
	tc_name = "TC_MODEL_page_title"
	## print(tc_name)
	try:
		tit = driver.titlex 
	except Exception as ex:
		logging.error ("EXC " +  tc_name + ": " + str(ex))
		return False

	if driver.title == "Home - auticon":
		return True
	return False