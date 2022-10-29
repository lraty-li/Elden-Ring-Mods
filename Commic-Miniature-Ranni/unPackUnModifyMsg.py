import os


yabberPath=r"D:\Game\ERModing\Yabber.1.3.1\Yabber.exe"
langs=["deude","frafr","itait","jpnjp","korkr","polpl","porbr","rusru","spaar","spaes","thath","engus","zhocn","zhotw"]

unModifBasePath="E:/Steam/steamapps/common/ELDEN RING/Game/msg/"

targetDcxFileName = "item.msgbnd.dcx"

# 拼凑 xml 路径:
for lang in langs:
    os.system(yabberPath +" "+'"{}"'.format(unModifBasePath+lang+"/"+targetDcxFileName))
