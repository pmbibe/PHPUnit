import xml.etree.ElementTree as ET
tree = ET.parse('report.xml')
root = tree.getroot()
for child in root:
        Result=child.attrib
Number_of_Errors = Result["errors"]
print "Total tests: " + Result["tests"]
print "Errors: " + Result["errors"]
print "Success: " + Result["assertions"]
if Number_of_Errors > 0:
	print "Can't deploy"
else:
 	os.system("rsync -v ./PHPUnit/*   -e ssh /  root@192.168.141.203:/usr/share/nginx/html")
