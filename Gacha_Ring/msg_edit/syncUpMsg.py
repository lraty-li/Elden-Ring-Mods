import shutil
import html
import xml.dom.minidom
import os
import unPackUnModifyMsg
# in /msg/ folder

yabberPath = r"D:\Game\ERModing\Yabber.1.3.1\Yabber.exe"
#
langs = ["deude", "frafr", "itait", "jpnjp", "korkr", "polpl", "porbr", "rusru", "spaar", "spaes", "thath", "engus", "zhocn", "zhotw"]

excludeLangs = ["zhocn", "zhotw"]

workPlacePath = "D:/Game/ERModing/WorkPlace/gacha_ring/script/msg_edit/msg/"

unModifBasePath = "E:/Temp/ELDEN RING/Game/msg/"
pathPart = "/menu-msgbnd-dcx/GR/data/INTERROOT_win64/msg/"

"""
<text id="30000000">祈愿</text>
<text id="30000001">祈愿一次</text>
<text id="30000002">祈愿十次</text>
<text id="30000003">所需卢恩不足</text>
<text id="30000004">黄金卢恩[1]不足,是否使用10%升级所需卢恩兑换</text>
<text id="30000005">黄金卢恩[1]不足,是否使用100%升级所需卢恩兑换</text>
"""
i18nData = {
    "EventTextForTalk": {
        "id": [
            30000000,
            30000001,
            30000002,
            30000003,
            30000004,
            30000005,
            30000006,
        ],
        "zhocn":
        (
            "祈愿",
            "祈愿一次",
            "祈愿十次",
            "所需卢恩不足",
            "黄金卢恩【1】不足，是否使用10%升级所需卢恩兑换",
            "黄金卢恩【1】不足，是否使用100%升级所需卢恩兑换",
            "详情",
        ),
        "zhotw":
        (
            "祈願",
            "祈願一次",
            "祈願十次",
            "所需盧恩不足",
            "黃金盧恩【1】不足，是否使用10%升級所需盧恩兌換",
            "黃金盧恩【1】不足，是否使用100%升級所需盧恩兌換",
            "詳情"),
        "engus":
        (
            "Wish",
            "Wish x1",
            "Wish x10",
            "Insufficient runes",
            "1 Golden Rune [1] is needed. Purchase with 10% of runes needed to upgrade?",
            "10 Golden Rune [1] is needed. Purchase with 100% of runes needed to upgrade?",
            "Details"
        )},
    "TutorialTitle": {
            "id": [12000],
            "zhocn": ("艾奥尼亚战争",), "zhotw": ("艾奧尼亞戰爭",), "engus": ("The Battle of Aeonia",)
    },
    "TutorialBody": {
            "id": [12000],
            "zhocn": ('''
==========
女武神手刀
碎星大剑
==========
以上武器出现概率提升！！！
适合多种场合的强力武器
结束于2月25日 07:00
▸查看详情
  ''',),
            "zhotw": (
                '''
==========
女武神手刀
碎星大劍
==========
以上武器出現概率提升！！！
適合多種場合的強力武器
結束於2月25日 07:00
▸查看詳情
  '''
            ,),
            "engus": (
                '''
==========
Hand of Malenia
Starscourge greatsword
==========
DISPLAYED WEAPONS - RATE UP !!!
Rate weapons usefull in all kinds of stages
End at 07:00, 2/25
▸Details
  '''
            ,)
    }

}

# 拼凑 xml 路径:
for lang in langs:

  langNamePathPart = lang + pathPart + lang[0:-2]+lang[-2:]
  fmgFileName = list(map(lambda x: x + ".fmg", i18nData.keys()))
  xmlFileName = list(map(lambda x: x + ".xml", fmgFileName))

  unModifBasePathBase = unModifBasePath + langNamePathPart
  workPlacePathBase = workPlacePath + langNamePathPart

  unModXMLPath = list(map(lambda x: os.path.join(unModifBasePathBase, x), xmlFileName))
  unModFMGPath = list(map(lambda x: os.path.join(unModifBasePathBase, x), fmgFileName))
  workPlaceXMLPath = list(map(lambda x: os.path.join(workPlacePathBase, x), xmlFileName))
  workPlaceFMGPath = list(map(lambda x: os.path.join(workPlacePathBase, x), fmgFileName))

  for index in range(len(fmgFileName)):
    currXMLPath = workPlaceXMLPath[index]
    os.system(yabberPath + " "+'"{}"'.format(unModFMGPath[index]))
    shutil.copyfile(unModXMLPath[index], currXMLPath)

    # collect i18n
    document = xml.dom.minidom.parse(currXMLPath)
    nodes = document.documentElement.getElementsByTagName("entries")[0].childNodes
    nodesTextNode = []
    nodesId = []
    nodesData = []
    # 收集已有id 与数据
    for node in nodes:
      if len(node.childNodes) == 0:
        # 为 \n 节点
        continue
      else:
        nodesTextNode.append(node)
        nodesId.append(node.getAttribute('id'))
        nodesData.append(node.childNodes[0].data)
    # add new i18n

    # 添加条目到event msg for talk
    entriesNode = document.documentElement.getElementsByTagName("entries")[0]

    tempLang = lang
    currData = i18nData[list(i18nData.keys())[index]]
    if lang not in currData.keys():
      tempLang = "engus"
    textIds = currData['id']
    for id in textIds:
      newNode = document.createElement("text")
      newNode.appendChild(document.createTextNode(currData[tempLang][textIds.index(id)]))
      newNode.setAttribute("id", str(id))
      entriesNode.insertBefore(
          newNode, nodes[len(nodes)-1])

    # 覆写文件
    # backup
    shutil.copyfile(currXMLPath, currXMLPath + ".bak")
    with open(currXMLPath, 'w', encoding="utf-8") as f:
        # document.writexml(f,newl="\n")

        # 多周目提示字符被替换
        # f.write(html.unescape(document.toxml()))
      f.write(document.toxml().replace("&quot;", "\""))
    # yabber repack one xml
    os.system(yabberPath + " "+'"{}"'.format(currXMLPath))
  # repack hold menu
  os.system(yabberPath + " "+'"{}"'.format(os.path.join(workPlacePath, lang, "menu-msgbnd-dcx")))

  # remove folder
  shutil.rmtree(os.path.join(workPlacePath, lang, "menu-msgbnd-dcx"))
  print("done of {}".format(lang))

  #copy to mod test path
  modBuildPath = 'E:\Temp\ELDEN RING\Game\mod\gacha-ring\msg'
  shutil.rmtree(modBuildPath)
  shutil.copytree(workPlacePath, modBuildPath)
