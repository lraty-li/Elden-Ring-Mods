import os
import shutil
from common import *

unModifBasePath=r"E:/Temp/ELDEN RING/Game/msg"
workPlacePath = "D:/Game/ERModing/WorkPlace/gacha_ring/script/read_rarity/names_all"

shutil.rmtree(workPlacePath)
os.makedirs(workPlacePath)

# 拼凑 xml 路径:
for lang in langs:
  workPlaceLangFolder = os.path.join(workPlacePath, lang)
  if not os.path.exists(workPlaceLangFolder):
    os.makedirs(workPlaceLangFolder)
  os.system(yabberPath +" "+'"{}"'.format(unModifBasePath + "/" +lang+"/"+"item.msgbnd.dcx"))
  for fileName in msgNameFile:
    fmgPath = os.path.join(unModifBasePath, lang, r'item-msgbnd-dcx/GR/data/INTERROOT_win64/msg', lang[0:-2]+lang[-2:].upper(), fileName + '.fmg')
    xmlPath = fmgPath + '.xml'
    os.system(yabberPath +" "+'"{}"'.format(fmgPath))
    shutil.copyfile(xmlPath, os.path.join(workPlaceLangFolder, fileName + '.fmg.xml'))

#  复制到工作目录


