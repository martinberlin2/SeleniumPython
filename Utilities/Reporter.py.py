

# Reporter.py -- schreibt Testergebnis in /Reports/report.txt
# Testcase				Result		Reason
import os.path as path
TCnameLen = 25
resultLen = 10
reasonLen = 55


def openReport(): # legt ./Reports/report.txt an und Param: none; Returns: none; Error: ErrorString
	report = './Reports/report.txt'
	if os.path.isfile(report) == True:
		os.remove(report)
		print("os.remove(report)")
		
	with open(report, "a") as reportFile:
		TCname = fillString("Testcase:", TCnameLen, ".")
		result = fillString("Result:", resultLen, ".")
		reason = fillString("Reason:", reasonLen, ".")
		line = "TCname + result + reason\n\n"
		reportFile.write(line)

def closeReport(): # Summenbildung und schliesst den Report; Param: none; Returns: none; Error: ErrorString
		report = './Reports/report.txt'
		with open(report, "a") as reportFile:
			--Summenbildung
			reportFile.close()
		
def report(TCname, result, reason): # Param: String TCname, Bool result, String reason; Returns: None; Error: ErrorString
	report = './Reports/report.txt'
	if os.path.isfile(report) == True:
		os.remove(report)
		print("os.remove(report)")
	
	with open(report, "a") as reportFile:
		TCname = fillString(TCname, TCnameLen, ".")
		result = fillString(result, resultLen, ".")
		reason = fillString(reason, reasonLen, ".")
		line = "TCname + result + reason\n\n"
		reportFile.write(line)
		
		
def fillString(s, nr, c): # Param: s String, nr auf wieviele Stellen auffüllen, c Character für Füllung; Returns: gefüllten String 
	