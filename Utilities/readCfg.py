

# readCfg.py -- Konfig-Datei einlesen
# Konfig-Datei: # Category <TAB> Value
# Klasse CFG: Category + Value 
# dir = CFG.get(dir)
import os.path as path
from typing import List

class CFG: 
	def __init__ (self) :
		self.cfg_items: List []
	
	def add(c,v, self):
		(self.cfg_items).append([c,v])
				## AttributeError: 'str' object has no attribute 'cfg_items'
		# TODO Doppelte checken
	
	def get(c, self):
		arr = self.cfg-items
		pos = 0
		while pos < len(arr):
			item = arr[pos]
			if item.c == c:
				return item.v
			pos = pos+1
		return "category not found"

def readConfig(filename): # <- relativer Dateiname; Datei= "Kategorie<TAB>Wert", Returns Array (category, value) 
	# readConfig("./config.txt")
	# import os.path
	
	mylist = []
	mylist.append([1,3])
	print(mylist)
	
	if path.isfile(filename) == False:
		print("Config File not found")
		return
	cfgFile = open(filename, "r")
	cfg = CFG()
	while True:   						 # for line in cfgFile:
		line = cfgFile.readline()
		if not line:    #check if line is null
			break
		linesplit = line.split()
		category = linesplit[0]
		value 	 = linesplit[1]
		cfg.add(category, value)
		print(category)
		print(value)
	#close file
	cfgFile.close
			
	# def importList(self, list): # TODO noch kein Check ob list 2D ist. self.list = list
		# self.list = list

	# def exportList(self): #-> return self.list
		# return self.list
		

readConfig("./config.txt")