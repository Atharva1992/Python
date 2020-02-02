import xml.etree.ElementTree as ET
input = '''<stuff>
<users>
    <user x="2">
        <id>001</id>
        <name>Chuck</name>
    </user>
    <user>
        <id>002</id>
        <name>Barry</name>
    </user>
</users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')

print(lst)
for item in lst :
    print("Name : ",item.find('name').text)
    print("ID : ", item.find('id').text)
    print("Atri :", item.get('x'))
