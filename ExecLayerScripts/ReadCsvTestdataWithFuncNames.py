

	# https://docs.python.org/3/library/csv.html#reader-objects
	
import csv # finder reader nicht
from Utilities.readCfg import readConfig 
config = readConfig("./config.txt")
SeleniumRoot = config.get("SeleniumRoot")
script_filename = SeleniumRoot + r"\ExecLayerScripts\DDT_script.py"

import os.path
if os.path.isfile(script_filename) == True:
	os.remove(script_filename)
	
# SeleniumRoot = r"D:\Travel\SeleniumPython"   # ReiseLab
## print("SeleniumRoot = " + SeleniumRoot) 

# ModuleName;Testcases.CollatzStep
# TestcaseName;ExpectedResult;Param1;;
# Odd1;16;5;;
# Odd2;4;1
# Even1;16;8;;
# Even2;5;10;;


def run():
# TODO Für alle .py as aktPy in Execution List: # daher td_filename
	aktTC = SeleniumRoot + r"\TestCases\CollatzStep"
	td_filename = SeleniumRoot + r"\TestCases\CollatzStep_Testdata.csv"
	# if not exist, normal TC 
	print (str(td_filename))
	with open(td_filename, newline='') as td, open(script_filename, "a") as dd_script:
		testdata = csv.reader (td, delimiter = ";")
		if csv == None:
			print("if csv == None:")
		# existTestdata() ; nein -> cols = 0, ja -> cols = 1
		ModuleName = "Testcases.CollatzStep"
		dd_script.write("\n\n# Data Driven Test Exec Script\n")
		dd_script.write("\nimport " + ModuleName + " as TC  \n")
		# testdata = csv.reader(td, delimiter = ";")
		# csv.reader(csvfile, dialect='excel', **fmtparams)
		rows = 1
		for row in testdata:
			if rows > 2:
				print(row[0] + "\n")
				if row[0] == None: # "":
					print("## Ende ## + row[0]")
					break
				out  = "exec(" + ModuleName + ".tc, ["
				# wenn Testdaten: if existTestdata()
				c = 0
				while c < cols:
					out = out + ", " + str(row[c])
					c=c+1	
				out = out + "])"
				dd_script.write(out + "\n")
			if rows == 2:
				cols = 0
				while row[cols] != "":
					# print(row[cols] + "\n")
					cols = cols + 1
				# cols = cols - 1
				rows = rows + 1
			if rows == 1:
				rows = rows + 1
		# script_filename.close 
