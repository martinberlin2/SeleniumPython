# Pfad Reporting manuell ändern - noch

# Start für Selenium python Test

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
	
def start(): # collects unexpected exceptions from main 
	# print("Started")
	try:
		reporter.openReport()
		main()  # startet nacheinander alle TC in /testcases, rekursiv; kein Harness
		# one_tc()
	except Exception as ex:
		logging.error("EXC main level: " + str(ex))

def one_tc(): # returns: None; nur developen + debug
	from selenium import webdriver
	driverpath = config.get("gecko")
	driver = webdriver.Firefox(executable_path=driverpath)
		
	driver.get("https://auticon.de") 
	from TestCases import TC_1_1_popup_cookies_deny as testcase 
	result = testcase.tc(driver)
	print(tc_name + ": " + str(result))
	
	driver.quit()
	
	reporter.addStats(passed, failed, errors)
	reporter.closeReport()
	
def main():	# alle TC in /testcases, rekursiv
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	
	import time 
	driverpath = config.get("gecko")
	driver = webdriver.Firefox(executable_path=driverpath)
	# https://stackoverflow.com/questions/49929374/notadirectoryerror-winerror-267-the-directory-name-is-invalid-error-while-inv	 
	driver.get("https://auticon.de") 
	passed = 0
	failed = 0
	errors = 0
	import os
	import importlib 
	myroot = config.get("SeleniumRoot")
					## print ("myroot = " + myroot)
	path = myroot + r'\TestCases'
					## print ("path = " + path)
	ignorePath = path + '\__pycache__'
					## print("ignorePath: " + ignorePath)
	
	for root, directories, file in os.walk(path): # root = path 
					## print("\nroot: " + str(root))
					## print("directories: " + str(directories))
					## print("file: " + str(file) + " jetztReturn\n")   ## alle Dateien 

		for onefile in file: 
			if root != ignorePath:
				if(onefile.endswith(".py")):
					module_name = onefile[0:len(onefile)-3]
					module_name = root + "\\" + module_name    
									# läuft in Windows TODO ... Linux, Unix: Pfad erst umfummeln
									# print ("module_name = " + module_name) #  Pfad ohne .py
				
					module_name = module_name[len(myroot)+1: len(module_name)]
					module_name = module_name.replace("\\", ".", 100)

									# print ("module_name = " + module_name + "\n") #  Pfad ohne .py, das wird verwendet
				
					## String befummeln: DONE 2.12. usw Gelöscht 19.5.
					
					# module_name = "TestCases.TC_1_1_popup_cookies_deny"    # so gehts
					module = importlib.import_module(module_name, package=None) 
					if module_name != "TestCases.Mouse_over_-_Tooltip_von_title" :
						print ("module_name = " + module_name + "\n") 
						result = module.tc(driver)
					
					tc_name_parts = module_name.split(".", -1)
					tc_name = tc_name_parts[len(tc_name_parts) - 1]
					# print(tc_name + ": " + str(result))
					if result == "Passed":
						passed = passed + 1
						reporter.report(tc_name, result, "")
					else:
						failed = failed + 1
						reporter.report(tc_name, "FAILED", result)
					
					
	
	# +++++++++++++++ nachgeschobener TC ++++++++++++++
	module_name = "TestCases.Mouse_over_-_Tooltip_von_title"
	try:
		module = importlib.import_module(module_name, package=None) 
	except BaseException as be:
		print("TestCases.Mouse_over_-_Tooltip_von_title " + str(be))
	
	result = module.tc(driver)
	print(module_name + ": " + str(result) +"\n")
	
	tc_name_parts = module_name.split(".", -1)
	tc_name = tc_name_parts[len(tc_name_parts) - 1]
	# print(tc_name + ": " + str(result))
	if result == "Passed":
		passed = passed + 1
		reporter.report(tc_name, result, "")
	else:
		failed = failed + 1
		reporter.report(tc_name, "FAILED", result)
	# +++++++++++++++ nachgeschobener TC Ende ++++++++++++++
	driver.close()
	driver.quit()
	reporter.addStats(passed, failed, errors)
	reporter.closeReport()
			
# execAllTestcases()	
start()

# so in meinem Python-Unit-Test:
# def execFuncWithExc(functionName, args): # -> result, Exception given as String from Exception. functionName not in "" 
	# try:
		# result = functionName(*args)