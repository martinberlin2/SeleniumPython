

# start für selenium python Test
# evalTC(3, "len1", execFuncWithExc(lcs, ["abc", "daf"]) ,[1,"a"]) 
# geht das in Selenium ?
# ----------- NKL - Lose von Mom

import logging
logging.basicConfig(filename= 'C:/Users/laoch/OneDrive/Dokumente/Meins/Eigenes_F/auticon/Python/SeleniumPython/Logs/log.txt', level=logging.INFO) 

	
def start():
	try:
		main()
	except Exception as ex:
		logging.info("EXC: " + str(ex))

def main():	
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	
	import time # import problem
	driverpath = "C:/Users/laoch/OneDrive/Dokumente/Meins/AndereProgramme_G/Work/Drivers/geckodriver.exe"
	driver = webdriver.Firefox(executable_path=driverpath)
		# https://stackoverflow.com/questions/49929374/notadirectoryerror-winerror-267-the-directory-name-is-invalid-error-while-inv
	# from selenium.common.exceptions import [TheNameOfTheExceptionClass]
	# sonst: erst schreiben, dann importe raussuchen
	
	driver.get("https://auticon.de") #  smoke test 
	# print(driver.title)
	import TC_1_title(driver)

	# zuletzt
	driver.close()
	 
start()