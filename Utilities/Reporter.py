# Fertig - committen und merge nach develop

# Reporter.py -- schreibt Testergebnis in /Reports/report.txt
# Testcase				Result		Reason

from os import stat  
from os import remove 
from os import path 
from Utilities.readCfg import readConfig 

config = readConfig("./config.txt")
SeleniumRoot = config.get("SeleniumRoot")

# f5 mit config 
reportfile = SeleniumRoot + '/Reports/Report.txt'

# reportfile = r'C:\Users\laoch\OneDrive\Dokumente\Meins\Eigenes_F\auticon\Python\SeleniumPython\Reports\Report.txt'

# reportfile = r'C:\Users\Lap126\Documents\auticon\Lern\Testautomatisierung\SeleniumPython\Reports\Report.txt'

TCnameLen = 30
resultLen = 10
reasonLen = 55

# geht; TODO : bei Aufruf von start ueber Config 
# reportfile = SeleniumRoot + '\Reports\Report.txt'

def openReport(): # legt ./Reports/report.txt an und Param: none; Returns: none; Error: ErrorString
	
	# # import stat
	# st = None
	# try:
		# st = stat(reportfile)
	# except(OSError):
		# print ("OSError" + str(st))  # Pfad passt nicht 
		# return
	# except Exception as ex:
		# print("Andere Exception os.stat: " + str(ex) + "--report=" + str(reportfile))
		# return 

	if path.isfile(reportfile) == True:
		remove(reportfile)
		# print("remove(reportfile)")
		
	with open(reportfile, "a") as reportFile:
		TCname = fillString("Testcase:", TCnameLen, " ")
		result = fillString("Result:", resultLen, " ")
		reason = fillString("Reason:", reasonLen, " ")
		line = TCname + " " + result + " " + reason
		reportFile.write(line + "\n")
		line = fillString("", TCnameLen + resultLen + reasonLen, "-")
		reportFile.write(line + "\n")
		

def closeReport(): # Summenbildung und schliesst den Report; Param: none; Returns: none; Error: ErrorString
	with open(reportfile, "a") as reportFile:
		# --Summenbildung
		reportFile.close()
		
def report(TCname, result, reason): # Param: String TCname, String result "Passed" or "FAILED" von Aufrufer, String reason; Returns: None; Error: ErrorString
	with open(reportfile, "a") as reportFile:
		TCname = fillString(TCname, TCnameLen, ".")
		result = fillString(result, resultLen, " ")
		reason = fillString(reason, reasonLen, " ")
		line = TCname + " " + result + " " + reason
		reportFile.write(line + "\n")
		
		
def fillString(s, nr, c): # Param: s String, nr auf wieviele Stellen auffüllen, c Character für Füllung; Returns: gefüllten String 
	s = str(s)  ## da kommt auch bool an ! 
	print("fillstring params: " + s + str(nr) + c)
	lens = len(s)
	while lens < nr:
		s=s+c
		lens = lens + 1
	return s 
	
def addStats(passed, failed, errors): # Param: Nr of TCs; errors = mistake is in TC programming 
	with open(reportfile, "a") as reportFile:
		line = fillString("", TCnameLen + resultLen + reasonLen, "=")
		print("+" + line + "+")
		reportFile.write(line + "\n")
		line = "Passed: " + str(passed) + ", Failed: " + str(failed) + ", Errors: " + str(errors)
		print("+" + line + "+")
		reportFile.write(line + "\n")
		
# openReport()
# report("TC1", str(True), "")
# report("TCFailed", str(False), "Geht gar nicht")
# closeReport()