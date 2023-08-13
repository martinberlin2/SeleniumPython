

# python -m CompareFiles
# CompFiles in NaTALi 10.8.

def CompFiles(result, expected): # --> (Zeilennr, Spaltennr) or "ExpectedFileNotFound" (prio), "ResultFileNotFound", "FilesAreEqual" 
	import divers
	compareStrings = divers.compareStrings
	rsfile = './' + result
	exfile = './' + expected
	import os.path
	if os.path.isfile(exfile) == False:
		return "ExpectedFileNotFound"
	if os.path.isfile(rsfile) == False:
		return "ResultFileNotFound"

	line = -1
	# with open(result, "r") as rfile:
	col = 0
	
	with open(exfile, "r") as efile, open(rsfile, "r") as rfile:
		rtext = rfile.readline()
		etext = efile.readline()
		# logging.info(rtext)
		# logging.info(etext)
		while rtext + etext!= '':
			line = line + 1
			if rtext != etext:
				col = compareStrings(rtext,etext) # kein Check auf "StringsAreEqual"
				# logging.info("Abweichung Zeile, Spalte: ", line, col)
				# logging.info("rtext=", rtext,"#")
				# logging.info("etext=", etext,"#")
				# logging.info(line, col)
				return (line, col)
			# with open(result, "r") as rfile:
			rtext = rfile.readline()
			etext = efile.readline()
			# logging.info("rtext=", rtext)
			# logging.info("etext=", etext)
		# close()
		# logging.info("FilesAreEqual")
	return "FilesAreEqual"


def CompFilesAlt(result, expected): #-> returns line of first difference, or "ExpectedFileNotFound" (prio), "ResultFileNotFound", "FilesAreEqual"	
	import os.path
	if os.path.isfile('./' + expected) == False:
		return "ExpectedFileNotFound"
	if os.path.isfile('./' + result) == False:
		return "ResultFileNotFound"
	line = -1
	# with open(result, "r") as rfile:				
	with open(expected, "r") as efile, open(result, "r") as rfile:
		rtext = rfile.readline()
		etext = efile.readline()
		while rtext + etext!= '':
			line = line + 1
			if rtext != etext:
				# logging.info("		Abweichung Zeile ", line)
				# logging.info("		rtext=", rtext,"#")
				# logging.info("		etext=", etext,"#")
				return line
			# with open(result, "r") as rfile:
			rtext = rfile.readline()
			# logging.info("rtext=", rtext)
			# with open(expected, "r") as efile:
			etext = efile.readline()
			# logging.info("etext=", etext)
		# close()
		# logging.info("Dateien sind gleich")
	return "FilesAreEqual"
	
# erg = CompFiles("3fruits.txt", "3fruits.exp")