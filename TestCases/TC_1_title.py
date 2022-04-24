import logging 

def tc(driver): # -> bool
	print("TC_1_title")
	try:
		print(driver.title)
	except Exception as ex:
		print("EXC TC_1_title: " + str(ex))
		return False

	if driver.title == "Home - auticon":
		return True
	return False