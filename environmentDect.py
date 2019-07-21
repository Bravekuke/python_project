#!/usr/bin/python
# -*- coding: UTF-8 -*-
from xml.dom.minidom import parse
import xml.dom.minidom

if __name__ == '__main__':
    xmlpath = r"C:\Users\DELL\Desktop\Decting\SCFC_TL19_ENB_FSMr4_MIMO_TM3_32TRX.xml"
    DomTree = xml.dom.minidom.parse(xmlpath)
    root = DomTree.documentElement  # 创建dom树对象
    print(root)
    element = root.getElementsByTagName('p')
    for i in range(len(element)):
        if element[i].getAttribute("name") == "btsName":
            print("yes"element[i].txt)
        else:
            print("no")