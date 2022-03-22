

# start für selenium python Test
# evalTC(3, "len1", execFuncWithExc(lcs, ["abc", "daf"]) ,[1,"a"]) 
# geht das in Selenium ?

import logging
from Utilities.readCfg import readConfig # as readConfig
import Utilities.Reporter as reporter
import importlib

config = readConfig("./config.txt")
SeleniumRoot = config.get("SeleniumRoot")
# print(SeleniumRoot)

logging.basicConfig(filename= SeleniumRoot + '/Logs/log.txt', level=logging.INFO) 
	
def start(): # collects unexpected exceptions from main 
	try:
		execAllTestcases()
	except Exception as ex:
		logging.error("EXC: " + str(ex))

def main():	
	passed = 0
	failed = 0
	errors = 0
	reporter.openReport()
	print("Reporter.openReport()")
	# reporter.report("TC1", str(True), "Laeuft")
	# reporter.report("TCFailed", str(False), "Geht gar nicht")
	passed = 4
	failed = 2
	errors = 1
	# reporter.addStats(passed, failed, errors)
	# reporter.closeReport()
	# return 
	
	
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	
	import time 
	driverpath = config.get("gecko")
	driver = webdriver.Firefox(executable_path=driverpath)
		# https://stackoverflow.com/questions/49929374/notadirectoryerror-winerror-267-the-directory-name-is-invalid-error-while-inv
		 
	driver.get("https://auticon.de") 
	## driver = None

	# from TestCases import TC_1_title as testcase 
	# result = testcase.tc(driver)
	# print(result)
	
	# from TestCases import TC_1_1_popup_cookies_deny as testcase # am worklab: f1
	# result = testcase.tc(driver)
	# print(result)
	
	import importlib
	module_name = "TestCases.TC_1_2_popup_openPositions"
	module = importlib.import_module(module_name, package=None) 
	result = module.tc(driver)
	module_name = "root.dir.subdir." + module_name 
	print(module_name)
	tc_name_parts = module_name.split(".", -1)
	tc_name = tc_name_parts[len(tc_name_parts) - 1]
	# tc_name = lastpart(module_name, ".")
	print(tc_name + ": " + result)
	if result == "Passed":
		passed = passed + 1
		reporter.report(tc_name, result, "")
	else:
		failed = failed + 1
		reporter.report(tc_name, "FAILED", result)
	
	
	# from TestCases import TC_1_2_popup_openPositions as testcase # home: f2 -- Merged
	# result = testcase.tc(driver)
	# print(result)

	# from TestCases import TC_2_topline as testcase 
	# result = testcase.tc(driver)
	# print(result)
	
	# from TestCases import TC_4_menuLinksObenSort as testcase 
	# result = testcase.tc(driver)
	# print(result)
	
	driver.close()
	driver.quit()
	reporter.addStats(passed, failed, errors)
	reporter.closeReport()
	
def execAllTestcases(): # alle TC in 
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	
	import time 
	driverpath = config.get("gecko")
	driver = webdriver.Firefox(executable_path=driverpath)
	# https://stackoverflow.com/questions/49929374/notadirectoryerror-winerror-267-the-directory-name-is-invalid-error-while-inv	 
	driver.get("https://auticon.de") 
	passed = 4
	failed = 2
	errors = 1
	import os
	myroot = config.get("SeleniumRoot")
	print ("myroot = " + myroot)
			# path =r'C:\Users\laoch\OneDrive\Dokumente\Meins\Eigenes_F\auticon\Python\SeleniumPython\TestCases'
			# print ("path = " + path)
	path = myroot + r'\TestCases'
	print ("path = " + path)
	ignorePath = path + '\__pycache__'
	# print("ignorePath: " + ignorePath)
	for root, directories, file in os.walk(path): # root = path 
		print("\nroot: " + str(root))
		print("directories: " + str(directories))
		print("file: " + str(file))
		for onefile in file: 
			if root != ignorePath:
				if(onefile.endswith(".py")):
					# print("file= " + onefile)
					module_name = onefile[0:len(onefile)-3]
					module_name = root + "\\" + module_name    # läuft in Windows TODO ... Linux, Unix: Pfad erst umfummeln
					print ("module_name = " + module_name) #  Pfad ohne .py
					
					# String befummeln:
					# myroot = C:\Users\laoch\OneDrive\Dokumente\Meins\Eigenes_F\auticon\Python\SeleniumPython
					# No module named 'C:\\Users\\laoch\\OneDrive\\Dokumente\\Meins\\Eigenes_F\\auticon\\Python\\SeleniumPython\\TestCases\\TC_1_1_popup_cookies_deny'
					
					
					# module_name = "TestCases.TC_1_1_popup_cookies_deny"    # so gehts
					
					
					## von main()
					# module_name = "TestCases.TC_1_2_popup_openPositions"
					module = importlib.import_module(module_name, package=None) 
						# No module named 'C:\\Users\\laoch\\OneDrive\\Dokumente\\Meins\\Eigenes_F\\auticon\\Python\\SeleniumPython\\TestCases\\TC_1_1_popup_cookies_deny'
					
					result = module.tc(driver)
					return
					# module_name = "root.dir.subdir." + module_name 
					# print(module_name)
					tc_name_parts = module_name.split(".", -1)
					tc_name = tc_name_parts[len(tc_name_parts) - 1]
					# tc_name = lastpart(module_name, ".")
					print(tc_name + ": " + result)
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
			
execAllTestcases()	
# start()

# def execFuncWithExc(functionName, args): # -> result, Exception given as String from Exception. functionName not in "" 
	# try:
		# result = functionName(*args)