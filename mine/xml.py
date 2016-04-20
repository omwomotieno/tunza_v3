# Using lxml:

from lxml import etree

# create XML
root = etree.Element('root')
root.append(etree.Element('child'))
# another child with text
child = etree.Element('child')
child.text = 'some text'
root.append(child)

# pretty string
s = etree.tostring(root, pretty_print=True)
print s
Output:

<root >
  <child / >
  <child > some text < /child >
< / root >

------------------------------------------

# ElementTree is a good module for reading xml and writing too e.g.

from xml.etree.ElementTree import Element, SubElement, tostring

root = Element('root')
child = SubElement(root, "child")
child.text = "I am a child"

print tostring(root)
Output:

<root > <child > I am a child < /child > < / root >
See this tutorial for more details and how to pretty print.

# Alternatively if your XML is simple, do not underestimate
# the power of string formatting :)

xmlTemplate = """<root>
    <person>
        <name>%(name)s</name>
        <address>%(address)s</address>
     </person>
</root>"""

data = {'name': 'anurag', 'address': 'Pune, india'}
print xmlTemplate % data
Output:

<root >
    <person >
        <name > anurag < /name >
        <address > Pune, india < /address >
     </person>
</root>

# You can use string.Template or some template engine too,
# for complex formatting.

