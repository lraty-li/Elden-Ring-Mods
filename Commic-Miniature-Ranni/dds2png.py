import os
import shutil


ddsRootPath = "allDDS"
outPutPath = "pngs"
texconvPath = "texconv.exe"

ddsFiles = os.listdir(ddsRootPath)

if not os.path.exists(outPutPath):
  os.mkdir(outPutPath)

for ddsFile in ddsFiles:
  os.system(texconvPath +" "+ os.path.join(ddsRootPath, ddsFile) + " " + "-ft png")
  pngName = "{}".format(ddsFile)
  pngName = pngName.replace(".dds", ".png")
  os.rename(os.path.join(pngName), os.path.join(outPutPath, pngName))
  os.remove(os.path.join(ddsRootPath, ddsFile))


