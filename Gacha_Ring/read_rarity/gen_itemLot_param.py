
from read_xlsx import dumpDataFromXlsx
import os
from functools import reduce
import random
import pickle
import json
from common import *
import shutil

if __name__ == '__main__':
  awards = []
  allNames = {k : readNames('names_all\{}'.format(k)) for k in langs }
  with open('./classfied', 'rb') as file:
    awards = pickle.load(file)
  allCsvLines = []

  #  all : 0 - 16384
  # legend 131 1.6% *2
  allCsvLines += genCsvData(awards['legendary'])
  allCsvLines += genCsvData(awards['legendary'])
  allCsvLines += genCsvData(awards['legendary'])
  allCsvLines += genCsvData(awards['legendary'])

  # rare
  # 13% - > 26%
  allCsvLines += genCsvData(awards['rare'])
  allCsvLines += genCsvData(awards['rare'])
  allCsvLines += genCsvData(awards['rare'])
  allCsvLines += genCsvData(awards['rare'])  # len = 836
  allCsvLines += genCsvData(awards['rare'])
  allCsvLines += genCsvData(awards['rare'], 80)  # 从0开始，导致靠后的概率比较低

  # common
  allCsvLines += genCsvData(awards['common'])  # len = 836
  allCsvLines += genCsvData(awards['common'])
  allCsvLines += genCsvData(awards['common'])
  allCsvLines += genCsvData(awards['common'])
  allCsvLines += genCsvData(awards['common'])
  allCsvLines += genCsvData(awards['common'])
  allCsvLines += genCsvData(awards['common'])
  allCsvLines += genCsvData(awards['common'], 538)

  # default
  allCsvLines += genCsvData(awards['default']) # 206
  allCsvLines += genCsvData(awards['default'])
  allCsvLines += genCsvData(awards['default'])
  allCsvLines += genCsvData(awards['default'])
  allCsvLines += genCsvData(awards['default'])
  allCsvLines += genCsvData(awards['default'])

  print("len(allCsvLines) before fill", len(allCsvLines))


  try:
    while 1:
      for id in tempFillerGoods.keys():
        allCsvLines.append(template.format(lotIdCounter, tempFillerGoods[id], id, itemTypeMap['EquipParamGoods']))
        if(lotIdCounter >= 363850):
          raise EOFError
        lotIdCounter += 10

      for id in tempFillerWeapons.keys():
        allCsvLines.append(template.format(lotIdCounter, tempFillerWeapons[id], id, itemTypeMap['EquipParamWeapon']))
        if(lotIdCounter >= 363850):
          raise EOFError
        lotIdCounter += 10
  except Exception:
    pass

  #
  # not random enought, re arrange
  allCsvLines = allCsvLines[:16384]
  random.shuffle(allCsvLines)
  tempLotId = 200010
  # name : [freq, ids, itemType]
  rateRecord = {line.split(';')[1] : [0, [], line.split(';')[10]] for line in allCsvLines}

  for index in range(len(allCsvLines)):
    line = allCsvLines[index]
    allCsvLines[index] = str(tempLotId) + line[6:]
    line = allCsvLines[index]
    tempLotId += 10

    itemName = line.split(';')[1]
    itemID = line.split(';')[2]
    itemType = line.split(';')[10]
    # calc rate
    rateRecord[itemName][0] += 1
    if(itemID not in rateRecord[itemName][1]):
      rateRecord[itemName][1].append(itemID)



  rates = []
  repeates = []

  for itemName in rateRecord:
    entry = rateRecord[itemName]
    frequency = entry[0]
    ids = entry[1]
    itemType = entry[2]

    if(len(ids) > 1):
      repeates.append((itemName, ids))
    # name, rate, itemType, ids
    rates.append((itemName, frequency/len(allCsvLines)* 100, itemType , ids))
  rates = sorted(rates, key = lambda x : (x[1], x[0]))

  # generate eng name rate
  # names in other lang
  ratesAllLang = {}
  for lang in allNames.keys():
    ratesAllLang[lang] = [ (allNames[lang][itemTypeMapReversed[i[2]]][i[3][0]], i[1]) for i in rates]


  
  fileName = 'output'

  ratesOutputFolder = 'rate_' + fileName
  if os.path.exists(ratesOutputFolder):
    shutil.rmtree(ratesOutputFolder )
  os.mkdir(ratesOutputFolder)
  for lang in ratesAllLang:
    with open( os.path.join(ratesOutputFolder, lang + '.txt'), 'w+', encoding='utf8') as file:
      file.writelines(['{:.3f}% {} {}'.format(line[1], line[0], '\n') for line in ratesAllLang[lang]])


  with open(fileName + '.txt', 'w+', encoding='utf8') as file:
    file.writelines(line + '\n' for line in allCsvLines)
  with open( 'rate_' + fileName + '.txt', 'w+', encoding='utf8') as file:
    file.writelines([ '{:.3f}% {} {}'.format(line[1], line[0], '\n') for line in rates])
  print("DONE")


  # duplicate check
  # temp = []
  # for lien in allCsvLines:
  #   temp.append(lien[:6])
  # for j in temp:
  #   count = temp.count(j)
  #   if count > 1:
  #     print(j)
