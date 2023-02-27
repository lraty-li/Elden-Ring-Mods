# combining mod

## Attention

- The following may mention the certain lines of files, but by the time you see this note the file may have changed and I forgot to update it. Note the date the file was modified.

- files could be found on mod's page or [github](https://github.com/lraty-li/Elden-Ring-Mods/tree/main/Gacha_Ring) DOC folder

## file

The files involved are as follows: If the mod you need to merge does not use some of the files, you may not need to merge manually

- event/common.emevd.dcx adds events to generate a random number by waiting for the esd setting flag bit and playing animation

-script /talk/m00_00_00_00.talkesdbnd.dcx adds grace menu options, item consumption, soul check, lot items

- msg/{lang}/menu.msgbnd.dcx site menu options' text

- menu/hi/00_solo.tpfbdt and menu/hi/00_solo.tpfbhd display the image in Details

- regulation.bin
  - tutorialParam has modified row 1 to show the picture in details
  - itemLotParam_map Added row 200000-281910 for dropping various items

## Required software

[UXM-Selective-Unpack](https://github.com/Nordgaren/UXM-Selective-Unpack/releases/tag/2.1.7.1)

[DarkScript](https://github.com/AinTunez/DarkScript3/releases)

[Yabber](https://github.com/JKAnderson/Yabber/releases/tag/1.3.1)

[esdtool](https://github.com/thefifthmatt/ESDLang/releases/tag/v0.3)

[Yapped-Rune-Bear](https://github.com/vawser/Yapped-Rune-Bear/releases/tag/2.14.1)

## emevd

### Check whether event ids conflict

id 9970, 9971, 9972, 9973 are used. If the mod you want to merge already uses some of them, you need to ctrl f to find and change them all to any other number. The same goes for the other step

### Adds the initialization for the new event

emved is responsible for handling various events in the game, each of which is similar Structure of

``` javascript
$Event(event id, Default, function() {
...
code
...
});
```

open common.emevd.dcx using DarkScript, add the contents of emevd_0.txt to common.emevd.dcx's ```$Event(0,),``` noting that added to the function in the argument, After adding it, it will look like this:

<https://github.com/lraty-li/Elden-Ring-Mods/blob/main/Gacha_Ring/emved/common.emevd.dcx.js#L372>

``` javascript
$Event(event id, Default, function() {
...
InitializeEvent(0, 9970, 0);
InitializeEvent(0, 9971, 0);
InitializeEvent(0, 9973, 0);
...
});
```

### Added mod new events

Add the contents of emevd_1.txt to common.emevd.dcx, which you can scroll to the bottom of the document with DarkScript, and then paste directly. These are independent new events, dont added to other events as in the previous step.

### Save

ctrl + s in DarkScript

## esd

### Get t000001000.py

Drag script/talk/m00_00_00_00.talkesdbnd.dcx to Yabber.exe, you should get folder m00_00_00_00_-Talkesdbnd-dcx, go into folder, Drag t000001000.esd to esdtool.exe, enter the configuration as prompted, and it will be decompiled to t000001000.py

### grace menu options

You need to add the contents of t000001000.py_0.txt to ```def t000001000_x31():``` before ```AddTalkListData(99, 20000009, -1)```. **Note that Python uses indentation to distinguish code blocks**. You can add this by making the two lines align. ```AddTalkListData(99, 20000009, -1)``` is the "away" button of the game itself, hopefully other mods haven't modified it

This file contains code from previous mods, so don't worry about the commented out parts
<https://github.com/lraty-li/Elden-Ring-Mods/blob/main/Gacha_Ring/t000001000.py#L1098>

```python
        AddTalkListData(24, 30000000, -1)
        AddTalkListData(99, 20000009, -1)
```

### Raffle menu

Also in the rage of  ```def t000001000_x31():```, add the contents of t000001000.py_1.txt before  ```elif GetTalkListEntryResult() == 2```

<https://github.com/lraty-li/Elden-Ring-Mods/blob/main/Gacha_Ring/t000001000.py#L1135>

``` python
        # gacha ring
        elif GetTalkListEntryResult() == 24:
            c1_140(0)
            c1_110()

            def ExitPause():
                c1_110()
            assert t000001000_x2233()
            pass
            
        # ============================
        elif GetTalkListEntryResult() == 2:
          # upgrade
```

### Item/Soul check, item drop

add the contents of t000001000.py_2.txt directly to common.emevd.dcx, you scroll to the bottom of t000001000.py and paste it directly.

## regulation.bin

### Add tutorialParam

This is not necessary, just to display the picture

- search tutorialParam in Yapped-Rune-Bear and set the parameters of row 1 to:

``` csv
disableParam network test;   Do not check;
menuType;   100;
triggerType;   0;
repeatType;   1;
imageId;   300;
unlockEventFlagId;   1062265997;
textId;   12000;
displayMinTime;   1;
displayTime;   3;
```

- After editing, click on any other row and ctrl s to save

## Add itemLotParam_map

- open regulation.bin with Yapped-Rune-Bear, Export csv through Field - Export Data after itemLotParam_map has been selected with .
- Then go to the Yapped-Rune-Bear.exe folder, Projects\ExampleMod\CSV\ER find TutorialParam.csv, open it, copy and paste the contents of TutorialParam.txt to the end of the file.
- After itemLotParam_map has been selected in Yapped-Rune-Bear, import csv through Field-Import Data and save by ctrl s

## msg

### python script

https://github.com/lraty-li/Elden-Ring-Mods/blob/main/Gacha_Ring/msg_edit/syncUpMsg.py

This is a script for synchronizing files in all languages, if you know python, you can check this out

### Unpack

Drag menu.msgbnd.dcx to yabber.exe to unpack the fmg file. Drag EventTextForTalk.fmg, TutorialTitle.fmg, TutorialBody.fmg to yabber.exe to get various xml

### EventTextForTalk.fmg.xml

these are just to help you locate where to appending content. Don't just scroll to the end of document then copy and paste.

```xml
</entries>
</fmg> 
```

```xml
</files>
</bxf4>
```

Scroll to the end of the file and after appending it will look something like this:

```xml
<text id="30000000">Wish</text>
<text id="30000001">Wish x1</text>
<text id="30000002">Wish x10</text>
<text id="30000003">Insufficient runes</text>
<text id="30000004">1 Golden Rune [1] is needed. Purchase with 10% of runes needed to upgrade?</text>
<text id="30000005">10 Golden Rune [1] is needed. Purchase with 100% of runes needed to upgrade?</text>
<text id="30000006">Details</text>
</entries>
</fmg>
```

### TutorialBody.fmg.xml

``` xml
<text id="12000">
==========
Hand of Malenia
Starscourge greatsword
==========
DISPLAYED WEAPONS - RATE UP !!!
Rate weapons usefull in all kinds of stages
End at 07:00, 2/25
▸Details
</text>
</entries>
</fmg>
```

### TutorialTitle.fmg.xml

```xml
<text id="12000">The Battle of Aeonia</text>
</entries>
</fmg>
```

### Pack

Do the reverse, drag the xml to yabber, and then drag the menu-msgbnd-dcx to yabber

## menu

This part is optional

### Unpack

Drag menu\hi\00_solo.tpfbhd to yabber.exe to unpack 00_solo.tpfbdt.

### Added tutorial images

You can find MENU_Tuto_00300.tpf.dcx in the optional files on the mod page and place it in 00_solo-tpfbhd\00_Solo. Then edit _yabber-bxf4.xml in folder 00_solo-tpfbhd and append to the end of the document, will look like this

```xml
<file>
<flags>0x40</flags>
<id>2428</id>
<root />
<path>00_Solo\MENU_Tuto_00300.tpf.dcx</path>
</file>
</files>
</bxf4>
```

### Pack

drag 00_solo-tpfbhd folder to yabber.exe

## links

http://soulsmodding.wikidot.com/tutorial:intro-to-elden-ring-emevd
