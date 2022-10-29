import os
import shutil
modRootPath="./modBuild"


langs=["deude","frafr","itait","jpnjp","korkr","polpl","porbr","rusru","spaar","spaes","thath","engus","zhocn","zhotw"]
# 最后两位大写

basePath="E:/Steam/steamapps/common/ELDEN RING/Game/msg-bak/msg/"

if not os.path.exists(modRootPath):
    os.makedirs(modRootPath)
    
for lang in langs:
    if not os.path.exists(modRootPath+"/msg/{}".format(lang)):
        os.makedirs(modRootPath+"/msg/{}".format(lang))
    
    # 复制menu.msgbnd.dcx文件到此处
    shutil.copyfile("{}".format(basePath+lang+"/menu.msgbnd.dcx"),modRootPath+"/msg/"+lang+"/menu.msgbnd.dcx")