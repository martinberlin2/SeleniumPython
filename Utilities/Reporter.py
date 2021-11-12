

# Reporter.py -- schreibt Testergebnis in /Reports/report.txt
# Testcase				Result		Reason

from os import stat  
from os import remove 
from os import path 

# from Utilities.readCfg import readConfig # as readConfig
TCnameLen = 25
resultLen = 8
reasonLen = 55

reportfile = r'C:\Users\laoch\OneDrive\Dokumente\Meins\Eigenes_F\auticon\Python\SeleniumPython\Reports\Report.txt'
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
		
def report(TCname, result, reason): # Param: String TCname, String result, String reason; Returns: None; Error: ErrorString
	with open(reportfile, "a") as reportFile:
		TCname = fillString(TCname, TCnameLen, ".")
		result = fillString(result, resultLen, " ")
		reason = fillString(reason, reasonLen, " ")
		line = TCname + " " + result + " " + reason
		reportFile.write(line + "\n")
		
		
def fillString(s, nr, c): # Param: s String, nr auf wieviele Stellen auffüllen, c Character für Füllung; Returns: gefüllten String 
	lens = len(s)
	while lens < nr:
		s=s+c
		lens = lens + 1
	return s 
	
openReport()
report("TC1", str(True), "")
report("TCFailed", str(False), "Geht gar nicht")
closeReport()