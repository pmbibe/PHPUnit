import xml.etree.ElementTree as ET
tree = ET.parse('report.xml')
root = tree.getroot()
for child in root:
        Result=child.attrib
Number_of_Errors = Result["errors"]
if Number_of_Errors > 0:
	print 0
else: 
	print 1
