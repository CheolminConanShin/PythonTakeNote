from xml.etree.ElementTree import parse
tree = parse("note.xml")
note = tree.getroot()

print (note.get("date"))
print (note.get("foo", "default"))
print (note.keys())
print (note.items())
