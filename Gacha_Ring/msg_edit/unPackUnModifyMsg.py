import os
import shutil


yabberPath=r"D:\Game\ERModing\Yabber.1.3.1\Yabber.exe"
langs=["deude","frafr","itait","jpnjp","korkr","polpl","porbr","rusru","spaar","spaes","thath","engus","zhocn","zhotw"]

unModifBasePath=r"E:/Temp/ELDEN RING/Game/msg"
workPlacePath = "D:/Game/ERModing/WorkPlace/gacha_ring/script/msg_edit/msg"
# 拼凑 xml 路径:
# for lang in langs:
#     os.system(yabberPath +" "+'"{}"'.format(unModifBasePath + "/" +lang+"/"+"menu.msgbnd.dcx"))

#  复制到工作目录

# Copy src to dst. (cp src dst)
shutil.rmtree(workPlacePath)
shutil.copytree(unModifBasePath, workPlacePath)
