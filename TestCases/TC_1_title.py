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
	
   # <button type="button" class="pum-close popmake-close" aria-label="Schließen">
   
   # <a class="_brlbs-btn _brlbs-cursor" href="#" tabindex="0" role="button" data-cookie-refuse="">
   # Nur essenzielle Cookies akzeptieren                                        </a>

# driver = None
# tc(driver)