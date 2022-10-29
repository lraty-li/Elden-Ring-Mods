# Comic miniature ranni

create a new item with item ID 30000, icon ID 609. replaced item icon from Asimi quest.

add a new row to regulation.bin in ItemLotParam_map row id 30131 to let Bloodhound Knight Darriwil drop item.

## Install

Because the packed 01_common.tpf.dcx and 00_solo.tpfbdt will reach about 1GB, only texture provided inside menu folder(.dds)

You will need to unpack your game to acquire other necessary file:

- unpack menu from your game using [UXM-Selective-Unpack](https://github.com/Nordgaren/UXM-Selective-Unpack/releases)
  
  - click "View Files"

  - chose "00_solo.tpfbdt", "00_solo.tpfbhd", "01_common.tpf.dcx" under "menu\hi" (i'm not sure when will game use texture from "menu\low", but replace file in "menu\hi" workable)
- after the UXM-Selective-Unpack finish, you should be able to find menu folder in your game exe folder, then using [Yabber](https://github.com/JKAnderson/Yabber) to unpack dcx file

  - drag "00_solo.tpfbhd", "01_common.tpf.dcx" to Yabber.exe, then yabber will unpack file into "00_solo-tpfbhd" and "01_common-tpf-dcx" folder
- replace the texture file

  - replace SB_Icon_01.dds inside "01_common-tpf-dcx"

  - go to "00_solo-tpfbhd\00_Solo\" find "MENU_Knowledge_00609.tpf.dcx", and drag to Yabber.exe

  - replace "MENU_Knowledge_00609.dds" inside "00_solo-tpfbhd\00_Solo\MENU_Knowledge_00609-tpf-dcx"

- go back to "menu\hi", drag "01_common-tpf-dcx" and "00_solo-tpfbhd" to Yabber, then you will get the modified "00_solo.tpfbdt", "00_solo.tpfbhd", "01_common.tpf.dcx"
