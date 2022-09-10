# Code explanation

My English is not good, machine translation is used a lot here, if you understand Chinese, you can go to [Chinese version](./code_explanation_zh.md)

Based on the code located in the [draft folder](../draft/script-talk/), please correct me if I misunderstand.

## Basic introduction

- You need to understand binary and decimal, and [ESDLang](https://github.com/thefifthmatt/ESDLang)
- The mod modifies two files:
  - The t000001000.py file is mainly about the menu that is displayed when the player rests at grace.
    - Added summon/make Melina leave, chat with Melina, and a secondary menu of specific chat options(choosing what to chat).
  - The t000003000.py file is mainly about Melina's specific dialogue calls.
    - Added detecting a rare in-game progress ane entry into the mod dialogue flow.

### Grace menu(t000001000.py)

``` python
t000001000_x31 
  |- t000001000_x52 
      |- t000001000_x43 
          |- t000001000_x46 (似乎没有具体作用)
          |- t000001000_x49
              |- t000001000_x57
              |- t000001000_x58
```

In t000001000.py, t000001000_x31 handles adding options to the grace menu (upgrades, great runes, assigning sacred flasks...), where t000001000_x52 handles adding options to talk to Melina, talk to mini ranni, etc. until t000001000_x57 is the more specific code for adding Melina-related talk option.

#### Adding menu options

``` xml
AddTalkListData(param1, param2, param3)
param1: When this option is selected, the result of GetTalkListEntryResult() 
param2: The text id of the dialog option（EventTextForTalk）
param3: Unknown, almost always -1

AddTalkListDataIf(conditions ,param1, param2, param3)
Equivalent to whether to execute AddTalkListData according to the conditions

GetTalkListEntryResult()
The return value is the result after the player clicks the menu option
```

such as:
in t000001000_x31(): AddTalkListData(4, 15000390, -1)

- 15000390is eventTextForTalk id

  ``` xml
  <text id="15000390">Memorize spell</text>
  ```
- "4" is when the player selects "Memorize spell" in the bonfire menu, the return value of GetTalkListEntryResult() will be 4, that is, execute:

``` python
  elif GetTalkListEntryResult() == 4:
      # 记忆魔法
      """State 7"""
      OpenMagicEquip(-1, -1)
      assert not (CheckSpecificPersonMenuIsOpen(11, 0) ==
                  1 and not CheckSpecificPersonGenericDialogIsOpen(0))
```

t000001000_x57 is to use z8=11, AddTalkListDataIf(condition, z8, "Talk to Melina", -1) to judge various game progress and then decide what "Talk to Melina" option to add

#### Execute menu option

We focus on the execution part of Melina's conversation, after the player selects "Talk to Melina", in:

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

noting that GetTalkListEntryResult() == 12:  is also use t000001000_x36, but the specific execution is not understood.

值得注意的是, GetTalkListEntryResult() == 12: 也使用了t000001000_x36，但具体执行暂不理解。

- event flag 4651  It can be used to judge whether Melina has appeared in the grace.
- t000001000_x36 Determine whether to execute t000001000_x28 or t000001000_x29
- t000001000_x28 Can be used to summon Melina in grace, **and run the dialogue flow (code) of t000003000.py**
  - In c1_128, c2180 is Melina's character id, and z14 seems to be the animation speed.
- t000001000_x29 Used to clear the event flag and state and make Melina disappear from the grace

### Problem: How to pass state

As mentioned above, c1_128 does not provide any parameters to control what dialogue to carry out, but to check various event flags at t000003000, etc. and then carry out dialogue or give items to player and so on.

**Problem**：How does t000003000 know what is selected when the player selects a mod's dialogue option in the grace menu?

- Option 1: mocking the flow of the game itself, set an event flag.
  - At that time, it took a lot of time to figure out meaning of event flags this mod using, and it was not clear which event flags were used in the game itself. This method was not adopted.
  - Currently, there are some [unpacking](https://raw.githubusercontent.com/Nordgaren/Erd-Tools/main/Documentation/Params/Params-Translated/Event%20Param%20Flags%20Translated.csv) that look like meaning of event flags , you can simplify the current complexity by setting event flags that are not used by the game plan.

To try to avoid possible event flag conflicts, record player options are implemented using event flags with known meanings.

## Key principles of mod

### "store" a number into the event flag

#### binary switch

If you don't know binary, it's best to look on the net for some explanation.

The event flag has only two states, true and false.
Assuming true is 1 and false is 0, use two event flags: A and B

|  A   | B  | decimal |
|  ----  |  ----  |  ----  |
| 0  | 0 | 0 |
| 0  | 1 | 1 |
| 1  | 0 | 2 |
| 1  | 1 | 3 |

By setting the state of A and B, we can store a number (decimal) in a sense.

#### The specific operation of mod

You can search for "AddTalkListData(22" in t000001000.py to see some explanation in the comments (in Chinese).

##### mod dialog state

``` xml
    # 11009260 : Reach the root of the erd tree, and temporarily separate with melina, (the game itself is used for one-time dialogue)(<text id="100131000">My utmost thanks.</text>)
    # 11009251 : Trigger the reunion dialogue after defeating MORGOTT THE OMEN KING in LEYNDELL ROYAL CAPITAL
```

When a player selects a chat option, we sets:

```python
eventFlag(4680) = false # 0
eventFlag(4681) = true # 1
```

That is to say, after the player enters the leydell royal capital, he does not sit on any bonfire to defeat the morgott once. Although it is not impossible, it is generally rare, So used to judge whether to enter the mod dialogue. (I think I really didn't want to look for more event flag at the time). After the dialogue ends, restore the values of these two event flags according to whether player has rold medallion

##### Store player choices

Use the following 5 event flags to store numbers:

``` xml
4680 : Whether maked accord with Melina (<text id="100011000">Then it's settled.</text>)
4681 : Have met Melina (mostly triggered in grace Gatefront )
35009360 : Melina found out that the player accept Frenzied Flame (<text id="100190000">You...have inherited the frenzied flame.</text>)
1054539201 : Burn the erd tree with frenzied flame?
1054539205 : Tree Burning Occurs
```

When you can enter the mod chatting, the values of these five event flags can be determined as follows:

```python
eventFlag(4680) = true # 1
eventFlag(4681) = true # 1
eventFlag(35009360) = false # 0
eventFlag(1054539201) = false # 0
eventFlag(1054539205) = false # 0
```

By setting these event flags to store numbers, theoretically 2^5 = 32 dialogue options can be stored. **This is why it is always emphasized not to close the game suddenly when the mod is in dialogue**, because when the mod chatting is in progress, these five event flags do not correspond to the player's existing game progress.

## Mod code explanation

### grace menu(t000001000.py)

- t000001000_x31() adding summon/make melina leave/chat with melina

```python
    if(not((GetEventFlag(11009260)==1 and GetEventFlag(11009251)==0))  and GetEventFlag(1054539200)==0 and  GetEventFlag(35009360)==0 and GetEventFlag(4681)==1 and GetEventFlag(4680)==1):
        # 70000002 "chat with melina" ; 23 GetTalkListEntryResult after seleted
        AddTalkListDataIf(GetEventFlag(4651) == 1, 23, 70000002, -1)

        if(GetEventFlag(4651) == 1):
            # display summon or make leave
            # make melina leave
            AddTalkListData(22, 70000001, -1)
        else:
            # summon melina
            AddTalkListData(22, 70000000, -1)
    else:
        pass
```

- Execution options
  - using TalkListEntryResult 22 and 23

``` python
  # summon or make leave
  elif GetTalkListEntryResult() == 22:
      assert t000001000_x2222()
      pass
  # enter secondary chatting menu  (chat with Melina)
  elif GetTalkListEntryResult() == 23:
      assert t000001000_x2223()
      pass
```

- def t000001000_x2222():
  - Basically copied of t000001000_x36, to perform specific Melina appear/leave animations, etc.

- def t000001000_x2223():
  - Build a secondary menu of chat options (specifically which sentence to choose), and according to the player's choice, call t000001000_x2226 to store the decimal number

- def t000001000_x2224():
  - Add dialog options to secondary menu

- def t000001000_x2225():
  - Originally used for some attempts to convert from decimal to binary, the mod is not used

- def t000001000_x2226():
  - Set 5 event flags respectively, and set 11009260 and 11009251, marking entering the mod dialogue

- def t000001000_x2227():
  - Found a function that can give items to the player, for testing, not used in the mod

- def t000001000_x2228():
  - Detects if the player is holding mimic teat spirit ash, from +0 to +10

### 梅琳娜对话调用 (t000003000.py)

- def t000003000_x2222():
  - Modified x45 function, added detecting whether to enter the mod dialogue

```python
    if( GetEventFlag(11009260)==0 and GetEventFlag(11009251)==1):
        assert t000003000_x2227()
        return 0
```


- def t000003000_x2227():
  - Convert binary to decimal, calculate GetTalkListEntryResult

- def t000003000_x2224(text2=10012000):
  - Call t000003000_x32 to execute the dialog, call t000003000_x2225 to reset the event flag

- def t000003000_x2225():
  - Reset the event flag, and restore 11009260 and 11009251 according to whether player have Rold Medallion

## event flag 与 函数意义

you can find the Chinese version in the [note folder](../note/), which is an exploration during mod development, and cannot be guaranteed to be correct

### event flag

```xml
102 new game plus？
108 accepted frenzied flame

4651 is melina shown up at grace (if set to false, will not enter t000003000)
4680 maked accord with melina 
4681 has meet melina
4699 learnd how to upgrade from melina(seperate in royal capital)

11009260 arrived royal capital and seperate with melina
11009251 reuinte with melina after defeatting mogott


35009360 melina found that player accpeted frenzied flame

1054539200 : burn erd tree with melina?
1054539201 : burn erd tree with player it self?
1054539205 : erd tree burned
1054539215 : arrived FORGE OF THE GIANTS？
```
