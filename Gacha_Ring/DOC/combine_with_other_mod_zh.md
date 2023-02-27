# 合并mod

## 注意

- 以下内容中可能会提到某些文件的具体行数，但当你看到这份说明的时候文件可能已经改动而我忘记更新这里，注意对比文件的修改日期。

- 之后用到的文件可以在mod界面或者[github](https://github.com/lraty-li/Elden-Ring-Mods/edit/main/Gacha_Ring/DOC) 找到

## 文件

涉及到的文件有以下这些：如果你需要合并的mod并没有使用到其中的某些文件，也许你不需要手动进行合并

- event/common.emevd.dcx 添加等待esd设置标志位然后播放动画，生成随机数的事件

- script/talk/m00_00_00_00.talkesdbnd.dcx 添加赐福菜单选项，物品消耗，魂量检查，掉落物品

- msg/{lang}/menu.msgbnd.dcx 赐福菜单选项的文本

- menu/hi/00_solo.tpfbdt 和 menu/hi/00_solo.tpfbhd 用于显示 “详情”中的图片

- regulation.bin
  - tutorialParam 修改了row 1,显示详情中的图片
  - itemLotParam_map 新增row 200000 - 281910 ，用于掉落各种物品

## 要求软件

[UXM-Selective-Unpack](https://github.com/Nordgaren/UXM-Selective-Unpack/releases/tag/2.1.7.1)

[DarkScript](https://github.com/AinTunez/DarkScript3/releases)

[Yabber](https://github.com/JKAnderson/Yabber/releases/tag/1.3.1)

[Esdtools](https://github.com/thefifthmatt/ESDLang/releases/tag/v0.3)

[Yapped-Rune-Bear](https://github.com/vawser/Yapped-Rune-Bear/releases/tag/2.14.1)

## emevd

### 检查事件id是否冲突

id 9970, 9971, 9972, 9973 被使用到，如果你要合并的mod已经用到了其中的一些，你需要ctrl f 找到并全部修改成随便其他的数字。之后的步骤也是一样

### 添加新增的事件的初始化

emved 负责处理游戏中的各种事件，每一个事件有类似

``` javascript
$Event(事件id, Default, function() {
  ...
  代码
  ...
});
```

的结构

使用DarkScript 打开 common.emevd.dcx, 你需要将emevd_0.txt的内容添加到common.emevd.dcx的 ```$Event(0,``` 中，要注意是添加到其中的参数的function中，添加完之后看起来会是：

<https://github.com/lraty-li/Elden-Ring-Mods/blob/main/Gacha_Ring/emved/common.emevd.dcx.js#L372>

``` javascript
$Event(事件id, Default, function() {
  ...
    InitializeEvent(0, 9970, 0);
    InitializeEvent(0, 9971, 0);
    InitializeEvent(0, 9973, 0);
  ...
});
```

### 添加mod新增的事件

将emevd_1.txt的内容添加到common.emevd.dcx，你可以在DarkScript打开后拖到文档底部，然后直接粘贴，这些都是独立的新增的事件，不要像前一步一样加到其他事件中。

### 保存

在DarkScript中ctrl + s 即可

## esd

### 获取t000001000.py

拖拽 script/talk/m00_00_00_00.talkesdbnd.dcx 到 Yabber.exe ，你应该会得到m00_00_00_00-talkesdbnd-dcx文件夹，进入这个文件夹找到t000001000.esd，再将它拖动到esdtools.exe，根据提示输入配置，之后会反编译得到t000001000.py

### 赐福菜单选项

你需要将t000001000.py_0.txt的内容添加到 ```def t000001000_x31():``` 中的 ```AddTalkListData(99, 20000009, -1)``` 之前。**注意，Python使用缩进来区分代码块** ， 你可以这样添加：让这两行对齐。```AddTalkListData(99, 20000009, -1)```是游戏本身的“离开”按钮，希望其他mod没有对其修改

这个文件包含了以前mod的代码，不需要关心那些注释掉的部分

<https://github.com/lraty-li/Elden-Ring-Mods/blob/main/Gacha_Ring/t000001000.py#L1098>

```python
        AddTalkListData(24, 30000000, -1)
        AddTalkListData(99, 20000009, -1)
```

### 抽奖菜单

同样在```def t000001000_x31():```，将t000001000.py_1.txt的内容添加到```elif GetTalkListEntryResult() == 2:```之前

https://github.com/lraty-li/Elden-Ring-Mods/blob/main/Gacha_Ring/t000001000.py#L1135

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
          # 升级
```

### 物品/魂量检查，物品掉落

将t000001000.py_2.txt的内容直接添加到common.emevd.dcx，你拖动到t000001000.py的底部，然后直接粘贴。

## regulation.bin

### 添加tutorialParam

这不是必须的，只是用来显示图片

- 使用 Yapped-Rune-Bear，搜索tutorialParam， 将row 1 的参数分别设定为:

``` csv
  disableParam network test;  不勾选;
  menuType;  100;
  triggerType;  0;
  repeatType;  1;
  imageId;  300;
  unlockEventFlagId;  1062265997;
  textId;  12000;
  displayMinTime;  1;
  displayTime;  3;
```

- 编辑完之后，随便点击一下其他row再ctrl s 保存

### 添加itemLotParam_map

- 在Yapped-Rune-Bear选中itemLotParam_map之后，通过Field - Export Data 导出csv。
- 之后到 Yapped-Rune-Bear.exe 所在文件夹，Projects\ExampleMod\CSV\ER 找到 TutorialParam.csv，打开之后，将TutorialParam.txt 的内容复制粘贴到文件尾部。
- 在Yapped-Rune-Bear选中itemLotParam_map之后，通过Field - Import Data 导入csv，ctrl s 保存

## msg

### python 脚本

https://github.com/lraty-li/Elden-Ring-Mods/blob/main/Gacha_Ring/msg_edit/syncUpMsg.py

这是用来同步所有语言文件的脚本，如果你了解python，可以看看这个

### 解包

拖拽 menu.msgbnd.dcx 到 yabber.exe，解包出fmg文件。再将EventTextForTalk.fmg， TutorialTitle.fmg，TutorialBody.fmg 拖到 yabber.exe，得到各种的xml

### EventTextForTalk.fmg.xml

```xml
</entries>
</fmg> 这个部分只是为了方便你定位追加内容的位置，不要直接拉到最后复制粘贴，之后的追加也是这样。
```

滚动到到文件尾部追加完之后看起来会是这个样子：

```xml
<text id="30000000">祈愿</text>
<text id="30000001">祈愿一次</text>
<text id="30000002">祈愿十次</text>
<text id="30000003">所需卢恩不足</text>
<text id="30000004">黄金卢恩【1】不足，是否使用10%升级所需卢恩兑换</text>
<text id="30000005">黄金卢恩【1】不足，是否使用100%升级所需卢恩兑换</text>
<text id="30000006">详情</text>
</entries>
</fmg>
```

### TutorialBody.fmg.xml

``` xml
<text id="12000">
==========
女武神手刀
碎星大剑
==========
以上武器出现概率提升！！！
适合多种场合的强力武器
结束于2月25日 07:00
▸查看详情
  </text>
  </entries>
</fmg>
```

### TutorialTitle.fmg.xml

```xml
<text id="12000">艾奥尼亚战争</text>
</entries>
</fmg>
```

### 打包

反向进行以上的操作，拖拽xml到yabber，然后再将menu-msgbnd-dcx拖到yabber

## menu

这部分是可选的

### 解包

将 menu\hi\00_solo.tpfbhd 拖到 yabber.exe，会将00_solo.tpfbdt解包。

### 新增tutorial 图片

你可以在mod 页面的optional files 找到 MENU_Tuto_00300.tpf.dcx，将其放到00_solo-tpfbhd\00_Solo中，然后编辑 00_solo-tpfbhd 文件夹中的_yabber-bxf4.xml，在文档尾部追加

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

### 打包 

将 00_solo-tpfbhd 文件夹拖动到yabber.exe


## links

http://soulsmodding.wikidot.com/tutorial:intro-to-elden-ring-emevd
