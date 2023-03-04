import json
from read_csv import loadParam
from functools import reduce
import pickle

if __name__ == '__main__':
  idRarity = []
  with open('./idRarity', 'rb') as file:
      idRarity = pickle.load(file)
  idRarity = loadParam()
 
  # idRarityPair = reduce(merge, [idRarity[i] for i in idRarity])

  # classfy items
  # 0 - default ; 291
  # 1 - common ; 3463
  # 2 - rare ; 1278
  # 3 - legendary ; 248


  itemRarityCategory = [0, 1, 2, 3]
  itemRarityCategoryName = ['default', 'common', 'rare', 'legendary']
  classfied = {}
  for rarity in itemRarityCategory:
    rarityName = itemRarityCategoryName[itemRarityCategory.index(rarity)]
    classfied[rarityName] = {}
    counter = 0
    for category in idRarity:
      classfied[rarityName][category] = {}
      # 屎山覆屎山
      for id in idRarity[category].keys():
        if idRarity[category][id][1][0] == str(rarity):
          if len(idRarity[category][id][1]) == 1:
            classfied[rarityName][category][id] = (idRarity[category][id][0], )
          else:
            classfied[rarityName][category][id] = (idRarity[category][id][0], idRarity[category][id][1][1])
          counter += 1
    classfied[rarityName]['sum'] = counter
  with open('./rarity_rar_sum.json', 'w', encoding='utf8') as file:
    file.write(json.dumps(classfied, ensure_ascii=False))
  with open('./classfied', 'wb') as file:
      idRarity = pickle.dump(classfied, file)
  print('DONE')
