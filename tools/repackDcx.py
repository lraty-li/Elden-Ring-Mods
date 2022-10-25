import os
import shutil

## *** 当需要更新：
## 删除esdtoolconfig.json，重新指定regulation.bin的位置

gamePath="\"E:\Steam\steamapps\common\ELDEN RING\Game\""
esdToolPath=r"D:\Game\ERModing\esdtool-v0.3\esdtool.exe"
yabberPath=r"D:\Game\ERModing\Yabber.1.3.1\Yabber.exe"

writeloose=r"D:\Game\ERModing\Collected\WorkPlace\dialogueLogic\%e.esd"

pathBase=r"D:\Game\ERModing\Collected\WorkPlace\dialogueLogic"


esdParamsTest=esdToolPath+" -er -basedir "+gamePath+r" -backup -i D:\Game\ERModing\Collected\WorkPlace\dialogueLogic\t000001000.py D:\Game\ERModing\Collected\WorkPlace\dialogueLogic\t000003000.py -writeloose "+writeloose

fileTargets=["t000001000.py","t000003000.py"]


# py to esd file

allfileTargets=""
for fileName in fileTargets:
    allfileTargets=allfileTargets+" "+pathBase+"\\"+fileName
py2EsdCMD=esdToolPath +" "+allfileTargets

try:
  os.system(py2EsdCMD)
except Exception as e:
  print(e)



# copy esd file to, 与其他esd 文件合并为dcx
dstPath = r"D:\Game\ERModing\Collected\1.06\script\talk\m00_00_00_00-talkesdbnd-dcx\GR\data\INTERROOT_win64\script\talk\m00_00_00_00"


try:
  for fileName in fileTargets:
    shutil.move(pathBase+"\\"+fileName[0:-3]+".esd",dstPath+"\\"+fileName[0:-3]+".esd")
except Exception as e:
  print(e)


# gen dcx
targetFolder=r'"D:\Game\ERModing\Collected\1.06\script\talk\m00_00_00_00-talkesdbnd-dcx"'

try:
  os.system(yabberPath +" "+targetFolder)
except Exception as e:
  print(e)

# copy dcx to 
srcDcxFile=r"D:\Game\ERModing\Collected\1.06\script\talk\m00_00_00_00.talkesdbnd.dcx"
# targetModPath=r"D:\Game\ERModing\Collected\1.06\mod\Chat-With-Melina-Mod\script\talk\m00_00_00_00.talkesdbnd.dcx"
targetModPath =r"D:\Game\ERModing\Collected\WorkPlace\dialogueLogic\modBuild\m00_00_00_00.talkesdbnd.dcx"

try:
  if os.path.exists(targetModPath):
    os.remove(targetModPath)  
  shutil.move(srcDcxFile,targetModPath)
except Exception as e:
  print(e)

