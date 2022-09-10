# 代码解释

基于位于[draft文件夹](../draft/script-talk/)的代码，如果理解有错误请指正。

## 基础介绍

- 你需要了解二进制与十进制，以及[ESDLang](https://github.com/thefifthmatt/ESDLang)
- 该mod修改了两个文件:

  - t000001000.py文件主要关于当玩家在赐福处休息时显示的菜单。
    - 添加召唤/遣返梅琳娜，与梅琳娜聊天，以及具体聊天选项的二级菜单。
  - t000003000.py文件主要关于梅琳娜的具体对话调用。
    - 添加当在一个罕见的游戏进度下，进入mod对话流程的检测。


### 赐福菜单(t000001000.py)

``` python
t000001000_x31 
  |- t000001000_x52 
      |- t000001000_x43 
          |- t000001000_x46 (似乎没有具体作用)
          |- t000001000_x49
              |- t000001000_x57
              |- t000001000_x58
```

t000001000.py 中，t000001000_x31处理向赐福菜单添加选项（升级、大卢恩、分配元素瓶...）， 其中让t000001000_x52处理添加与梅琳娜交谈、与娇小拉妮交谈等等的选项，直到t000001000_x57才是比较具体处理添加梅琳娜相关对话的代码。

#### 添加菜单选项

``` xml
AddTalkListData(param1, param2, param3)
param1: 选择该选项后，GetTalkListEntryResult()的结果
param2: 对话选项的文字id（EventTextForTalk）
param3: 未知，几乎都是-1

AddTalkListDataIf(条件 ,param1, param2, param3)
相当于根据条件，是否执行AddTalkListData

GetTalkListEntryResult()
返回值为玩家点击菜单选项后的结果
```

例如：
t000001000_x31()中: AddTalkListData(4, 15000390, -1)

- 15000390为对应的文本id

  ``` xml
  <text id="15000390">记忆</text>
  ```

- 4 为当玩家在篝火菜单选择“记忆”（法术、魔法...），GetTalkListEntryResult()返回值为4，即执行:

``` python
  elif GetTalkListEntryResult() == 4:
      # 记忆魔法
      """State 7"""
      OpenMagicEquip(-1, -1)
      assert not (CheckSpecificPersonMenuIsOpen(11, 0) ==
                  1 and not CheckSpecificPersonGenericDialogIsOpen(0))
```

t000001000_x57便是以z8=11，AddTalkListDataIf(条件, z8, "与梅琳娜交谈", -1) 来判断各种游戏进度然后决定添加哪些“与梅琳娜交谈”选项。

#### 执行菜单选项

我们关注梅琳娜交谈的执行部分，在玩家选择“与梅琳娜交谈”后，到:

``` python
  elif GetTalkListEntryResult() == 11:
      """State 21"""

      assert t000001000_x36(z12=4655)
```

``` python
t000001000_x36
  |- t000001000_x28
    |- t000001000_x35
        |- c1_128(2180, 21800000, 1, 3000, z13, z14, z15, z16)
  |- t000001000_x29
      |- c1_129
```

值得注意的是, GetTalkListEntryResult() == 12: 也使用了t000001000_x36，但具体执行暂不理解。

- event flag 4651  可以用来判断梅琳娜是否已经在赐福处出现。
- t000001000_x36 判断执行t000001000_x28还是t000001000_x29
- t000001000_x28 可用于在赐福召唤梅琳娜出现, **并且进行t000003000.py的对话流程**
  - c1_128中，c2180 为梅琳娜的 character id, z14似乎是动画速度。
- t000001000_x29 用于清除状态并让梅琳娜从赐福处消失

### 问题：如何传递状态

如上所述，c1_128并没有提供什么参数用于控制进行什么对话，而是在t000003000检查各种event flag等等然后进行对话给予物品等。

**问题**：当玩家在赐福菜单选择了一个mod的对话选项，t000003000如何知道选择了什么？

- 方案1:模仿游戏本身的做法，设置某个event flag。
  - 当时即使是搞清楚一些该mod相关的event flag就花费了不少时间，并不清楚游戏本身用到了哪些event flag，没有采用这个做法。
  - 目前已有一些貌似event flag的[解包](https://raw.githubusercontent.com/Nordgaren/Erd-Tools/main/Documentation/Params/Params-Translated/Event%20Param%20Flags%20Translated.csv)，可以通过设置游戏没用到的event flag来简化目前的复杂的方案。

为了尽力避免可能存在的event flag 冲突，利用已知含义的event flag来实现记录玩家选项。

## mod关键原理

### "存储"一个数字到event flag

#### 二进制开关

如果你不了解二进制，最好到网络上寻找一些解释。

event flag 只有两个状态，true和false。
假设 true 为1，false为0，利用两个event flag: A与B

|  A   | B  | 十进制 |
|  ----  |  ----  |  ----  |
| 0  | 0 | 0 |
| 0  | 1 | 1 |
| 1  | 0 | 2 |
| 1  | 1 | 3 |

通过设置 A 与 B 的状态，我们就能某种意义上的存储一个数字（十进制）。

#### mod的具体操作

你可以在t000001000.py中搜索 "AddTalkListData(22" 查看注释中的解释（中文）。

##### mod对话状态

``` xml
    # 11009260 : 到达黄金树根脚,暂时分别对话用的flag(游戏本身用于一次性对话) (<text id="100131000">……谢谢你。</text>)
    # 11009251 : 在王城击败噩兆王后触发重新会合对话
```

当玩家选择一个聊天选项后，会设置:

```python
eventFlag(4680) = false # 0
eventFlag(4681) = true # 1
```

即玩家在进入王城后，不坐任何篝火一次击败噩兆王，虽然不是不可能做到，但一般来说比较少见，就用于判断是否进入mod对话。（我想当时是真的不想再去寻找event flag）。对话结束之后，根据是否拥有洛德符节，还原这两个event flag的值。

##### 存储玩家的选择

使用以下5个event flag来进行存储数字:

``` xml
 4680 : 是否与梅琳娜达成合作(<text id="100011000">……这样就算谈成了。</text>) 
 4681 : 是否已经见过梅琳娜 （关卡前方触发）
 35009360 : 梅琳娜发现玩家受赐癫火 (<text id="100190000">……你受赐癫火了。</text>)
 1054539201 : 通过受赐癫火自行烧树?
 1054539205 : 烧树发生
```

在能够进入mod聊天的时候，这5个event flag的值为能够确定的分别为:

```python
eventFlag(4680) = true # 1
eventFlag(4681) = true # 1
eventFlag(35009360) = false # 0
eventFlag(1054539201) = false # 0
eventFlag(1054539205) = false # 0
```

通过设置这些event flag 来存储数字，理论上能够存储2^5 = 32 条对话选项。**这就是为什么一直强调mod对话时不要突然关游戏**，因为对话进行中的时候，这五个event flag 跟玩家已有的游戏进度是不对应的。

## mod代码讲解

### 赐福菜单（对话入口）(t000001000.py)

- t000001000_x31() 添加召唤/遣返/聊天

```python
    if(not((GetEventFlag(11009260)==1 and GetEventFlag(11009251)==0))  and GetEventFlag(1054539200)==0 and  GetEventFlag(35009360)==0 and GetEventFlag(4681)==1 and GetEventFlag(4680)==1):
        # 70000002 "和梅琳娜聊天" ; 23 为选择后GetTalkListEntryResult
        AddTalkListDataIf(GetEventFlag(4651) == 1, 23, 70000002, -1)

        if(GetEventFlag(4651) == 1):
            # 最终根据eventFlag判断,这里只是为了显示不同文本。
            # 遣返梅琳娜
            AddTalkListData(22, 70000001, -1)
        else:
            # 召唤梅琳娜
            AddTalkListData(22, 70000000, -1)
    else:
        pass
```

- 执行选项
  - 使用TalkListEntryResult 22 与 23

``` python
  # 召唤/遣返梅琳娜
  elif GetTalkListEntryResult() == 22:
      assert t000001000_x2222()
      pass
  # 进入梅琳娜二级菜单对话 (与梅琳娜聊天)
  elif GetTalkListEntryResult() == 23:
      assert t000001000_x2223()
      pass
```

- def t000001000_x2222():
  - 基本是复制t000001000_x36，用于执行具体的梅琳娜出现/离开动画等

- def t000001000_x2223():
  - 构建聊天选项（具体选哪一句）的二级菜单，并且根据玩家的选择，调用t000001000_x2226，存储十进制数字

- def t000001000_x2224():
  - 向二级菜单添加对话选项

- def t000001000_x2225():
  - 原本用于十进制转二进制的部分尝试，mod没有使用

- def t000001000_x2226():
  - 分别设置5个event flag，并且设置11009260与11009251，标志着进入mod对话

- def t000001000_x2227():
  - 发现可以给玩家物品的函数，用于测试，mod中没有使用

- def t000001000_x2228():
  - 检测玩家是否持有仿身泪滴，从+0到+10

### 梅琳娜对话调用 (t000003000.py)

- def t000003000_x2222():
  - 修改的x45函数，加入检测是否进入mod对话状态

```python
    if( GetEventFlag(11009260)==0 and GetEventFlag(11009251)==1):
        assert t000003000_x2227()
        return 0
```


- def t000003000_x2227():
  - 二进制转十进制，计算 GetTalkListEntryResult

- def t000003000_x2224(text2=10012000):
  - 调用t000003000_x32执行对话，调用t000003000_x2225重置event flag

- def t000003000_x2225():
  - 重置event flag，并且根据是否拥有洛德符节还原11009260与11009251

## event flag 与 函数意义

在[note文件夹](../note/)找到中文版，是mod开发时的探索，不能保证一定正确
