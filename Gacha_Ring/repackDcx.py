import os
import shutil

## *** 当需要更新：
## 删除esdtoolconfig.json，重新指定regulation.bin的位置

gamePath="\"E:\Temp\ELDEN RING\Game\""
esdToolPath=r"D:\Game\ERModing\esdtool-v0.3\esdtool.exe"
yabberPath=r"D:\Game\ERModing\Yabber.1.3.1\Yabber.exe"



pathBase=r"D:\Game\ERModing\WorkPlace\gacha_ring\script"


# writeloose="D:/Game/ERModing/WorkPlace/gacha-ring/script/%e.esd"
# esdParamsTest=esdToolPath+" -er -basedir "+gamePath+r" -backup -i D:\Game\ERModing\WorkPlace\gacha-ring\script\t000001000.py -writeloose "+writeloose

fileTargets=["t000001000.py"]


# py to esd file

allfileTargets=""
for fileName in fileTargets:
    allfileTargets=allfileTargets+" "+pathBase+"/"+fileName
#注意不要多空格
#D:\Game\ERModing\esdtool-v0.3\esdtool.exe D:\Game\ERModing\WorkPlace\gacha_ring\script\t000001000.py
py2EsdCMD = esdToolPath +allfileTargets

try:
  os.system(py2EsdCMD)
except Exception as e:
  print(e)



# copy esd file to, 与其他esd 文件合并为dcx
dstPath = r"E:\Temp\ELDEN RING\Game\script\talk\m00_00_00_00-talkesdbnd-dcx\GR\data\INTERROOT_win64\script\talk\m00_00_00_00"


for fileName in fileTargets:
    shutil.move(os.path.join(pathBase,fileName[0:-3]+".esd"),dstPath+"\\"+fileName[0:-3]+".esd")


# gen dcx
targetFolder=r'"E:\Temp\ELDEN RING\Game\script\talk\m00_00_00_00-talkesdbnd-dcx"'

try:
  os.system(yabberPath +" "+targetFolder)
except Exception as e:
  print(e)

# copy dcx to 
srcDcxFile=r"E:\Temp\ELDEN RING\Game\script\talk\m00_00_00_00.talkesdbnd.dcx"
# targetModPath=r"D:\Game\ERModing\Collected\1.06\mod\Chat-With-Melina-Mod\script\talk\m00_00_00_00.talkesdbnd.dcx"
targetModPath =r"E:\Temp\ELDEN RING\Game\mod\gacha-ring\script\talk\m00_00_00_00.talkesdbnd.dcx"

try:
  if os.path.exists(targetModPath):
    os.remove(targetModPath)  
  shutil.move(srcDcxFile,targetModPath)
except Exception as e:
  print(e)

