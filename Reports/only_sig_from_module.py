# only_sig_from_module.py
# reads python modul, writes only the signatures with the one-liner-comment, and which class
# - Frame: read and write text - fertig --> CopyFileLineByLine.py
# - wenn "def" am Anfang...
# - links trim und fertig!

# Testfälle
# expected_defs_tests_List2D.txt
# expected_defs_List2D.txt
# Dateien angelegt
# CompareFiles.py vorhanden  -- Testfälle -- fertig und läuft, neu 21.7. 
# TC: Codes von Tests_List2D und List2D - execTC anlegen - fertig
# 

# import NaTALi
# exec_TC = NaTALi.exec_TC
# exec_TCAlt = NaTALi.exec_TCAlt
# evalTC = NaTALi.evalTC
# execFuncWithExc = NaTALi.execFuncWithExc
# execMethWithExc = NaTALi.execMethWithExc
# evalTC = NaTALi.evalTC

import logging
import divers
containsString = divers.containsString

def only_sig_from_module(m):# reads module m.py, writes m_signatures.py - only the headers with the one-liner-comment. Returns None or "Module not found"
	infile = './' + m + ".py"
	outfile = './' + m + "_signatures.py"
	# logging.info("+++++++++++++++++++++++++++++++++ only_sig_from_module:" + infile)
	import os.path
	if os.path.isfile(infile) == False:
		# logging.info("Module not found")
		return "Module not found"	
	if os.path.isfile(outfile) == True:
		os.remove(outfile)
		# logging.info("os.remove(outfile)" + outfile)
	outfile = './' + m + "_signatures.py"
	# with open(outfile, "a") as headerFile:
		# headerFile.write("outfile ist angelegt\n")  # -- hier weiter testen warum schreibt und liest er nix
	with open(infile, "r") as module:   # von CopyFileLineByLine
		moduleLine = module.readline()
		# print("erste moduleLine:", moduleLine,"!", len(moduleLine))		
		while len(moduleLine) > 0:   # moduleLine != '':
			# logging.info("im WHILE")
			tempstr = process(moduleLine, outfile)
			# processended = process(moduleLine, outfile)
			# logging.info("processended: " + processended + "\n")
			# processended = "undef"
			try:
				moduleLine = module.readline() # kein EOFError
				# logging.info("im WHILE gelesen: " + moduleLine + "!" + str(len(moduleLine)))
			except Exception as ex:
				logging.info("EXC" + str(ex))
				logging.info("EXC moduleLine:" + moduleLine + str(len(moduleLine)) )
		# logging.info("end while")
	return

def process(line, outfile): #-> decides if line contains "def" or the class name	and writes -- PRIVATE
	with open(outfile, "a") as headerFile:		
		# logging.debug("start process:" + line + "!")
		line = line.strip()   # nicht # line = strip(line)
		# logging.debug("process:" + line + "!")
		# if True:
		# headerFile.write(line + "+++++ vor if")  # so gehts
		# try:
			# temperg = containsString(line, "def", True)
			# logging.debug("containsString(line, def, True)" + temperg)
		# except Exception as ex:
			# logging.debug("EXC containsString" + str(ex))
		# headerFile.write(line + "+++++ nach if")  # so gehts
		foundpos = -9
		try:
			foundpos = containsString(line, "def", True)
			# logging.info ("containsString foundpos:" + str(foundpos))
		except Exception as ex:
			logging.info ("containsString EXC:" + str(ex))
		if foundpos == 0:
		# if containsString(line, "def", True) == 0:
		# if "def" in line:  # -- hier weiter: -> divers: containsString(str, substr, asWord) # -> pos or False
			# logging.info("############def in line: " + line)
			line = line + "\n"
			headerFile.write(line)  # so gehts
	return "process ended"