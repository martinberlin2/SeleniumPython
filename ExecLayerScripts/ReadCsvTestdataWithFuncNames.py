

	# ReadAndWriteCSV
	# https://docs.python.org/3/library/csv.html#reader-objects

	# C:\Users\laoch\OneDrive\Dokumente\Meins\Eigenes_F\auticon\Python\SeleniumPython\TestData
	# DD_Testdata.csv 
import csv

from Utilities.readCfg import readConfig 
config = readConfig("./config.txt")
SeleniumRoot = config.get("SeleniumRoot")

# SeleniumRoot = r"D:\Travel\SeleniumPython"   # ReiseLab
## print("SeleniumRoot = " + SeleniumRoot) 
td_filename = SeleniumRoot + r"\TestData\DD_Testdata.csv"
## print (str(td_filename))

import os.path
script_filename = SeleniumRoot + r"ExecLayerScripts/DDT_script.py"
if os.path.isfile(dd_script_filename) == True:
	os.remove(dd_script_filename)
# with open(dd_script_filename, "a") as dd_script:
		# print("OutfileName:", outfile)
		# dd_script.write(line)

def run():
	outstring = ""
	LastLine = "Empty"
	with open(td_filename, newline='') as td, open(dd_script_filename, "a") as dd_script:
		testdata = csv.reader(td, delimiter = ";")
		for row in testdata:
			print(LastLine + "#" + str(row))
			if LastLine == "TestcaseName":
				TestcaseName = row[0]
				if TestcaseName == "":
					erg = "TestcaseName empty" # TODO line, file...
					print (erg)
					LastLine = "Empty"
					continue 
				else:	
					ExpectedResult = row[1]  # darf leer sein
					c=2
					while c <= cols:
						print(row[c])
						c = c + 1
			if LastLine == "ModuleName":
				header = row[0]
				if header != "TestcaseName": 
					erg = "Error TestcaseName header" # TODO line, file...
					print (erg)
					return erg
				header = row[1]
				if header != "ExpectedResult": 
					erg = "Error ExpectedResult header" # TODO line, file...
					print (erg)
					return erg
				c = 2
				while row[c] != "":
					print(row[c])
					c = c + 1
				cols = c - 1
				print ("cols gesetzt: " + str(cols))
				LastLine = "TestcaseName"
			if LastLine == "Empty" :
				header = row[0]
				if header == "":
					print ("--- Ende Testdata ---")
					break
				if header != "ModuleName": 
					erg = "Error ModuleName header" # TODO line, file...
					print (erg)
					return erg
				header = row[1]
				if header == "":
					erg = "Error functionName header" # TODO line, file...
					print (erg)
					return erg
				LastLine = "ModuleName"	
		print("---- Ende Testdata ----")
		return 
	# Ende with open(td_filename, newline='')

	# ExpectedResult	Param1	Param2
