

# DIV

# Selenium / Python imports
import logging 

def tc(URL, ER, z, n): # -> String, Params: URL, ER, params
	TC = "DIV" # TODO dynamisch - als Modulname
	print(TC + " start")
	result = DIV(z,n)
	TC_result = "passed"
	if result != ER:
		TC_result = "Failed: result = " + str(result)
	return TC_result

#  under test
def DIV(z,n):
	if n == 0:
		return "Div by zero"
	return z/n
	
# Aufruf:
# import TestCases.DIV as TC 
# result = TC.tc(None, 3,15, 5)
# result = TC.tc(None, "Div by zero",15, 0)

# print(result)