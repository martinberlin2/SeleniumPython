import logging 

def tc(driver): # -> bool
	
	tit = "Init"
	try:
		tit = driver.title 
	except Exception as ex:
		logging.error ("EXC TC_1_title: " + str(ex))
		return False
	if tit == "DB Fahrplan, Auskunft, Tickets, informieren und buchen - Deutsche Bahn":
		return True
	return False