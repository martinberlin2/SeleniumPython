# CopyFileLineByLine.py
# --- side product from:
# ##GOAL: reads python modul, writes only the signatures with the one-liner-comment, and which class
# - Frame: read and write text
# - Modul: textTools.py 
#	- containsWord(line, word) #->pos  <-StandardLibs!	
# 	- LineIfContains(*words, foundInThisOrder) # -> (posFirst, endposLast)
#	
# - links trim und fertig!

# Aufruf in main:
# import CopyFileLineByLine
# CopyFileLineByLine = CopyFileLineByLine.CopyFileLineByLine
# CopyFileLineByLine("Tests_List2D")



# Testfälle
# expected_defs_tests_List2D.txt
# expected_defs_List2D.txt
# Dateien angelegt
# CompareFiles.py vorhanden  -- Testfälle -- fertig und läuft, neu 21.7. 
# TC: Codes von Tests_List2D und List2D - execTC anlegen - fertig
# 


# evalTC(1, "File copied", CompFiles("Tests_List2D_signatures.py", "Tests_List2D.py"), "FilesAreEqual")

import NaTALi
exec_TC = NaTALi.exec_TC
exec_TCAlt = NaTALi.exec_TCAlt
evalTC = NaTALi.evalTC
execFuncWithExc = NaTALi.execFuncWithExc
execMethWithExc = NaTALi.execMethWithExc
evalTC = NaTALi.evalTC

# f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline. This makes the return value unambiguous; if f.readline() returns an empty string, the end of the file has been reached, while a blank line is represented by '\n', a string containing only a single newline.


def CopyFileLineByLine(f):# reads f.py, writes m_signatures.py - only the headers with the one-liner-comment, and which class. Returns None or "Module not found"
	infile = './' + f + ".py"
	outfile = './' + f + "_signatures.py"
	# print("only_sig_from_module:", infile)
	import os.path
	if os.path.isfile(infile) == False:
		# print("Module not found")
		return "Module not found"
	if os.path.isfile(outfile) == True:
		os.remove(outfile)
	with open(infile, "r") as module:   # weiter : erst in CompFiles lösen
		moduleLine = module.readline()
		# print("erste moduleLine:", moduleLine,"!")		
		while len(moduleLine) > 0:   # moduleLine != '':
			process(moduleLine, outfile)
			moduleLine = module.readline() # kein EOFError
			# print("moduleLine:", moduleLine)

def process(line, outfile): #-> decides if line contains "def" or the class name	and writes -- PRIVATE
	with open(outfile, "a") as headerFile:
		# print("OutfileName:", outfile)
		
		# do_some_stuff ... filter, search, evaluate the input text... then it's more than just copy!
		
		headerFile.write(line)