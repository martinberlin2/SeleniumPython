

# start für selenium python Test
# evalTC(3, "len1", execFuncWithExc(lcs, ["abc", "daf"]) ,[1,"a"]) 
# geht das in Selenium ?
# Erste Quelle https://www.selenium.dev/selenium/docs/api/py/api.html
# Zweite https://selenium-python.readthedocs.io/api.html

import logging
from Utilities.readCfg import readConfig # as readConfig
import Utilities.Reporter as reporter
import importlib

config = readConfig("./config.txt")
SeleniumRoot = config.get("SeleniumRoot")
# print(SeleniumRoot)

logging.basicConfig(filename= SeleniumRoot + '/Logs/log.txt', level=logging.INFO) 
# print("kommt hier hin")
	
	
def start(): # collects unexpected exceptions from main 
	# print("Started")
	try:
		main()
	except Exception as ex:
		logging.error("EXC main level: " + str(ex))

def main():	
	
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	
	# import time 
	driverpath = config.get("gecko")
	driver = webdriver.Firefox(executable_path=driverpath)
		# https://stackoverflow.com/questions/49929374/notadirectoryerror-winerror-267-the-directory-name-is-invalid-error-while-inv
		 
	driver.get("https://auticon.de") 
	from TestCases import TC_1_1_popup_cookies_deny as testcase # am worklab: f1
	result = testcase.tc(driver)
	print("TC_1_1_popup_cookies_deny: " + str(result))

	from TestCases import TC_1_2_popup_openPositions as testcase # am worklab: f1
	result = testcase.tc(driver)
	print("TC_1_2_popup_openPositions: " + str(result))

	
	from TestCases import TC_2_topline as testcase # am worklab: f1
	result = testcase.tc(driver)
	print("Done - TC_2_topline - Mouse over: " + str(result))

start()