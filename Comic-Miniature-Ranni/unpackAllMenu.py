import os
import shutil

yabberPath = r"D:\Game\ERModing\Yabber.1.3.1\Yabber.exe"

dcxsFolder = os.path.join("menu", "hi", "00_solo-tpfbhd", "00_Solo")
allDdsFolder = "allDDS"
outPut = "./pngs"

for dcxFile in os.listdir(dcxsFolder):
    folderName = "{}".format(dcxFile)
    folderName = folderName.replace(".", "-")
    unPackedDcxFolder = os.path.join(dcxsFolder, folderName)
    os.system(yabberPath + " " + os.path.join(dcxsFolder, dcxFile))

    # got a -dcx folder
    ddsFiles = os.listdir(unPackedDcxFolder)
    for ddsFile in ddsFiles:
        if not ddsFile.find(".dds") == -1:
            print(os.path.join(unPackedDcxFolder, ddsFile),
                  os.path.join(allDdsFolder, ddsFile))
            os.rename(os.path.join(unPackedDcxFolder, ddsFile),
                      os.path.join(allDdsFolder, ddsFile))

    shutil.rmtree(unPackedDcxFolder)
