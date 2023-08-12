

# Helper.py 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def expand_shadow_element(drv, element): # -> shadow_root: returns tree under element = das ueber shadow open in HTML
	shadow_root = drv.execute_script('return arguments[0].shadowRoot', element)
	# shadow_root = drv.execute_script('return arguments[0].shadowRoot.firstChild', element)
	return shadow_root

def isNotVisible(driver, cssSelector, seconds): # cssSelector weg nach max seconds -- für Promise-Lösung: verschwindet Elem nach seconds, z.B. nach click) ?; # sehr genau, bei 0.20000000000000004 False bei seconds = 0.2
	s = 0
	step = 0.01
	while s < seconds:
		try:
			elem = WebDriverWait(driver, step).until(
			EC.visibility_of_element_located((By.CSS_SELECTOR, cssSelector)))
		except Exception as ex:
			# print ("TRUE elem invisible after seconds " + str(s) + " " + str(ex))
			return True   
		# print(str(s))
		s = s + step
	# print ("FALSE elem still visible after seconds " + str(s))
	return False 

def getElem(driver, mode, timeout, cssSelector): # -> (seconds, elem, msg) : cssSelector available after seconds with errors = msg (none = "NoErrors"), returns elem, too. mode: "e" = existence, "v" = visibility (NYI), "c" = clickability
	import time 
	from datetime import datetime, timedelta
					# time.sleep(20) 
	print("getElem " + str(timeout))
	msg = "NoErrors"
	start = datetime.now()
	print("start done: " + str(start))
					# print(start)
					# return 10, None, msg
	finishplan = start + timedelta(seconds=timeout)
	# print("finishplan: " + str(finishplan))
	# return 99, None, msg
	#### elem = None    # muss das ?
	# step = timeout/100
	while datetime.now() <= finishplan:
		match mode:
			case "e": # Läuft auch ohne WebDriverWait, mit shadowDom
			# if mode == "e":
				try:
					elems = driver.find_elements(By.CSS_SELECTOR,cssSelector)
					print(msg + " " + str(len(elems)))
					neededSecs = datetime.now() - start
					msg = "getElem: Element found after seconds: " + str(neededSecs)
					if len(elems) > 1:
						msg = msg + " MORE elems found !"
					print(msg)
					for elem in elems:
						print(elem.text)
					return neededSecs, elems[0], msg
				except Exception as ex:
					dummy = "must have a statement here"
					# print ("no elem exists, seconds " + str(datetime.now() - start) + " " + str(ex))
			case "c":
			# elif mode == "c":
				try:
					# wird Parameter cssSelector:
					# cssSelector = "button.btn:nth-child(1)"
					cssSelector = ".js-accept-essential-cookies"
					elem = WebDriverWait(driver, step).until(
					EC.element_to_be_clickable((By.CSS_SELECTOR, cssSelector)))
					msg = "getElem: Element clickable return"
					print(msg)
					return datetime.now() - start, elem, msg
				except Exception as ex:
					print ("no elem clickable, seconds " + str(datetime.now() - start) + " " + str(ex))
				# except Exception as ex:
					# print("Other Exception: " + str(ex))
				if elem != None:
					msg = "getElem: Element clickable --- dead code ??"
					print(msg)
					return datetime.now() - start, elem, msg
			case _:
			# else: 
				msg = "Wrong parameter for mode"
				print (msg)
				return None, None, msg
	msg = "getElem: Element NOT found"
	print (msg)
	return datetime.now() - start, elem, msg

			