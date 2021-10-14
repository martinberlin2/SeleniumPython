import logging 

print("TC_1_title")
try:
	print(driver.title)
except Exception as ex:
	print("EXC TC1: " + str(ex))
	return False

if driver.title == "Home - auticon":
	return True
return False
	