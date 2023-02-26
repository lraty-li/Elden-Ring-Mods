# doc.xlsx
import re
import pickle
from openpyxl import load_workbook

# https://www.bilibili.com/read/cv19937910

workbooks = ['Unique Weapons IDs', 'Weapon IDs', 'Armor IDs', 'Item IDs', 'Spell IDs', 'Talisman IDs', 'AshesOfWar IDs']


def dumpAllId():
  workbook = load_workbook(filename="doc.xlsx")
  # workbook.worksheets

  gather = {}
  for sheetName in workbooks:
    sheet = workbook[sheetName]
    ids = []
    rowCouter = 1
    while True:
      aValue = sheet["{}{}".format("A", rowCouter)].value
      bValue = sheet["{}{}".format("B", rowCouter)].value
      rowCouter += 1
      # remove useless mamually
      if(aValue == None ):
        break
      if(aValue == 'ID'):
        continue
      if(bValue != None):
        ids.append((aValue, bValue))
      
    gather[sheetName] = ids

  with open('gather', 'wb') as file:
    pickle.dump(gather, file)


def genCsvData(iterable, lotIdCounter, typeId):
  csvLines = []
  template = "{};Gacha_Ring {};{};0;0;0;0;0;0;0;{};0;0;0;0;0;0;0;1000;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1062265999;0;0;-1;1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;-1;0;0;0;0;"
  for i in iterable:
    csvLines.append(template.format(lotIdCounter, i[1],str(int(i[0])), typeId))
    lotIdCounter += 10
  return csvLines


if __name__ == '__main__':
  dumpAllId()
  gather = {}
  with open('./gather', 'rb') as file:
    gather = pickle.load(file)


# .format(awarodItemLotId, itemName, itemId, itemType)
  lotIdCounter = 200000
  groups = [(gather['Unique Weapons IDs'] + gather['Weapon IDs'] + gather['Spell IDs'], 2), (gather['Armor IDs'], 3), (gather['Item IDs'], 1), (gather['Talisman IDs'], 4), (gather['AshesOfWar IDs'], 5)]

  allCsvLines = []
  for group in groups:
    csvLines = genCsvData(group[0], lotIdCounter, group[1])
    groupText = ""
    for line in csvLines:
      groupText += line + '\n'
    with open('output_{}.txt'.format(group[1]), 'w+', encoding='utf8') as file:
      file.write(groupText)
    allCsvLines.append(csvLines)
    lotIdCounter += len(csvLines)*10

  # spell = genCsvData(gather['Spell IDs'], lotIdCounter, 2)

  allCsvText = ""
  for i in allCsvLines:
    for j in i:
      allCsvText += j + '\n'
  # 补齐 到 8192 281910 
  # lotIdCounter += 10
  csvLines = genCsvData(groups[2][0], lotIdCounter, groups[2][1])
  lotIdCounter += len(csvLines)*10
  for line in csvLines:
    allCsvText += line + '\n'
  # 剩余的都设置为玛莲妮娅手刀 和 碎星大剑
  for i in range(0,int((281910 - lotIdCounter)/20)):
    allCsvText += "{};Gacha_Ring {};{};0;0;0;0;0;0;0;{};0;0;0;0;0;0;0;1000;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1062265999;0;0;-1;1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;-1;0;0;0;0;".format(lotIdCounter, "Starscourge Greatsword", 4050000,2) + '\n'
    lotIdCounter += 10
  while lotIdCounter<= 281910:
    allCsvText += "{};Gacha_Ring {};{};0;0;0;0;0;0;0;{};0;0;0;0;0;0;0;1000;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1062265999;0;0;-1;1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;-1;0;0;0;0;".format(lotIdCounter, "Hand of Malenia", 9020000,2) + '\n'
    lotIdCounter +=10



  with open('output.txt', 'w+', encoding='utf8') as file:
    file.write(allCsvText)
  print("DONE")
