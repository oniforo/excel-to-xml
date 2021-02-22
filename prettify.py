import xml.etree.ElementTree as ET
import xml.dom.minidom as DOM

def prettify(elem):
    raw = ET.tostring(elem, 'utf-8')
    dom_parse = DOM.parseString(raw)
    return dom_parse.toprettyxml(indent="   ")