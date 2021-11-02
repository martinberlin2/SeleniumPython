

# start für selenium python Test
# evalTC(3, "len1", execFuncWithExc(lcs, ["abc", "daf"]) ,[1,"a"]) 
# geht das in Selenium ?

import logging
from Utilities.readCfg import readConfig # as readConfig

config = readConfig("./config.txt")
# config.showAll()
SeleniumRoot = config.get("SeleniumRoot")
print(SeleniumRoot)

# home pc
# logging.basicConfig(filename= 'C:/Users/laoch/OneDrive/Dokumente/Meins/Eigenes_F/auticon/Python/SeleniumPython/Logs/log.txt', level=logging.INFO) 

# work lab
# logging.basicConfig(filename='C:/Users/Lap126/Documents/auticon/Lern/Testautomatisierung/SeleniumPython/Logs/log.txt', level=logging.INFO) 

# mit Config
logging.basicConfig(filename= SeleniumRoot + '/Logs/log.txt', level=logging.INFO) 
	
def start():
	try:
		main()
	except Exception as ex:
		logging.info("EXC: " + str(ex))

def main():	
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	
	import time # import problem
	# driverpath = "C:/Users/laoch/OneDrive/Dokumente/Meins/AndereProgramme_G/Work/Drivers/geckodriver.exe"
	driverpath = config.get("gecko")
	driver = webdriver.Firefox(executable_path=driverpath)
		# https://stackoverflow.com/questions/49929374/notadirectoryerror-winerror-267-the-directory-name-is-invalid-error-while-inv
	# from selenium.common.exceptions import [TheNameOfTheExceptionClass]
	# sonst: erst schreiben, dann importe raussuchen
	
	## driver = None
	driver.get("https://auticon.de") #  smoke test 
	# print(driver.title)
	# folder = Path('./TestCases')  # --- Unterverz für Python 
	
	## from TC_2_topline import tc
	
	# from TestCases import TC_1_title as testcase 
	# result = testcase.tc(driver)
	# print(result)
	# result in Log 
	# 
	
	# from TestCases import TC_1_1_popup_cookies_deny as testcase # am worklab: f1
	# result = testcase.tc(driver)
	# print(result)
	
	from TestCases import TC_1_2_popup_openPositions as testcase # am worklab: f2
	result = testcase.tc(driver)
	print(result)
	
	# from TestCases import TC_2_topline as testcase 
	# result = testcase.tc(driver)
	# print(result)
	
	# from TestCases import TC_4_menuLinksObenSort as testcase 
	# result = testcase.tc(driver)
	# print(result)
	
	# zuletzt
	driver.close()
	driver.quit()
	 
start()