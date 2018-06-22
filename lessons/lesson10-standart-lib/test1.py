from xml.etree import ElementTree as ET
from xml.dom import pulldom
from xml import sax

root = ET.Element('tasks')

day = ET.SubElement(root, 'day')
day.set('date', '01.01.2018')

task1 = ET.SubElement(day, 'task')
task1.text = "Wake up"

task2 = ET.SubElement(day, 'task')
task2.text = "Make coffee"

tree = ET.ElementTree(root)
tree.write('textFile.xml')


# tasks = tree.findall('.//task')
# for task in tasks:
#     print(task.text)


# doc = pulldom.parse('textFile.xml')
# for event, node in doc:
#     if event == pulldom.START_ELEMENT and node.localName == 'task':
#         doc.expandNode(node)
#         print(node.toxml())


#
# parsedTree = ET.parse('textFile.xml')
# root = parsedTree.getroot()
# for el in root:
#     for el1 in el:
#         print(el1.text)

class TasksHandler(sax.ContentHandler):
    def __init__(self):
        self.is_task = False

    def startElement(self, name, attrs):
        if name == 'task':
            self.is_task = True

    def endElement(self, name):
        if name == 'task':
            self.is_task = False

    def characters(self, content):
        if self.is_task:
            print(content)


parser = sax.make_parser()
parser.setContentHandler(TasksHandler())
parser.parse('textFile.xml')

# tasksHandler.