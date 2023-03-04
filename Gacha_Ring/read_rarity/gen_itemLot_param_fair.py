
from read_xlsx import dumpDataFromXlsx
from read_csv import loadParam
from functools import reduce
import random
import pickle

lotIdCounter = 200010  # random set flag 总是会设置一个


if __name__ == '__main__':
  awards = []
  with open('./classfied', 'rb') as file:
    awards = pickle.load(file)
  allCsvLines = []




  try:
    while 1:
      allCsvLines += genCsvData(awards['common'])
      allCsvLines += genCsvData(awards['rare'])
      allCsvLines += genCsvData(awards['default'])
      allCsvLines += genCsvData(awards['legendary'])
      if(lotIdCounter >= 363850):
        break
  except Exception:
    pass

  #
  # not random enought, re arrange
  print(len(allCsvLines))
  allCsvLines = allCsvLines[:16384]
  # random.shuffle(allCsvLines)
  tempLotId = 200010

  rateRecord = {line.split(';')[1] : [0, []] for line in allCsvLines}

  for index in range(len(allCsvLines)):
    line = allCsvLines[index]
    allCsvLines[index] = str(tempLotId) + line[6:]
    tempLotId += 10
    # calc rate
    itemName = line.split(';')[1]
    itemID = line.split(';')[2]
    rateRecord[itemName][0] += 1
    if(itemID not in rateRecord[itemName][1]):
      rateRecord[itemName][1].append(itemID)


  rates = []
  repeates = []
  for itemName in rateRecord:
    if(len(rateRecord[itemName][1]) > 1):
      repeates.append((itemName, rateRecord[itemName][1]))
    frequency = rateRecord[itemName][0]
    rates.append((itemName, frequency/len(allCsvLines)* 100))
  rates = sorted(rates, key = lambda x : (x[1], x[0]))

  # gen repeat csv for test
  # csv = []
  # emevd = []
  # for entry in repeates:
  #   for itemId in entry[1]:
  #     csv.append(template.format(lotIdCounter, entry[0], itemId, itemTypeMap['EquipParamGoods']))

  #     emevd.append('SetEventFlagID(1062265999, OFF);')
  #     emevd.append('AwardItemLot({});'.format(lotIdCounter))
  #     lotIdCounter += 10

  # with open( 'temp_csv' + '.txt', 'w+', encoding='utf8') as file:
  #   file.writelines(line + '\n' for line in csv)
  # with open( 'temp_emevd' + '.txt', 'w+', encoding='utf8') as file:
  #   file.writelines(line + '\n' for line in emevd)

  fileName = 'output_fair'
  
  with open( fileName + '.txt', 'w+', encoding='utf8') as file:
    file.writelines(line + '\n' for line in allCsvLines)
  with open( 'rate_' + fileName + '.txt', 'w+', encoding='utf8') as file:
    file.writelines([ '{:.3f}% {} {}'.format(line[1], line[0], '\n') for line in rates])
  print("DONE")
