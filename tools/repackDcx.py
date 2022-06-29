import os
import shutil

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

os.system(py2EsdCMD)



# copy esd file to
dstPath = r"E:\Steam\steamapps\common\ELDEN RING\Game\script\talk\m00_00_00_00-talkesdbnd-dcx\GR\data\INTERROOT_win64\script\talk\m00_00_00_00"
for fileName in fileTargets:
    shutil.move(pathBase+"\\"+fileName[0:-3]+".esd",dstPath+"\\"+fileName[0:-3]+".esd")




# gen dcx
targetFolder=r'"E:\Steam\steamapps\common\ELDEN RING\Game\script\talk\m00_00_00_00-talkesdbnd-dcx"'

os.system(yabberPath +" "+targetFolder)

# copy dcx to 
srcDcxFile=r"E:\Steam\steamapps\common\ELDEN RING\Game\script\talk\m00_00_00_00.talkesdbnd.dcx"
targetModPath=r"E:\Steam\steamapps\common\ELDEN RING\Game\mod\Chat-With-Melina-Mod\script\talk\m00_00_00_00.talkesdbnd.dcx"
shutil.move(srcDcxFile,targetModPath)
