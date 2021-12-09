

# Helper.py 


def substrAfterHead(s, head): # keine Prüfungen 
	return s[len(head): len(s)]
	
def testSubstrAfterHead(): 
	print("tail == " + substrAfterHead("headtail", "head"))
	print("leer ==" + substrAfterHead("str", "str"))
	print("komplett ==" + substrAfterHead("komplett", ""))
	
testSubstrAfterHead()
