import xml.dom.minidom as xmldom
import os

xml_filepath = os.path.abspath(r"C:\Users\DELL\Desktop\Decting\SCFC_TL19_ENB_FSMr4_MIMO_TM3_32TRX.xml")
# 得到文件对象
dom_obj = xmldom.parse(xml_filepath)
# 得到元素对象
element_obj = dom_obj.documentElement
# 获得子标签
sub_element_obj = element_obj.getElementsByTagName("managedObject")

for i in range(len(sub_element_obj)):
    print(i)
    if sub_element_obj[i].findall("p"):
        print(sub_element_obj[i].text())






