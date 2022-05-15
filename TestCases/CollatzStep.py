

# CollatzStep

# Selenium / Python imports
import logging 

def tc(URL, ER, input): # -> String, Params: URL, ER, params
	TC = "CollatzStep" # TODO dynamisch - als Modulname
	print(TC + " start")
	result = CollatzStep(input)
	TC_result = "passed"
	if result != ER:
		TC_result = "Failed: result = " + str(result)
	return TC_result

#  under test
def CollatzStep(input):
	if isnaturalEven(input):
		return int(input / 2)
	return int(input * 3 + 1)
	
def isnaturalEven(x):
	if x % 2 == 0:
		return True
	return False

# Aufruf:
# import TestCases.CollatzStep as TC 
# result = TC.tc(None, 16,5)
# print(result)