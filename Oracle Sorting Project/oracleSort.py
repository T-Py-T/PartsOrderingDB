class oracleSort:
    '''Oracle database object'''
    def __init__(self, name):
        self.name = name
        self.partNum = ""
        self.partDescription = ""
        self.partDrawingNum = ""
        self.individualPartNum = []
        self.assocDrawingNum =[]
    def set_pn(self, partNum):
        self.partNum =  self.partNum + partNum
    def set_pd(self, partDescription):
        self.partDescription =  self.partDescription + partDescription
    def set_pdn(self, partDrawingNum):
        self.partDrawingNum =  self.partDrawingNum + partDrawingNum
    def add_ipn(self, individualPartNum):
        self.individualPartNum.append(individualPartNum)
    def add_adn(self, assocDrawingNum):
        self.assocDrawingNum.append(assocDrawingNum)
    def print_content(self):
        print self.name
        print self.partNum
        print self.partDescription
        print self.partDrawingNum
        print self.individualPartNum
        print self.assocDrawingNum
    def clear_object(self):
        self.partNum = ""
        self.partDescription = ""
        self.partDrawingNum = ""
        self.individualPartNum = []
        self.assocDrawingNum =[]
		
def xml_read(file):
	import xml.etree.ElementTree as ET
	dict1 = {}
	raw = open('RobotPartsOrdering_Acad_Macro2.xml','r')
	data = raw.read()
	# print data
	tree = ET.fromstring(data)
    
	for row in tree.findall ('row') :
		rownum = 0 
		rowname = ""
		rowname2 = ""
		x = 0.0
		y = 0.0
		for cell in row.findall('cell')
			if row num == 0:
				rowname = cell.findtext('data')
				rownum += 1
			if row num == 1:
				rowname2 = cell.findtext('data')
				rownum += 1
			if row num == 2:
				x = cell.findtext('data')
				rownum += 1
			if row num == 3:
				y = cell.findtext('data')
				rownum += 1
		

	'''
	for lines in tree:
		if line.attribute == 'string':
			if counter == 0:
				partNum = text
				counter +=1
			if counter == 1:
				partDescription = text
				counter += 1
			if counter == 2:
				partDrawingNum = text
				counter += 1
	'''
	
		
def sql_createTable(tableName):
    import sqlite3
    conn = sqlite3.connect('F:\PythonScripts\PythonTest.sqlite')
    c = conn.cursor()
    c.execute('''CREATE TABLE tableName (Part Number TEXT, Part Description TEXT, Part Drawing Number TEXT)''')
    conn.commit()
    conn.close()

def sql_addRow(tableName, rowData):
    import sqlite3
    conn = sqlite3.connect('F:\PythonScripts\PythonScripts\PythonTest.sqlite')
    c = conn.cursor()
	c.execute('SELECT partNumber FROM tableName WHERE partNumber = ? ', (partNumber, tableName, partNumber ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO tableName (org, count) 
                VALUES ( ?, 1 )''', (org, ) )
    c.execute('''INSERT INTO tableName(rowData)''')
    conn.commit()
    conn.close()

def sql_addIndex(tableName, rowName, IndexData):
    import sqlite3
    conn = sqlite3.connect('F:\PythonScripts\PythonScripts\PythonTest.sqlite')
    c = conn.cursor()
    c.execute('''INSERT INTO rowName(indexData)''')
    conn.commit()
    conn.close()