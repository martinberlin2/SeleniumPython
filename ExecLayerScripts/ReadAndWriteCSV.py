

	# ReadAndWriteCSV
	# https://docs.python.org/3/library/csv.html#reader-objects

	# C:\Users\laoch\OneDrive\Dokumente\Meins\Eigenes_F\auticon\Python\SeleniumPython\TestData
	# DD_Testdata.csv 
import csv

from Utilities.readCfg import readConfig 
config = readConfig("./config.txt")
SeleniumRoot = config.get("SeleniumRoot")

# SeleniumRoot = r"D:\Travel\SeleniumPython"   # ReiseLab
# print("SeleniumRoot = " + SeleniumRoot)
pfadfile = r"\TestData\DD_Testdata.csv"
td_filename = SeleniumRoot + pfadfile
## print (str(td_filename))

def run():
	numOfParams = howManyParams()
	## print(numOfParams)
	readAll(numOfParams)
	
def isLineEmpty(numOfParams, line):
	i = 0
	while i < numOfParams:
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
			if isLineEmpty(numOfParams, row):
				print("Leerzeile erkannt")
				break
			c = 2
			while c < numOfParams + 2:
				print(row[c])
				c = c + 1
			print("-------")
		print("---- Ende Testdata ----")
			
			
	# wieviele Header
def howManyParams(): # returns number of Parameters, call first
	testdata = "Init"
	with open(td_filename, newline='') as f:
		testdata = csv.reader(f, delimiter = ";")
		for headline in testdata:
			## print(headline)
			## print (headline[2])  # 0-index
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
