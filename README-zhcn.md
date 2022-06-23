# EldenRingMod-chat-with-Melina

让玩家能够在赐福与梅琳娜聊天的mod

## 警告

跟梅琳娜聊天的时候**不要突然关闭游戏**，因为在聊天时mod通过修改(进入对话后能够确定值的)某些事件标志位来达成分辨选项的目的，如果在对话未结束，未复原标志位，理论上会导致游戏存档进度不正确。(在未来摸清更多even flag 比如未使用的后会改进)

## 安装

推荐使用 [modEngine2](https://github.com/soulsmods/ModEngine2) 安装

## 能够聊天的进度

与梅琳娜达成约定后 ~ 王城分离前
击败噩兆后重新会合 ~ 被发现接受癫火/烧树

## 聊天条目

条目(例如箴言)需要被 "与梅琳娜交谈" 触发过才能在聊天界面选择,目前一共有17句对话(实际在游戏中最多能看到16句)。

## 修改的对话脚本

```xml
script\talk\m00_00_00_00-talkesdbnd-dcx\GR\data\INTERROOT_win64\script\talk\m00_00_00_00

t000001000.py
t000003000.py
```

## 新增的文本ID (EventTextForTalk)

除了中文简体、中文繁体，其他语言版本的聊天选项都设置为英文翻译。如果你想新增翻译,请看```intl``` 文件夹, 只需要翻译70000000 到 70000000 70000002 即可，剩余文本来自游戏对话。

```xml
msg\zhocn\menu-msgbnd-dcx\GR\data\INTERROOT_win64\msg\zhoCN\EventTextForTalk.fmg.xml
```

``` xml
<text id="70000000">召唤梅琳娜</text>
<text id="70000001">遣返梅琳娜</text>
<text id="70000002">和梅琳娜聊天</text>

<text id="70000100">%null%</text>
<text id="70000101">"……关于我吗？"</text>
<text id="70000102">"…我直接复诵玛莉卡的箴言"</text>
<text id="70000103">"…我直接复诵玛莉卡的箴言"</text>
<text id="70000104">"…我直接复诵玛莉卡的箴言"</text>
<text id="70000105">"…我直接复诵玛莉卡的箴言"</text>
<text id="70000106">"…我直接复诵玛莉卡的箴言"</text>
<text id="70000107">"…我直接复诵玛莉卡的箴言"</text>
<text id="70000108">"…我直接复诵玛莉卡的箴言"</text>
<text id="70000109">"……"</text>
<text id="70000110">"……"</text>
<text id="70000111">"…你不用担心火种"</text>
<text id="70000112">"…这簇小巧的金光…"</text>
<text id="70000113">"…我想告诉你一件事"</text>
<text id="70000114">"…如果你的心向着癫火"</text>
<text id="70000115">"…我会准备火种…"</text>
<text id="70000116">"…我再说一次──"</text>
<text id="70000117">"拜托你了，能不能悬崖勒马？"</text>
```

## TODO

- 处理其他语言的具体对话选项(由talkMsg获得)
- 只检查是否通过梅琳娜烧树，即使癫火仍然允许聊天？
- 因为不知道如何检查玩家持有的骨灰，目前的仿身泪滴废案对话 ```<text id="70000109">"……"</text>``` 和 ```<text id="70000110">"……"</text>``` 主要通过检查是否持有猎杀指头刀触发，然而随着流程推进，玩家会失去该物品。

## mod 实现

为什么不能突然关闭游戏?
TBC

## 聊天选项与具体文本的对应关系

TBC

## 其他(与mod无关)

### 被跳过的文本

在击败王城噩兆后与梅琳娜的对话中，下面的文本 ```<text id="100140010">```的文本是被跳过的(也没有对应语音)。

```xml
<text id="100140000">……好久不见了。</text>
...
<text id="100140010">你还记得我吗？我是梅琳娜。</text>
...
<text id="100140020">我想和你聊一聊。</text>
```

### 不同称呼

根据是否持有洛德符节，梅琳娜会将与玩家一同前进区分称呼为"约定(前往黄金树根脚)"或者"旅行(前往火焰大锅)"，仿身泪滴废案也如此，这也是为什么最多只能看到16句对话。

## 鸣谢

- FromSoftware
- the [?ServerName? discord](https://discord.gg/97qU4236)
- [JKAnderson's UXM](https://github.com/JKAnderson/UXM) and [Nordgaren's selective UXM](https://github.com/Nordgaren/UXM-Selective-Unpack) and elden ring's version form ?ServerName? discord
- [Yabber](https://github.com/JKAnderson/Yabber)
- [souls Mod engine2](https://github.com/soulsmods/ModEngine2)
- [edstools](https://github.com/thefifthmatt/ESDLang)
