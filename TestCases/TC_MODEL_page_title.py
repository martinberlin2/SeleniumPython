import logging 

tc_name = "TC_MODEL_page_title"
ER = "Home - auticon"

def tc(tc_name, ER, page): # -> bool
	print(tc_name)
	
	try:
		titel = page.title 
	except Exception as ex:
		ret = ("EXC " +  tc_name + ": " + str(ex))
		logging.error(ret)
		return ret

	if titel == ER:
		return "passed"
	return "Fail: Titel = " + titel