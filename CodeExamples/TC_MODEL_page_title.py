import logging 

def tc(URL, tc_name, ER, params): # -> String     KÖNNTE SO AUSSEHEN-...
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