# from wand import image
import shutil
from PIL import Image
import os

yabberPath = r"D:\Game\ERModing\Yabber.1.3.1\Yabber.exe"
aetRootPath = os.path.join("asset", "aet")
allDdsFolder = "allDDS"
outPut = "./pngs"

if os.path.exists(allDdsFolder):
  shutil.rmtree(allDdsFolder)
os.makedirs(allDdsFolder)

# unpack all dcx


# aet000 aet001
aetXXXs = os.listdir(aetRootPath)

for aetXXXFolder in aetXXXs:
    aetXXXFolderPath = os.path.join(aetRootPath, aetXXXFolder)
    files = os.listdir(aetXXXFolderPath)
    for dcxFile in files:
        if dcxFile.find("_l.tpf") == -1 and dcxFile.find("-dcx") == -1:
            try:
                folderName = "{}".format(dcxFile)
                folderName = folderName.replace(".", "-")
                unPackedDcxFolder = os.path.join(
                    aetRootPath, aetXXXFolder, folderName)

                dcxFilePath = os.path.join(aetRootPath, aetXXXFolder, dcxFile)
                if not os.path.exists(unPackedDcxFolder):
                  os.system(yabberPath +" "+ dcxFilePath)

                # got a -dcx folder
                ddsFiles = os.listdir(unPackedDcxFolder)
                for ddsFile in ddsFiles:
                    if not ddsFile.find(".dds") == -1:
                        os.rename(os.path.join(aetRootPath, aetXXXFolder, folderName, ddsFile), os.path.join(
                            allDdsFolder, ddsFile))
                # shutil.rmtree(unPackedDcxFolder)
                # remove the dcx
                # os.remove(dcxFilePath)
                
            except Exception as e:
                print(e)
                print(e.__traceback__.tb_lineno)
                os._exit(0)
    shutil.rmtree(aetXXXFolderPath)
