import shutil
import html
import xml.dom.minidom
import os
# in /msg/ folder

yabberPath = r"D:\Game\ERModing\Yabber.1.3.1\Yabber.exe"
# 
langs = ["deude","frafr","itait","jpnjp","korkr","polpl","porbr","rusru","spaar","spaes","thath","engus","zhocn", "zhotw"]

excludeLangs = ["zhocn", "zhotw"]

workPlacePath = "E:/Steam/steamapps/common/ELDEN RING/Game/msg-bak/msg/"

unModifBasePath = "E:/Steam/steamapps/common/ELDEN RING/Game/msg/"
pathPart = "/menu-msgbnd-dcx/GR/data/INTERROOT_win64/msg/"

"""
<text id="70000000">召唤梅琳娜</text>
<text id="70000001">遣返梅琳娜</text>
<text id="70000002">和梅琳娜聊天</text>
"""
# 对照表, 从talk msg 获取对应data（字符串），放入自定义的even text for talk
"""
event Text for talk id |  talk msg id
70000100 | 保留为空
70000101 | <text id="100031000">……关于我吗？</text>
70000102 | <text id="100030000">……这簇小巧的金光，是黄金树的赐福。</text>
70000103 | <text id="100102010">“噢，拉达冈啊，黄金律法的忠犬啊。”</text>
70000104 | <text id="100103010">“我在此宣告，去探索黄金律法──”</text>
70000105 | <text id="100104010">“王的众战士啊，吾王葛孚雷啊。”</text>
70000106 | <text id="100041010">“吾王啊，王的众战士啊，我将夺去你们的赐福。”</text>
70000107 | <text id="100044010">“在你们面临死亡之后，那被夺去的会再归还──”</text>
70000108 | <text id="100045010">“黄金树是掌管一切的存在。做出抉择吧──”</text>
70000109 | <text id="100120010">……你的身体里，还住着另外一个人吗？</text> (约定)
70000110 | <text id="100121010">……你的身体里，还住着另外一个人吗？</text> (旅行)
70000111 | <text id="100150000">……你不用担心火种。</text>
70000112 | <text id="100101010">“半神啊，我可爱的孩子啊。”</text> 
70000113 | <text id="100160000">……我想告诉你一件事。</text>
70000114 | <text id="100180000">……如果你的心向着癫火，</text>
70000115 | <text id="100181000">……我会准备火种。</text>
70000116 | <text id="100185010">请让你的心，远离癫火吧。</text>
70000117 | <text id="100186000">拜托你了，能不能悬崖勒马？</text>
"""
comparationTable = {
    # "70000100":"",
    "70000101": "100031000",
    "70000102": "100030000",
    "70000103": "100102010",
    "70000104": "100103010",
    "70000105": "100104010",
    "70000106": "100041010",
    "70000107": "100044010",
    "70000108": "100045010",
    "70000109": "100120010",
    "70000110": "100121010",
    "70000111": "100150000",
    "70000112": "100101010",
    "70000113": "100160000",
    "70000114": "100180000",
    "70000115": "100181000",
    "70000116": "100185010",
    "70000117": "100186000",
}

