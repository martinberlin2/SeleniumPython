

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
pfadfile = r"\TestData\DD_Testdata.csv"
td_filename = SeleniumRoot + pfadfile
## print (str(td_filename))

def run():
	params = howManyParams()
	readAll(params)
	
	
	LastLine = "Empty"
	with open(td_filename, newline='') as f:
		testdata = csv.reader(f, delimiter = ";")
		for row in testdata:
			print(LastLine + "#" + str(row))
			if LastLine == "ModuleName":
				if row[0] == "":
					erg = "Error in testdata" # TODO line, file...
					print (erg)
					return erg
				TestcaseName = row[1]
				if TestcaseName == "": 
					erg = "Empty TestcaseName" # TODO line, file...
					print (erg)
					return erg
				ExpectedResult = row[2]
				if ExpectedResult == "": 
					erg = "Empty ExpectedResult" # TODO line, file...
					print (erg)
					return erg
				
				
				LastLine = "TestcaseName"
			
			
			
			
			if LastLine == "Empty" :
				if row[0] == "":
					print ("--- Ende Testdata ---")
					break
				if row[0] != "ModuleName": 
					erg = "Error in testdata" # TODO line, file...
					print (erg)
					return erg
				ModuleName = row[1]
				if ModuleName == "": 
					erg = "Empty ModuleName" # TODO line, file...
					print (erg)
					return erg
				LastLine = "ModuleName"
			
			
			
			c = 2
			while c < numOfParams + 2:
				print(row[c])
				c = c + 1
			print("-------")
		print("---- Ende Testdata ----")
	
	
	# ddtc_exec.py öffnen
	nextMod = getNextModule() # "" oder Modulname
	while nextMod != "":
		next = processTC(nextMod) # TC Daten lesen + schreiben; 
		nextMod = getNextModule()
		
# def getNextModule():
	
		

# def processTC(nextMod): 
	# howManyParams()   # naechste Zeile
	# für jede Zeile : Schreiben in ddtc_exec.py

	
def isLineEmpty(numOfParams, line): 
	i = 0
	while i < numOfParams + 2:
		if line[i] != "":
			return False
		i = i + 1
	return True
	
	
	
def readAll(numOfParams):
	# pfadhome = r"C:\Users\laoch\OneDrive\Dokumente\Meins\Eigenes_F\auticon\Python\SeleniumPython"
	with open(td_filename, newline='') as f:
		testdata = csv.reader(f, delimiter = ";")
		for row in testdata:
			# print("row read")
			print(str(row))
			## print (row[2])  # 0-index
			# if isLineEmpty(numOfParams, row):
				# print("Leerzeile erkannt")
				# break
			c = 2
			while c < numOfParams + 2:
				print(row[c])
				c = c + 1
			print("-------")
		print("---- Ende Testdata ----")
			
	for testdata:
	row = readLine  # leer, Headers, Data
	LOOP
		if row[0] != "ModuleName": Error
		ModuleName == row[1]
		if ModuleName == "": Error
		readLine
		if row[0] != "TestcaseName": Error
		cols = 0
		while row[cols] != "":
			cols = cols + 1
		if cols < 3: "Error? No Parameters, why data driven?"
		readLine
		while row[0] != "":
			processTestdata
			readLine
		
	# endloop
			

		
	# wieviele Header
def howManyParams(): # returns number of Parameters, call first
	testdata = "Init"
	with open(td_filename, newline='') as f:
		testdata = csv.reader(f, delimiter = ";")
		for headline in testdata:
			print(headline)
			print ("howManyParams")  # 0-index
			break # get the first row 
		params = 1
		col = 2
		# value = headline[0,0]  # if leer then Fehler
		value = headline[col]
		while value != "":
			## print(value)
			params  = params + 1
			col = col + 1
			value = headline[col]
		params = params - 1
		return params

	# ExpectedResult	Param1	Param2
