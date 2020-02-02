import xml.etree.ElementTree as ET
data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
     +12342452134
     </phone>
     <email hide="yes"/>
     </person> '''

tree = ET.fromstring(data)
print('Name :',tree.find('name').text)
print('Phone :',tree.find('phone').text)
print('Attr :',tree.find('email').get('hide'))
print(tree.find('phone').get('type'))
