from xml.etree.ElementTree import Element, SubElement, dump

note = Element("note")
to = Element("to")
to.text = "Tove"

note.append(to)
SubElement(note, "from").text = "Jani"
#속성을 아래와 같이 추가한다.
note.attrib["date"] = "20140909"

dump(note)
