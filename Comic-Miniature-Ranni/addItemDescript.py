import shutil
import html
import xml.dom.minidom
import os
# in /msg/ folder

# ** 复制娇小拉妮 物品名称与描述

yabberPath = r"D:\Game\ERModing\Yabber.1.3.1\Yabber.exe"
# 
langs = ["deude","frafr","itait","jpnjp","korkr","polpl","porbr","rusru","spaar","spaes","thath","engus","zhocn", "zhotw"]

excludeLangs = ["zhocn", "zhotw"]

workPlacePath = "msg"
modBuildPath = "modBuild"

unModifBasePath = os.path.join("E:", "Steam", "steamapps", "common", "ELDEN RING", "Game","msg") 
pathPart = os.path.join("item-msgbnd-dcx","GR", "data","INTERROOT_win64", "msg" )

targetDcxFileName = "item.msgbnd.dcx"

# todo using list
targetFiles = ["GoodsCaption.fmg", "GoodsName.fmg", "GoodsInfo.fmg"]

winzigeRanniGoodsId = '8146'
new_item_winzigeRanniGoodsId = '30000'

# 拼凑 xml 路径:
for lang in langs:
  for fmgFile in targetFiles:
    xmlPath = os.path.join( workPlacePath, lang, pathPart, lang[0:-2] + lang[-2:].upper(), fmgFile + ".xml")


    origin_fmg_filePath = '"{}"'.format(os.path.join(unModifBasePath, lang, pathPart, lang[0:-2] + lang[-2:].upper(), fmgFile)) 

    origin_fmg_xml_filePath = '"{}"'.format(os.path.join(unModifBasePath, lang, pathPart, lang[0:-2] + lang[-2:].upper(), fmgFile + ".xml"))


    # 重新解包
    os.system(yabberPath + " "+ origin_fmg_filePath)
    # 复制到工作目录
    shutil.move(origin_fmg_xml_filePath.replace("\"", ""), xmlPath)

    # shutil.rmtree(os.path.join(unModifBasePath, lang, targetDcxFileName))

    # copy node
    document_eventForTalk = xml.dom.minidom.parse(xmlPath)
    nodes_eventForTalk = document_eventForTalk.documentElement.getElementsByTagName("entries")[
        0].childNodes
    nodes_TextNode = []
    nodes_Id = []
    nodes_Data = []
    # 收集已有id 与数据
    for node in nodes_eventForTalk:
        if len(node.childNodes) == 0:
            # 为 \n 节点
            continue
        else:
            nodes_TextNode.append(node)
            nodes_Id.append(node.getAttribute('id'))
            nodes_Data.append(node.childNodes[0].data)

    # 添加条目到event msg for talk
    entriesNode = document_eventForTalk.documentElement.getElementsByTagName("entries")[
        0]
    newNode = document_eventForTalk.createElement("text")
    newNode.appendChild(document_eventForTalk.createTextNode('"{}"'.format(
        nodes_Data[nodes_Id.index(winzigeRanniGoodsId)])))
    newNode.setAttribute("id", new_item_winzigeRanniGoodsId)
    entriesNode.insertBefore(
        newNode, nodes_eventForTalk[len(nodes_eventForTalk)-1])
 
    # 覆写文件
    # backup
    # shutil.copyfile(xmlPath, xmlPath+".bak")
    with open(xmlPath, 'w',encoding="utf-8") as f:
    # with open("output-{}.xml".format(lang), 'w', encoding="utf-8") as f:
        # document_eventForTalk.writexml(f,newl="\n")

        # 多周目提示字符被替换
        # f.write(html.unescape(document_eventForTalk.toxml()))
        f.write(document_eventForTalk.toxml().replace("&quot;","\""))
    # yabber repack
    os.system(yabberPath +" "+'"{}"'.format(xmlPath))
  os.system(yabberPath +" "+os.path.join(workPlacePath, lang, targetDcxFileName.replace(".","-")))
  #copy to mod build folder
  modBuildPath_lang = os.path.join(modBuildPath,"msg",lang)
  if(not os.path.exists(modBuildPath_lang)):
    os.makedirs(modBuildPath_lang)
  shutil.move(os.path.join(workPlacePath, lang, targetDcxFileName), os.path.join( modBuildPath_lang,targetDcxFileName))
  print("done of {}".format(lang))
