

# start für selenium python Test
# evalTC(3, "len1", execFuncWithExc(lcs, ["abc", "daf"]) ,[1,"a"]) 
# geht das in Selenium ?

import logging
from Utilities.readCfg import readConfig # as readConfig

config = readConfig("./config.txt")
SeleniumRoot = config.get("SeleniumRoot")
print(SeleniumRoot)

logging.basicConfig(filename= SeleniumRoot + '/Logs/log.txt', level=logging.INFO) 
	
def start():
	try:
		main()
	except Exception as ex:
		logging.error("EXC: " + str(ex))

def main():	
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
	print(result)
	
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
	
def execAllTestcases(): # alle TC in 
	import os
	myroot = config.get("SeleniumRoot")
	# path =r'C:\Users\laoch\OneDrive\Dokumente\Meins\Eigenes_F\auticon\Python\SeleniumPython\TestCases'
	for root, directories, file in os.walk(path): # root = path 
		print("root: " + str(root))
		print("directories: " + str(directories))
		print("file: " + str(file))
		for onefile in file:
			if root != path + '\__pycache__':
				if(onefile.endswith(".py")):
					print("file= " + onefile)
					# print(os.path.join(root,file))
					
execAllTestcases()	
# start()