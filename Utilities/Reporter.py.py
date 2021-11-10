

# Reporter.py -- schreibt Testergebnis in /Reports/report.txt
# Testcase				Result		Failed:Why
import os.path as path

def readConfig(filename): # Param: relativer Dateiname; Datei= "Kategorie<TAB>Wert", Returns: cfg= CFG-Objekt mit Einträgen (category, value), Zugriff: cfg.get("category") --> value; Error: String "config category not found"
	report = './Reports/report.txt'
	