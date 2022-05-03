

	# ReadAndWriteCSV
	# https://docs.python.org/3/library/csv.html#reader-objects

	# C:\Users\laoch\OneDrive\Dokumente\Meins\Eigenes_F\auticon\Python\SeleniumPython\TestData
	# DD_Testdata.csv 

def readAll():
	pfadhome = r"C:\Users\laoch\OneDrive\Dokumente\Meins\Eigenes_F\auticon\Python\SeleniumPython"
	pfadfile = r"\TestData\DD_Testdata.csv"
	td_filename = pfadhome + pfadfile
	
	import csv
	with open(td_filename, newline='') as f:
		testdata = csv.reader(f)
		print("row read1")
		for row in testdata:
			print("row read")
			print(row)
		 

	# wieviele Header
def otherstuff():
	headers = 1

	value = tdWS.cell(row = 1, column = headers)
	while value != "":
		headers = headers + 1
		value = tdWS.cell(row = 1, column = headers)
	headers = headers - 1

	# alles lesen, alles drucken
	r = 2
	col1 = tdWS.cell(row = r, column = 1)
	while col1 != "":
		for c in range  (2, headers):
			value = tdWS.cell(row = r, column = c)
			print ("r= " + r + "c= " + "Wert: " + value)
		r = r + 1
		col1 = tdWS.cell(row = r, column = 1)


	# ExpectedResult	Param1	Param2
