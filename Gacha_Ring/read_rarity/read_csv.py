import csv
import pickle
import xml.dom.minidom
import os
from common import *

def loadNamesXml(currXMLPath):
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
  return dict(zip(nodesId, nodesData))


def loadParam():

  byPassTokens = ('＋',
            '厚重',
            '锋利',
            '优质',
            '火焰',
            '焰术',
            '雷电',
            '神圣',
            '魔力',
            '寒冷',
            '毒',
            '血',
            '神秘', '说明：')

  params = {}
  paramsWithName = {}
  paramsNoName = {}

  for fileName in csvParam:
    index = csvParam.index(fileName)
    names = loadNamesXml(os.path.join('names', msgNameFile[index] + '.fmg.xml'))
    csv_reader = csv.DictReader(open("./{}.csv".format(fileName)), delimiter=';')
    for line in csv_reader:
      # collect id, rarity
      rows = [row for row in csv_reader]
      rowIds = [row['Row ID'] for row in rows]
      rowRarity = [row['rarity'] for row in rows]
      values = [(rarity,) for rarity in rowRarity]
      if('goodsType' in rows[0].keys()):

        values = list(zip([rarity for rarity in rowRarity], [gType['goodsType'] for gType in rows]))
      params[fileName] = dict(zip(rowIds, values))
    temp = {}
    noName = []
    for k in params[fileName]:
      byPassFlag = False
      try:
        for byPassToken in byPassTokens:
          if byPassToken in names[k]:
            byPassFlag = True
            break
        if (names[k] == '[ERROR]' or byPassFlag):
          continue
        temp[k] = [names[k], params[fileName][k]]
      except Exception as e:
        noName.append(k)
    paramsWithName[fileName] = temp
    paramsNoName[fileName] = noName
  with open('idRarity', 'wb') as file:
    pickle.dump(paramsWithName, file)
  return paramsWithName


if __name__ == '__main__':
  loadParam()
