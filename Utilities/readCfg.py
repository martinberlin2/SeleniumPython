

# readCfg.py -- Konfig-Datei einlesen
# Konfig-Datei: # Category <TAB> Value
# Klasse CFG: Category + Value 
# dir = CFG.get(dir)
import os.path as path


class CFG: 
	def __init__ (self) : # ok
		# print("init CFG")
		self.cfg_items = []
	
	def addElem(self, c,v):  # ok
		self.cfg_items.append([c,v])
				## AttributeError: 'str' object has no attribute 'cfg_items'
		# TODO Doppelte checken
	
	def get(self, category):  # ok
		arr = self.cfg_items
		pos = 0
		while pos < len(arr): # geht, ab jetzt for
			item = arr[pos]
			if item[0] == category:
				return item[1]
			pos = pos+1
		return "config category not found"
		
	def showAll(self):  # ok 
		print("config=:")
		for elem in self.cfg_items:
			print(elem[0] + " = " + elem[1])
	

def readConfig(filename): # Param: relativer Dateiname; Datei= "Kategorie<TAB>Wert", Returns: cfg= CFG-Objekt mit Einträgen (category, value), Zugriff: cfg.get("category") --> value; Error: String "config category not found", "Config File not found"
	# readConfig("./config.txt")
	# import os.path
	
	# mylist = []
	# mylist.append([1,3])
	# print(mylist) # [[1, 3]] ---- ok
	
	if path.isfile(filename) == False:
		print("Config File not found")   # ok
		return "Config File not found"
	cfgFile = open(filename, "r")
	cfg = CFG()
	while True:	 # for line in cfgFile:
		line = cfgFile.readline()
		if not line:    #check if line is null
			break
		if line[0] != "#":			
			linesplit = line.split()
			category = linesplit[0]
			value 	 = linesplit[1]
			cfg.addElem(category, value)
		# print(category)
		# print(value + "\n")
	#close file
	cfgFile.close
	# cfg.showAll()
	# dir = cfg.get("DIR")
	# print ("dir: " + dir)
	# location = cfg.get("LOCATION")
	# print ("location: " + location)
	# what = cfg.get("what")
	# print ("what: " + what)		
	
	
	# def importList(self, list): # TODO noch kein Check ob list 2D ist. self.list = list
		# self.list = list

	# def exportList(self): #-> return self.list
		# return self.list
		
		
	return cfg 

# config = readConfig("./config.txt")
# config.showAll()
# SeleniumRoot = config.get("SeleniumRoot")
# print(SeleniumRoot)
