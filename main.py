

# main für selenium python Test
# evalTC(3, "len1", execFuncWithExc(lcs, ["abc", "daf"]) ,[1,"a"]) 
# geht das in Selenium ?


def start():
	try:
		main()
	except Exception as ex:
		logging.info(str(ex))

def main():
	import logging
	logging.basicConfig(filename= './log.txt', level=logging.INFO)# , 
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	# from selenium.common.exceptions import [TheNameOfTheExceptionClass]
	# sonst: erst schreiben, dann importe raussuchen


	# zuletzt
	driver.close()
	