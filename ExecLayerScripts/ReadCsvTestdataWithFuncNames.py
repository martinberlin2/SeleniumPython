

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
script_filename = SeleniumRoot + r"\ExecLayerScripts\DDT_script.py"
if os.path.isfile(script_filename) == True:
	os.remove(script_filename)
# with open(script_filename, "a") as dd_script:
		# print("OutfileName:", outfile)
		# dd_script.write(line)

def run():
	LastLine = "Empty"
	with open(td_filename, newline='') as td, open(script_filename, "a") as dd_script:
		dd_script.write("\n\nData Driven Test Exec Script\n")
		testdata = csv.reader(td, delimiter = ";")
		TestcaseName = "Tinit"
		ExpectedResult = "Einit"
		params = "Pinit"
		ModuleName = "Minit"
		for row in testdata:
			# print(LastLine + "#" + str(row))
			if LastLine == "TestcaseName":
				TestcaseName = row[0]
				if TestcaseName == "":
					erg = "TestcaseName empty" # TODO line, file...
					# print (erg)
					LastLine = "Empty"
					continue 
				else:	
					ExpectedResult = row[1]  # darf leer sein
					c = 2
					params = []
					while c <= cols: # row[c] != "":
						print(str(row[c]))
						params.append(row[c])
						print("params: " + str(params))
						c = c + 1
					# cols = c - 1
					# while c <= cols:
						# print(row[c])
						# c = c + 1
						
			if LastLine == "ModuleName":
				TestcaseName = "init"
				ExpectedResult = "init"
				params = "init"
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
				params = []
				while row[c] != "":
					print(str(row[c]))
					params.append(row[c])
					print("params: " + str(params))
					c = c + 1
				cols = c - 1
				print ("cols = " + str(cols))
				# params = params + "]"
				# print ("cols gesetzt: " + str(cols))
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
				ModuleName = row[1]
				if header == "":
					erg = "Error functionName header" # TODO line, file...
					print (str(erg))
					return erg
				LastLine = "ModuleName"	
			dd_script.write(LastLine + " " + ModuleName + " " + TestcaseName + " " + ExpectedResult + " " + str(params) + "\n")
		print("---- Ende Testdata ----")
		return 
	# Ende with open(td_filename, newline='')

	# ExpectedResult	Param1	Param2
