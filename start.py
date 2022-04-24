# Pfad Reporting manuell ändern - noch

# start für selenium python Test

# Erste Quelle https://www.selenium.dev/selenium/docs/api/py/api.html
# Zweite https://selenium-python.readthedocs.io/api.html

# git checkout zielbranch
# git merge branchderreinsoll

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
		# one_tc(tc_name)
	except Exception as ex:
		logging.error("EXC main level: " + str(ex))

def one_tc(tc_name): # returns: None; nur developen + debug
	
	from selenium import webdriver
	driverpath = config.get("gecko")
	driver = webdriver.Firefox(executable_path=driverpath)
		
	driver.get("https://auticon.de") 

	from TestCases import TC_1_1_popup_cookies_deny as testcase 
	result = testcase.tc(driver)
	print(tc_name + ": " + str(result))
	
	driver.quit()
	
	# reporter.addStats(passed, failed, errors)
	# reporter.closeReport()
	
def main():	# alle TC in /testcases
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
	print ("myroot = " + myroot)
	path = myroot + r'\TestCases'
	print ("path = " + path)
	ignorePath = path + '\__pycache__'
	# print("ignorePath: " + ignorePath)
	
	for root, directories, file in os.walk(path): # root = path 
		print("\nroot: " + str(root))

		## print("directories: " + str(directories))
		## print("file: " + str(file))

		for onefile in file: 
			if root != ignorePath:
				if(onefile.endswith(".py")):
					module_name = onefile[0:len(onefile)-3]
					module_name = root + "\\" + module_name    
						# läuft in Windows TODO ... Linux, Unix: Pfad erst umfummeln
					# print ("module_name = " + module_name) #  Pfad ohne .py
				
					module_name = module_name[len(myroot)+1: len(module_name)]
					module_name = module_name.replace("\\", ".", 100)

					print ("module_name = " + module_name) #  Pfad ohne .py
				#C:\Users\laoch\OneDrive\Dokumente\Meins\Eigenes_F\auticon\Python\SeleniumPython\TestCases\TC_1_1_popup_cookies_deny#
					
					## String befummeln: DONE 2.12.
					## myroot = C:\Users\laoch\OneDrive\Dokumente\Meins\Eigenes_F\auticon\Python\SeleniumPython
					## No module named 'C:\\Users\\laoch\\OneDrive\\Dokumente\\Meins\\Eigenes_F\\auticon\\Python\\SeleniumPython\\TestCases\\TC_1_1_popup_cookies_deny'
					## 1. StrAfterStr(str, startstr)     
					## 2. StrAfterStr(module_name, myroot) --> TestCases\TC_1_1_popup_cookies_deny
					## 3. replace \ -> .
					
					
					# module_name = "TestCases.TC_1_1_popup_cookies_deny"    # so gehts
					
					
					## von main()
					# module_name = "TestCases.TC_1_2_popup_openPositions"
					module = importlib.import_module(module_name, package=None) 
					result = module.tc(driver)
					
					# module_name = "root.dir.subdir." + module_name 
					# print(module_name)
					tc_name_parts = module_name.split(".", -1)
					tc_name = tc_name_parts[len(tc_name_parts) - 1]
					# tc_name = lastpart(module_name, ".")
					print(tc_name + ": " + str(result))
					if result == "Passed":
						passed = passed + 1
						reporter.report(tc_name, result, "")
					else:
						failed = failed + 1
						reporter.report(tc_name, "FAILED", result)
					
					
					# import modulename
					# result =  # TC_1_2_popup_openPositions
					# print(os.path.join(root,file))
			# else: print("ignorePath")	
	driver.close()
	driver.quit()
	reporter.addStats(passed, failed, errors)
	reporter.closeReport()
			
# execAllTestcases()	
start()

# def execFuncWithExc(functionName, args): # -> result, Exception given as String from Exception. functionName not in "" 
	# try:
		# result = functionName(*args)

