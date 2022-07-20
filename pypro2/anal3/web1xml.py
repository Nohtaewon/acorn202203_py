# 웹문서 처리 : XML
# ElementTree 모듈 이용
import xml.etree.ElementTree as etree

xmlfile = etree.parse("my.xml")
print(xmlfile, type(xmlfile))

root = xmlfile.getroot()
print(root.tag)
print(root[0].tag)
print(root[0][0].tag)
print(root[0][0].attrib)
print(root[0][2].attrib.keys())
print(root[0][2].attrib.values())
imsi=list(root[0][2].attrib.values())
print(imsi)

print('------------------------------------------')
children = root.findall('item')
for it in children:
    re_id=it.find('name').get("id")     # 속성값
    re_name=it.find("name").text        # 요소값
    print(re_id, re_name)