# 拼凑 xml 路径:
for lang in langs:
    xmlPaht_EventTextForTalk = workPlacePath+lang+pathPart + \
        lang[0:-2]+lang[-2:].upper()+"/"+"EventTextForTalk.fmg.xml"
    xmlPaht_TalkMsg = workPlacePath + lang+pathPart + \
        lang[0:-2]+lang[-2:].upper()+"/"+"TalkMsg.fmg.xml"
    # 重新解包
    os.system(yabberPath + " "+'"{}"'.format(unModifBasePath+lang +
              pathPart+lang[0:-2]+lang[-2:].upper()+"/"+"EventTextForTalk.fmg"))
    # 复制到工作目录
    shutil.copyfile(unModifBasePath+lang+pathPart+lang[0:-2]+lang[-2:].upper()+"/"+"EventTextForTalk.fmg.xml",
                    workPlacePath+lang+pathPart+lang[0:-2]+lang[-2:].upper()+"/"+"EventTextForTalk.fmg.xml")

    os.system(yabberPath + " "+'"{}"'.format(unModifBasePath + lang +
              pathPart+lang[0:-2]+lang[-2:].upper()+"/"+"TalkMsg.fmg"))
    shutil.copyfile(unModifBasePath+lang+pathPart+lang[0:-2]+lang[-2:].upper(
    )+"/"+"TalkMsg.fmg.xml", workPlacePath+lang+pathPart+lang[0:-2]+lang[-2:].upper()+"/"+"TalkMsg.fmg.xml")

    # event text for talk
    # 从 talkmsg获取二级菜单的选项字符串
    document_eventForTalk = xml.dom.minidom.parse(xmlPaht_EventTextForTalk)
    nodes_eventForTalk = document_eventForTalk.documentElement.getElementsByTagName("entries")[
        0].childNodes
    nodes_eventForTalk_TextNode = []
    nodes_eventForTalk_Id = []
    nodes_eventForTalk_Data = []
    # 收集已有id 与数据
    for node in nodes_eventForTalk:
        if len(node.childNodes) == 0:
            # 为 \n 节点
            continue
        else:
            nodes_eventForTalk_TextNode.append(node)
            nodes_eventForTalk_Id.append(node.getAttribute('id'))
            nodes_eventForTalk_Data.append(node.childNodes[0].data)

    # talk msg
    document_talkMsg = xml.dom.minidom.parse(xmlPaht_TalkMsg)
    nodes_talkMsg = document_talkMsg.documentElement.getElementsByTagName("entries")[
        0].childNodes
    nodes_talkMsg_TextNode = []
    nodes_talkMsg_Id = []
    nodes_talkMsg_Data = []
    # 收集已有id 与数据
    for node in nodes_talkMsg:
        if len(node.childNodes) == 0:
            # 为 \n 节点
            continue
        else:
            nodes_talkMsg_TextNode.append(node)
            nodes_talkMsg_Id.append(node.getAttribute('id'))
            nodes_talkMsg_Data.append(node.childNodes[0].data)

    # 添加条目到event msg for talk
    entriesNode = document_eventForTalk.documentElement.getElementsByTagName("entries")[
        0]
    for entryKey in comparationTable:
        if entryKey in nodes_eventForTalk_Id:
            # 已存在自定义条目，修改相应node？
            nodes_eventForTalk_TextNode[nodes_eventForTalk_Id.index(entryKey)].childNodes[0].data = '"{}"'.format(
                nodes_talkMsg_Data[nodes_talkMsg_Id.index(comparationTable[entryKey])])
            continue
        else:
            # 不存在，新增node
            newNode = document_eventForTalk.createElement("text")
            newNode.appendChild(document_eventForTalk.createTextNode('"{}"'.format(
                nodes_talkMsg_Data[nodes_talkMsg_Id.index(comparationTable[entryKey])])))
            newNode.setAttribute("id", entryKey)
            entriesNode.insertBefore(
                newNode, nodes_eventForTalk[len(nodes_eventForTalk)-1])
    summonMeli="Summon Melina"
    leaveMeli="Let Melina Leave"
    chatMeli="Chat With Melina"
    if(lang=="zhocn"):
        summonMeli="召唤梅琳娜"
        leaveMeli="让梅琳娜离去"
        chatMeli="与梅琳娜聊天"
    elif(lang=="zhotw"):
        summonMeli="召喚梅琳娜"
        leaveMeli="讓梅琳娜離去"
        chatMeli="與梅琳娜聊天"
    # TODO 添加 "召唤梅琳娜" ,一级菜单选项
    newNode = document_eventForTalk.createElement("text")
    newNode.appendChild(document_eventForTalk.createTextNode(summonMeli))
    newNode.setAttribute("id", str(70000000))
    entriesNode.insertBefore(
        newNode, nodes_eventForTalk[len(nodes_eventForTalk)-1])

    newNode = document_eventForTalk.createElement("text")
    newNode.appendChild(
        document_eventForTalk.createTextNode(leaveMeli))
    newNode.setAttribute("id", str(70000001))
    entriesNode.insertBefore(
        newNode, nodes_eventForTalk[len(nodes_eventForTalk)-1])

    newNode = document_eventForTalk.createElement("text")
    newNode.appendChild(
        document_eventForTalk.createTextNode(chatMeli))
    newNode.setAttribute("id", str(70000002))
    entriesNode.insertBefore(
        newNode, nodes_eventForTalk[len(nodes_eventForTalk)-1])

    # 覆写文件
    # backup
    shutil.copyfile(xmlPaht_EventTextForTalk, xmlPaht_EventTextForTalk+".bak")
    with open(xmlPaht_EventTextForTalk.format(lang), 'w',encoding="utf-8") as f:
    # with open("output-{}.xml".format(lang), 'w', encoding="utf-8") as f:
        # document_eventForTalk.writexml(f,newl="\n")

        # 多周目提示字符被替换
        # f.write(html.unescape(document_eventForTalk.toxml()))
        f.write(document_eventForTalk.toxml().replace("&quot;","\""))
    # yabber repack
    os.system(yabberPath +" "+'"{}"'.format(xmlPaht_EventTextForTalk))
    os.system(yabberPath +" "+'"{}"'.format(workPlacePath+lang+"/menu-msgbnd-dcx"))

    print("done of {}".format(lang))
