# -*- coding: utf-8 -*-
def t000003000_1():
    """State 0,1"""
    if not IsClientPlayer():
        """State 3"""
        Label('L0')
        call = t000003000_x46()

        def WhilePaused():
            # eventflag:400001:lot:100010:Rold Medallion
            c5_121(not GetEventFlag(400001) or GetEventFlag(108) == 1, 9600)
        # eventflag:400001:lot:100010:Rold Medallion
            c5_121(GetEventFlag(400001) == 1 and not GetEventFlag(108), 9601)
            GiveSpEffectToPlayerIf(f231(90) < 90, 9600)
            GiveSpEffectToPlayerIf(not f231(90) < 90, 9603)
        assert IsClientPlayer() == 1
    else:
        pass
    """State 4"""
    call = t000003000_x47()
    assert not IsClientPlayer()
    Goto('L0')
    """Unused"""
    """State 2"""
    # actionbutton:6000:"Talk"
    t000003000_x7(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6001, flag5=6000, flag6=4652, flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode2=1, mode3=1)
    Quit()


def t000003000_x0(actionbutton1=6000, flag5=6000, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                  flag4=6001):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer(
        ) and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag5) == 1 or GetEventFlag(flag9) == 1 or GetEventFlag(flag10) == 1 or
                GetEventFlag(flag11) == 1 or GetEventFlag(flag12) == 1)
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 2"""
        if GetEventFlag(flag4) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag5) and not GetEventFlag(flag9) and not GetEventFlag(flag10) and not
              GetEventFlag(flag11) and not GetEventFlag(flag12)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0


def t000003000_x1():
    """State 0,1"""
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0


def t000003000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0


def t000003000_x3(lot1=_):
    """State 0,1"""
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0


def t000003000_x4(action1=23241004):
    """State 0,1"""
    # action:23241004:"A red mark was made on the map"
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0


def t000003000_x5(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t000003000_x21()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t000003000_x1()
    else:
        """State 4,7"""
        call = t000003000_x35()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t000003000_x1()
    """State 9"""
    return 0


def t000003000_x6():
    """State 0,1"""
    assert t000003000_x1()
    """State 2"""
    return 0


def t000003000_x7(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6001, flag5=6000, flag6=4652, flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode2=1, mode3=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t000003000_x24(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z3=z3, z4=z4, z5=z5, z6=z6, mode2=mode2,
                              mode3=mode3)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t000003000_x23()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0


def t000003000_x8(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6001, flag5=6000,
                  flag6=4652, flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000, z6=1000000, mode2=1,
                  mode3=1):
    """State 0"""
    while True:
        """State 2"""
        call = t000003000_x11(actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, z4=z4, z5=z5, z6=z6)

        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (
                DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(
                not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t000003000_x15(val1=val1, z3=z3)

            def WhilePaused():
                c5_138(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (
                    DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
                GiveSpEffectToPlayer(9640)
                c5_139(1 == (mode2 == 1), -1, 0)
                c5_139(1 == (mode3 == 1), 0, -1)

            def ExitPause():
                c1_138(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif IsAttackedBySomeone() == 1 and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        elif GetEventFlag(flag8) == 1:
            Goto('L0')
        elif GetEventFlag(flag6) == 1 and not GetEventFlag(flag7) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t000003000_x17(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t000003000_x28() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            # ???
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t000003000_x13(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0


def t000003000_x9(val2=10, val3=12):
    """State 0,1"""
    call = t000003000_x19(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t000003000_x5(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0


def t000003000_x10(flag1=6000, val2=10, val3=12):
    """State 0,8"""
    assert t000003000_x37()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t000003000_x22()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000003000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0


def t000003000_x11(actionbutton1=6000, flag4=6001, flag5=6000, z4=1000000, z5=1000000, z6=1000000):
    """State 0,1"""
    call = t000003000_x12(z7=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t000003000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0


def t000003000_x12(z7=_, val6=_):
    """State 0,1"""
    if f203(z7) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z7)
        assert f202() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1


def t000003000_x13(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t000003000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t000003000_x14()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000003000_x29()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0


def t000003000_x14():
    """State 0,1"""
    assert t000003000_x12(z7=1101, val6=1101)
    """State 2"""
    return 0


def t000003000_x15(val1=5, z3=1):
    """State 0,2"""
    assert t000003000_x25()
    """State 1"""
    call = t000003000_x16()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t000003000_x27()
    """State 4"""
    return 0


def t000003000_x16():
    """State 0,1"""
    assert t000003000_x12(z7=1000, val6=1000)
    """State 2"""
    return 0


def t000003000_x17(val5=12):
    """State 0,1"""
    call = t000003000_x18()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t000003000_x28()
    """State 3"""
    return 0


def t000003000_x18():
    """State 0,1"""
    assert t000003000_x12(z7=1100, val6=1100)
    """State 2"""
    return 0


def t000003000_x19(val2=10, val3=12):
    """State 0,5"""
    assert t000003000_x37()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t000003000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t000003000_x30()
    """Unused"""
    """State 6"""
    return 0


def t000003000_x20():
    """State 0,2"""
    call = t000003000_x12(z7=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0


def t000003000_x21():
    """State 0,1"""
    assert t000003000_x12(z7=1001, val6=1001)
    """State 2"""
    return 0


def t000003000_x22():
    """State 0,1"""
    assert t000003000_x12(z7=1103, val6=1103)
    """State 2"""
    return 0


def t000003000_x23():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0


def t000003000_x24(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6001, flag5=6000, flag6=4652, flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000,
                   z6=1000000, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t000003000_x8(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z3=z3,
                             z4=z4, z5=z5, z6=z6, mode2=mode2, mode3=mode3)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t000003000_x10(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t000003000_x9(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t000003000_x36() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0


def t000003000_x25():
    """State 0,1"""
    assert t000003000_x26()
    """State 2"""
    return 0


def t000003000_x26():
    """State 0,1"""
    assert t000003000_x12(z7=1104, val6=1104)
    """State 2"""
    return 0


def t000003000_x27():
    """State 0,1"""
    call = t000003000_x12(z7=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t000003000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0


def t000003000_x28():
    """State 0,1"""
    call = t000003000_x12(z7=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t000003000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0


def t000003000_x29():
    """State 0,1"""
    call = t000003000_x12(z7=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t000003000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0


def t000003000_x30():
    """State 0,1"""
    call = t000003000_x12(z7=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t000003000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0


def t000003000_x31(text2=_, z1=_, mode6=1):
    """State 0,5"""
    assert t000003000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text2, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode6:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(z1, 1)
    """State 6"""
    return 0


def t000003000_x32(text4=_, mode5=1):
    # 梅琳娜说话？
    """State 0,4"""
    assert t000003000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text4, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode5:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0


def t000003000_x33(text3=10002100, mode4=1):
    """State 0,4"""
    assert t000003000_x34() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    # talk:10002100:" "
    TalkToPlayer(text3, -1, -1, 1)
    """State 3"""
    if not mode4:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0


def t000003000_x34():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0


def t000003000_x35():
    """State 0,1"""
    assert t000003000_x12(z7=1002, val6=1002)
    """State 2"""
    return 0


def t000003000_x36():
    """State 0,1"""
    assert t000003000_x1()
    """State 2"""
    return 0


def t000003000_x37():
    """State 0,1"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 2"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 3"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 4"""
        ForceCloseMenu()
    else:
        pass
    """State 5"""
    return 0


def t000003000_x38():
    """State 0,1"""
    if not GetEventFlag(10000800):
        """State 2"""
        pass
    else:
        """State 3"""
        pass
    """State 4"""
    return 0


def t000003000_x39():
    # 升级询问
    """State 0,3"""
    # talk:10002000:"Shall I turn your runes to strength?"
    assert t000003000_x32(text4=10002000, mode5=1)
    """State 1"""
    SetWorkValue(2, GetPlayerStat(33))
    """State 4"""
    def ExitPause():
        SetWorkValue(0, 0)
        SetWorkValue(1, 0)
    assert t000003000_x44()
    """State 2"""
    SetWorkValue(2, 0)
    """State 5"""
    return 0


def t000003000_x40():
    """State 0"""
    if GetEventFlag(110) == 1:
        """State 1"""
        pass
    elif not GetEventFlag(4681):
        """State 3"""
        assert t000003000_x73()
    elif not GetEventFlag(4680):
        """State 2"""
        pass
    elif GetEventFlag(108) == 1:
        """State 6"""
        assert t000003000_x75()
    # eventflag:400001:lot:100010:Rold Medallion
    elif GetEventFlag(11009260) == 1 and not GetEventFlag(400001):
        """State 4"""
        assert t000003000_x74()
    else:
        """State 5"""
        assert t000003000_x72()
    """State 7"""
    return 0


def t000003000_x41():
    # 第一次跟梅琳娜对话
    """State 0,8"""
    assert GetCurrentStateElapsedTime() > 2
    """State 10"""
    # talk:10001000:"Have you heard of the Finger Maidens?"
    assert t000003000_x31(text2=10001000, z1=4681, mode6=1)
    """State 4"""
    ClearTalkListData()
    c1_110()
    """State 5"""
    # action:21001000:"Accept"
    AddTalkListData(1, 21001000, -1)
    # action:21001001:"Refuse"
    AddTalkListData(2, 21001001, -1)
    """State 6"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) ==
                1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    if GetTalkListEntryResult() == 1:
        """State 2,11"""
        assert t000003000_x81()
    else:
        """State 7,9"""
        # talk:10001200:"I understand. I'm asking you to put faith in but a stranger."
        assert t000003000_x31(text2=10001200, z1=1042372700, mode6=1)
    """State 3"""
    SetEventFlag(4670, 0)
    SetEventFlag(4698, 0)
    """State 12"""
    return 0


def t000003000_x42():
    # 通过梅琳娜烧树？
    """State 0,1"""
    assert DoesSelfHaveSpEffect(9606) == 1
    """State 2"""
    GiveSpEffectToPlayer(9602)

    def WhilePaused():
        GiveSpEffectToPlayer(9602)

    def ExitPause():
        GiveSpEffectToPlayer(9602)
    assert GetCurrentStateElapsedTime() > 9
    """State 3"""
    SetEventFlag(1054539205, 1)
    SetEventFlag(1054539200, 1)
    GiveSpEffectToPlayer(9601)

    def WhilePaused():
        GiveSpEffectToPlayer(9601)

    def ExitPause():
        GiveSpEffectToPlayer(9601)
    assert GetCurrentStateElapsedTime() > 2
    """State 5"""
    SetEventFlag(9000, 0)
    SetEventFlag(9020, 0)
    """State 4"""
    c1_138(-1)
    Quit()
    """Unused"""
    """State 6"""
    return 0


def t000003000_x43():
    """State 0,1"""
    if GetEventFlag(10009656) == 1:
        """State 16"""
        assert t000003000_x61()
    elif GetEventFlag(1042379200) == 1:
        """State 4"""
        assert t000003000_x50()
    elif GetEventFlag(1042379202) == 1:
        """State 5"""
        # talk:10003000:"This tiny golden aura is the grace of the Erdtree."
        assert t000003000_x51()
    elif GetEventFlag(1042372703) == 1:
        """State 26"""
        # talk:10003200:"Upon the cliff, in Castle Stormveil, is a shardbearer."
        assert t000003000_x54()
    elif GetEventFlag(1042379206) == 1:
        """State 6"""
        assert t000003000_x52()
    elif GetEventFlag(1046389201) == 1:
        """State 7"""
        # 检查是否第一次听
        # talk:10004100:"Very well. In Marika's own words."
        assert t000003000_x56(text2=10004100, z1=1046389202, z2=1046389203)
    elif GetEventFlag(1043349250) == 1:
        """State 8"""
        # talk:10004400:"In Marika's own words."
        assert t000003000_x56(text2=10004400, z1=1043349251, z2=1043349252)
    elif GetEventFlag(1038509250) == 1:
        """State 9"""
        # talk:10004500:"In Marika's own words."
        assert t000003000_x56(text2=10004500, z1=1038509251, z2=1038509252)
    elif GetEventFlag(1043539250) == 1:
        """State 10"""
        # talk:10010100:"In Marika's own words."
        assert t000003000_x56(text2=10010100, z1=1043539251, z2=1043539252)
    elif GetEventFlag(11009255) == 1:
        """State 11"""
        # talk:10010200:"In Marika's own words."
        assert t000003000_x56(text2=10010200, z1=11009256, z2=11009257)
    elif GetEventFlag(1043509200) == 1:
        """State 23"""
        # talk:10010300:"In Marika's own words."
        assert t000003000_x56(text2=10010300, z1=1043509201, z2=1043509202)
    elif GetEventFlag(1054559200) == 1:
        """State 12"""
        # talk:10010400:"In Marika's own words."
        assert t000003000_x56(text2=10010400, z1=1054559201, z2=1054559202)
    elif GetEventFlag(1036489250) == 1:
        """State 13"""
        assert t000003000_x57()
    elif GetEventFlag(1039519250) == 1:
        """State 14"""
        assert t000003000_x58()
    elif GetEventFlag(11009265) == 1:
        """State 27"""
        assert t000003000_x62()
    elif GetEventFlag(1037519200) == 1:
        """State 15"""
        assert t000003000_x59()
    elif GetEventFlag(1054539210) == 1:
        """State 19"""
        assert t000003000_x65()
    elif GetEventFlag(1054539215) == 1:
        """State 20"""
        assert t000003000_x66()
    elif GetEventFlag(35009350) == 1:
        """State 21"""
        assert t000003000_x67()
    elif GetEventFlag(35009352) == 1:
        """State 22"""
        assert t000003000_x68()
    elif GetEventFlag(35009355) == 1:
        """State 24"""
        assert t000003000_x69()
    elif GetEventFlag(35009358) == 1:
        """State 25"""
        assert t000003000_x70()
    elif GetEventFlag(11009270) == 1:
        """State 17"""
        assert t000003000_x63()
    elif GetEventFlag(11009275) == 1:
        """State 18"""
        assert t000003000_x64()
    elif GetEventFlag(4699) == 1:
        """State 3"""
        # talk:999999997:""
        assert t000003000_x31(text2=999999997, z1=11009251, mode6=1)
    else:
        """State 2"""
        pass
    """State 28"""
    return 0


def t000003000_x44():
    """State 0,1"""
    OpenSoul()
    """State 2"""
    # talk:10002100:" "
    assert (t000003000_x33(text3=10002100, mode4=1) and not (CheckSpecificPersonMenuIsOpen(10, 0) ==
            1 and not CheckSpecificPersonGenericDialogIsOpen(0)))
    """State 3"""
    return 0


def t000003000_x2222():
    # custom invoke of x45
    """State 0,7"""

    assert not GetEventFlag(9001)
    """State 10"""
    assert not DoesSelfHaveSpEffect(9606) or GetCurrentStateElapsedTime() > 10
    """State 5"""

    # 11009260 : 到达黄金树根脚,暂时分别(但之后不会设置回来) (<text id="100131000">……谢谢你。</text>)
    # 11009251 : 在王城击败噩兆王后重新会合对话

    # 被设置为不可能的状态,表示进入mod对话,之后根据有无洛德符节还原
    if( GetEventFlag(11009260)==0 and GetEventFlag(11009251)==1):
        assert t000003000_x2227()
        return 0
    elif GetEventFlag(4653) == 1:
        """State 1,12"""
        def WhilePaused():
            RequestAnimation(20004, -1)
        assert t000003000_x40()
    elif GetEventFlag(4654) == 1:
        """State 2,13"""
        assert t000003000_x38()
    elif GetEventFlag(4655) == 1:
        """State 3,15"""
        def WhilePaused():
            RequestAnimation(20004, -1)
        assert t000003000_x43()
    elif GetEventFlag(4657) == 1:
        """State 9,16"""
        def WhilePaused():
            RequestAnimation(20004, -1)
        assert t000003000_x53()
    elif GetEventFlag(4656) == 1:
        """State 4,11"""
        SetWorkValue(1, 0)

        def WhilePaused():
            GiveSpEffectToPlayer(9605)
            SetWorkValueIf(not GetWorkValue(
                1) > 1 and DoesPlayerHaveSpEffect(9604) == 1, 1, 1)
            RequestAnimationIf(GetWorkValue(1) > 1, 20002, -1)
            GiveSpEffectToPlayerIf(GetWorkValue(0) > 1, 9601)
            SetWorkValueIf(not GetWorkValue(
                0) > 1 and DoesSelfHaveSpEffect(9605) == 1, 0, 1)
            c5_121(GetWorkValue(1) > 1, 9602)
            SetWorkValueIf(GetWorkValue(
                0) > 1 and not DoesSelfHaveSpEffect(9605), 0, 0)

        def ExitPause():
            SetWorkValue(1, 0)
            SetWorkValue(0, 0)
        assert t000003000_x39()
    elif GetEventFlag(1054539200) == 1:
        """State 8,14"""
        t000003000_x42()

        def WhilePaused():
            RequestAnimation(20007, -1)
        Quit()
    else:
        """State 6"""
        pass
    """State 17"""
    # assert t000003000_x2225()
    return 0


def t000003000_x2224(text2=10012000):
    # 中间件t000003000_x31
    assert t000003000_x2225()
    assert t000003000_x32(text4=text2, mode5=1)
    return 0

    # if 1:
    #     assert t000003000_x2225()
    # elif 1:
    #     assert t000003000_x31(text2=text2, z1=4651, mode6=1)
    # else:
    #     return 0
    # call.get() 获取返回值
    # return 0


def t000003000_x2227():
    # 自定义对话响应
    if 1:
        def WhilePaused():
            RequestAnimation(20004, -1)

        # t000003000_x31 z1 为even flag,会被设置为1
        # 根据 5 个eventFlag , 二进制转十进制，决定对话选项

        # if GetEventFlag(1054539200):
        #     # binary(1 _ _ _ _ 0)
        #     if GetEventFlag(35009360):
        #         if GetEventFlag(4681):
        #             if GetEventFlag(4680):
        #                 if GetEventFlag(4651):
        #                     # binary(11111) -> dec(31)
        #                 else:
        #                     # binary(11110) -> dec(30)
        #             else:
        #                 # binary(1111_)
        #         else:
        #     else:
        #             # assert t000003000_x31(text2=10012000)
        # else:
        #     # assert t000003000_x31(text2=10014000)

        # 二进制转十进制，以下全部一样，关注 == 右值 即可
        if((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 0):
            # TODO test
            # <text id="106113000">……哦？</text>
            assert t000003000_x31(text2=10611300, z1=4651, mode6=1)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 1):
            #<text id="100031000">……关于我吗？</text>
            assert t000003000_x2224(text2=10003100)
            # return 0

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 12):
            # <text id="100101000">……我直接复诵玛莉卡的箴言：</text>
            # <text id="100101010">“半神啊，我可爱的孩子啊。”</text>
            assert t000003000_x2224(text2=10010100)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 3):
            # <text id="100102000">……我直接复诵玛莉卡的箴言：</text>
            #<text id="100102010">“噢，拉达冈啊，黄金律法的忠犬啊。”</text>
            assert t000003000_x2224(text2=10010200)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 4):
            # 100103000	……我直接复诵玛莉卡的箴言：
            # <text id="100103010">“我在此宣告，去探索黄金律法──”</text>
            assert t000003000_x2224(text2=10010300)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 5):
            # 100104000	……我直接复诵玛莉卡的箴言：
            #<text id="100104010">“王的众战士啊，吾王葛孚雷啊。”</text>
            assert t000003000_x2224(text2=10010400)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 6):
            # <text id="100041000">……我知道了。我直接复诵玛莉卡的箴言：</text>
            # <text id="100041010">“吾王啊，王的众战士啊，我将夺去你们的赐福。”</text>
            assert t000003000_x2224(text2=10004100)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 7):
            # <text id="100044000">……我直接复诵玛莉卡的箴言：</text>
            # <text id="100044010">“在你们面临死亡之后，那被夺去的会再归还──”</text>
            # 00111
            assert t000003000_x2224(text2=10004400)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 8):
            # 100045000	……我直接复诵玛莉卡的箴言：
            # <text id="100045010">“黄金树是掌管一切的存在。做出抉择吧──”</text>
            assert t000003000_x2224(text2=10004500)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 9):
            # 100120000	…… (仿身泪滴白金废案,约定)
            assert t000003000_x2224(text2=10012000)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 10):
            # 100121000	…… (仿身泪滴废案,旅行)
            assert t000003000_x2224(text2=10012100)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 11):
            # 100150000	……你不用担心火种。(刚开始)
            assert t000003000_x2224(text2=10015000)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 2):
            # 100030000	……这簇小巧的金光，是黄金树的赐福。
            assert t000003000_x2224(text2=10003000)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 13):
            # 100160000	……我想告诉你一件事。
            assert t000003000_x2224(text2=10016000)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 14):
            # 100180000	……如果你的心向着癫火，
            assert t000003000_x2224(text2=10018000)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 15):
            # 100181000	……我会准备火种。(癫火)
            assert t000003000_x2224(text2=10018100)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 16):
            # 100185000	……我再说一次──
            # <text id="100185010">请让你的心，远离癫火吧。</text>
            assert t000003000_x2224(text2=10018500)

        elif((GetEventFlag(1054539205)*16 + GetEventFlag(1054539201)*8 + GetEventFlag(35009360)*4 + GetEventFlag(4681)*2 + GetEventFlag(4680)*1) == 17):
            # <text id="100186000">拜托你了，能不能悬崖勒马？</text>
            assert t000003000_x2224(text2=10018600)
        else:
            # TODO default 测试
            # 106030000	<text id="106030000">……稍微聊聊过去的事吧。</text>
            assert t000003000_x31(text2=10603000, z1=4651, mode6=1)
    else:
        # # """never"""
        # # TODO default 测试 (没有作用？))
        # # <text id="106192010">……唉，没想到你这么缠人。</text>
        assert t000003000_x2225()
        # assert t000003000_x31(text2=10619000, z1=4651, mode6=1)
        pass
    return 0


def t000003000_x2225():
    # 重置flag
    


    SetEventFlag(4680, 1)
    SetEventFlag(4681, 1)
    SetEventFlag(35009360, 0)
    SetEventFlag(1054539201, 0)
    SetEventFlag(1054539205, 0)

    # 11009260 : 到达黄金树根脚,暂时分别(但之后不会设置回来) (<text id="100131000">……谢谢你。</text>)
    # 11009251 : 在王城击败噩兆王后重新会合对话

    # 设置为不可能的状态,表示进入mod对话,之后根据有无洛德符节还原
    # eventflag:400001:lot:100010:Rold Medallion

    # 没到王城分离
    SetEventFlag(11009260, 0)
    SetEventFlag(11009251, 0)  
    if(GetEventFlag(400001)):
        #拿到洛德符节,已经会合
        SetEventFlag(11009260, 1)
        SetEventFlag(11009251, 1)      
    else:
        # else 到底怎么调用？
        pass
    return 0

def t000003000_x45():
    """State 0,7"""
    assert not GetEventFlag(9001)
    """State 10"""
    assert not DoesSelfHaveSpEffect(9606) or GetCurrentStateElapsedTime() > 10
    """State 5"""
    if GetEventFlag(4653) == 1:
        """State 1,12"""
        def WhilePaused():
            RequestAnimation(20004, -1)
        assert t000003000_x40()
    elif GetEventFlag(4654) == 1:
        """State 2,13"""
        assert t000003000_x38()
    elif GetEventFlag(4655) == 1:
        """State 3,15"""
        def WhilePaused():
            RequestAnimation(20004, -1)
        assert t000003000_x43()
    elif GetEventFlag(4657) == 1:
        """State 9,16"""
        def WhilePaused():
            RequestAnimation(20004, -1)
        assert t000003000_x53()
    elif GetEventFlag(4656) == 1:
        """State 4,11"""
        SetWorkValue(1, 0)

        def WhilePaused():
            GiveSpEffectToPlayer(9605)
            SetWorkValueIf(not GetWorkValue(
                1) > 1 and DoesPlayerHaveSpEffect(9604) == 1, 1, 1)
            RequestAnimationIf(GetWorkValue(1) > 1, 20002, -1)
            GiveSpEffectToPlayerIf(GetWorkValue(0) > 1, 9601)
            SetWorkValueIf(not GetWorkValue(
                0) > 1 and DoesSelfHaveSpEffect(9605) == 1, 0, 1)
            c5_121(GetWorkValue(1) > 1, 9602)
            SetWorkValueIf(GetWorkValue(
                0) > 1 and not DoesSelfHaveSpEffect(9605), 0, 0)

        def ExitPause():
            SetWorkValue(1, 0)
            SetWorkValue(0, 0)
        assert t000003000_x39()
    elif GetEventFlag(1054539200) == 1:
        """State 8,14"""
        t000003000_x42()

        def WhilePaused():
            RequestAnimation(20007, -1)
        Quit()
    else:
        """State 6"""
        pass
    """State 17"""
    return 0


def t000003000_x46():
    """State 0"""
    while True:
        """State 1"""
        assert GetEventFlag(4652) == 1
        """State 2"""
        # ========== custom ===========
        call = t000003000_x2222()
        # =============================
        # call = t000003000_x45()

        def ExitPause():
            SetEventFlag(4652, 0)
            SetEventFlag(4653, 0)
            SetEventFlag(4654, 0)
            SetEventFlag(4655, 0)
            SetEventFlag(4656, 0)
            SetEventFlag(4657, 0)
        if call.Done():
            pass
        elif not GetEventFlag(4652):
            pass
        """State 3"""
        assert t000003000_x1()
    """Unused"""
    """State 4"""
    return 0


def t000003000_x47():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0


def t000003000_x48():
    """State 0"""
    if GetEventFlag(10000851) == 1:
        """State 7,10"""
        # talk:10010500:"Forgive me. I've been...testing you."
        assert t000003000_x32(text4=10010500, mode5=1)
    else:
        """State 8,11"""
        # talk:10010700:"Forgive me. I've been...testing you."
        assert t000003000_x32(text4=10010700, mode5=1)
    """State 9"""
    SetEventFlag(10009655, 1)
    """State 3"""
    ClearTalkListData()
    c1_110()
    """State 4"""
    # action:21001004:"Go to the Roundtable Hold"
    AddTalkListData(1, 21001004, -1)
    """State 5"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) ==
                1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    if GetTalkListEntryResult() == 1:
        """State 2,12"""
        assert t000003000_x78()
    else:
        """State 6"""
        pass
    """State 13"""
    return 0


def t000003000_x49():
    """State 0,6"""
    # talk:10014000:"Hello again, old friend."
    assert t000003000_x31(text2=10014000, z1=11009251, mode6=1)
    """State 1"""
    SetEventFlag(11002745, 1)
    """State 2"""
    SetEventFlag(11109687, 1)
    """State 5"""
    SetEventFlag(11009252, 1)
    """State 7"""
    # lot:100010:Rold Medallion
    call = t000003000_x3(lot1=100010)
    if call.Done() and not GetEventFlag(62528):
        """State 3,8"""
        # action:23241004:"A red mark was made on the map"
        assert t000003000_x4(action1=23241004)
    elif call.Done():
        """State 4"""
        pass
    """State 9"""
    return 0


def t000003000_x50():
    # 第一次拒绝了梅琳娜
    """State 0"""
    if not GetEventFlag(4681):
        """State 7,11"""
        # talk:10001000:"Have you heard of the Finger Maidens?"
        assert t000003000_x31(text2=10001000, z1=1042379201, mode6=1)
    else:
        """State 8,10"""
        # talk:10001300:"Have you reconsidered my offer?"
        assert t000003000_x31(text2=10001300, z1=1042379201, mode6=1)
    """State 3"""
    ClearTalkListData()
    c1_110()
    """State 4"""
    # action:21001000:"Accept"
    AddTalkListData(1, 21001000, -1)
    # action:21001001:"Refuse"
    AddTalkListData(2, 21001001, -1)
    """State 5"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) ==
                1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    if GetTalkListEntryResult() == 1:
        """State 2,12"""
        assert t000003000_x81()
    else:
        """State 6,9"""
        # talk:10001200:"I understand. I'm asking you to put faith in but a stranger."
        assert t000003000_x31(text2=10001200, z1=1042372700, mode6=1)
    """State 13"""
    return 0


def t000003000_x51():
    """State 0,2"""
    # talk:10003000:"This tiny golden aura is the grace of the Erdtree."
    assert t000003000_x31(text2=10003000, z1=1042379203, mode6=1)
    """State 1"""
    # 用于控制对话顺序？
    SetEventFlag(1042372703, 1)
    """State 3"""
    return 0


def t000003000_x52():
    """State 0,1"""
    # talk:10003100:"Me?"
    assert t000003000_x31(text2=10003100, z1=1042379207, mode6=1)
    """State 2"""
    return 0


def t000003000_x53():
    """State 0,1,2,3"""
    return 0


def t000003000_x54():
    """State 0,1"""
    # talk:10003200:"Upon the cliff, in Castle Stormveil, is a shardbearer."
    assert t000003000_x31(text2=10003200, z1=1042379209, mode6=1)
    """State 2"""
    return 0


def t000003000_x55():
    """State 0"""
    if not GetEventFlag(1046389200):
        """State 5,8"""
        # talk:10004000:"Spoken echoes linger here."
        assert t000003000_x32(text4=10004000, mode5=1)
    else:
        """State 6,7"""
        # talk:10004300:"Spoken echoes of Queen Marika linger here, as well."
        assert t000003000_x32(text4=10004300, mode5=1)
    """State 2"""
    ClearTalkListData()
    c1_110()
    """State 3"""
    # action:21001002:"I'm interested"
    AddTalkListData(1, 21001002, -1)
    # action:21001003:"I'm not interested"
    AddTalkListData(2, 21001003, -1)
    """State 4"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) ==
                1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    if GetTalkListEntryResult() == 1:
        """State 9"""
        return 0
    else:
        """State 10"""
        return 1


def t000003000_x56(text2=_, z1=_, z2=_):
    """State 0,3"""
    SetEventFlag(z2, 1)
    if not GetEventFlag(1046382700):
        """State 4"""
        call = t000003000_x55()
        if call.Get() == 0:
            """State 5"""
            Label('L0')
            assert t000003000_x31(text2=text2, z1=z1, mode6=1)
            """State 2"""
            SetEventFlag(1046389200, 1)
            """State 7"""
            assert t000003000_x76()
        elif call.Done():
            """State 6"""
            # <text id="100042000">……我知道了，这不必勉强自己听。</text>
            # talk:10004200:"Of course. Perhaps there is no need."
            assert t000003000_x31(text2=10004200, z1=1046382700, mode6=1)
    else:
        """State 1"""
        Goto('L0')
    """State 8"""
    return 0


def t000003000_x57():
    """State 0,1"""
    # talk:10011000:"Your seamster, Boc..."
    assert t000003000_x31(text2=10011000, z1=1036489251, mode6=1)
    """State 2"""
    return 0


def t000003000_x58():
    """State 0,1"""
    # talk:10011100:"Your seamster, Boc..."
    assert t000003000_x31(text2=10011100, z1=1039519251, mode6=1)
    """State 2"""
    return 0


def t000003000_x59():
    """State 0,1"""
    # talk:10013000:"The Erdtree...is close."
    assert t000003000_x31(text2=10013000, z1=1037519201, mode6=1)
    """State 2"""
    return 0


def t000003000_x60():
    """State 0,1"""
    # talk:10013100:"My utmost thanks."
    assert t000003000_x31(text2=10013100, z1=11009260, mode6=1)
    """State 2"""
    return 0


def t000003000_x61():
    """State 0,1"""
    assert t000003000_x78()
    """State 2"""
    return 0


def t000003000_x62():
    """State 0,1"""
    # talk:10014100:"I wish to journey with you once more."
    assert t000003000_x31(text2=10014100, z1=11009266, mode6=1)
    """State 2"""
    return 0


def t000003000_x63():
    """State 0,1"""
    # talk:10015000:"Think not, of the kindling."
    assert t000003000_x31(text2=10015000, z1=11009271, mode6=1)
    """State 2"""
    return 0


def t000003000_x64():
    """State 0,1"""
    # talk:10016000:"There is something I'd like to say."
    assert t000003000_x31(text2=10016000, z1=11009276, mode6=1)
    """State 2"""
    return 0


def t000003000_x65():
    """State 0,1"""
    # talk:10017000:"We're almost there."
    assert t000003000_x31(text2=10017000, z1=1054539211, mode6=1)
    """State 2"""
    return 0


def t000003000_x66():
    """State 0"""
    if not GetEventFlag(1054539216):
        """State 7"""
        # talk:10017100:"I have long observed the Lands Between."
        assert t000003000_x31(text2=10017100, z1=1054539216, mode6=1)
    else:
        """State 8"""
        # talk:10017400:"Are you ready to commit a cardinal sin?"
        assert t000003000_x31(text2=10017400, z1=1054539216, mode6=1)
    """State 3"""
    ClearTalkListData()
    c1_110()
    """State 4"""
    # action:21001005:"I'm ready"
    AddTalkListData(1, 21001005, -1)
    # action:21001006:"I'd like you to wait"
    AddTalkListData(2, 21001006, -1)
    """State 5"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) ==
                1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    if GetTalkListEntryResult() == 1:
        """State 2,9"""
        # talk:10017200:"Very well."
        assert t000003000_x32(text4=10017200, mode5=1)
        """State 11"""
        t000003000_x42()

        def WhilePaused():
            RequestAnimation(20007, -1)
        Quit()
    else:
        """State 6,10"""
        # talk:10017300:"Very well."
        assert t000003000_x32(text4=10017300, mode5=1)
        """State 12"""
        return 0


def t000003000_x67():
    """State 0,2"""
    # talk:10018000:"If you intend to claim the frenzied flame,"
    assert t000003000_x31(text2=10018000, z1=35009351, mode6=1)
    """State 1"""
    SetEventFlag(35002732, 1)
    """State 3"""
    return 0


def t000003000_x68():
    """State 0,2"""
    # talk:10018500:"I ask you, one more time."
    assert t000003000_x31(text2=10018500, z1=35009353, mode6=1)
    """State 1"""
    SetEventFlag(35002733, 1)
    """State 3"""
    return 0


def t000003000_x69():
    """State 0"""
    if GetEventFlag(35009356) == 1:
        """State 1,7"""
        # talk:10018100:"I shall see to the kindling."
        assert t000003000_x32(text4=10018100, mode5=1)
    elif GetEventFlag(35009357) == 1:
        """State 2,8"""
        # talk:10018200:"The frenzied flame is not to be meddled with."
        assert t000003000_x32(text4=10018200, mode5=1)
    elif GetEventFlag(1049539207) == 1:
        """State 3,5"""
        # talk:10018100:"I shall see to the kindling."
        assert t000003000_x31(text2=10018100, z1=35009356, mode6=1)
    else:
        """State 4,6"""
        # talk:10018200:"The frenzied flame is not to be meddled with."
        assert t000003000_x31(text2=10018200, z1=35009357, mode6=1)
    """State 9"""
    return 0


def t000003000_x70():
    """State 0,1"""
    # talk:10018600:"Please, put a stop to this madness."
    assert t000003000_x31(text2=10018600, z1=35009359, mode6=1)
    """State 2"""
    return 0


def t000003000_x71():
    """State 0"""
    # eventflag:400001:lot:100010:Rold Medallion
    if not GetEventFlag(400001):
        """State 2,4"""
        # talk:10019000:"You...have inherited the frenzied flame."
        assert t000003000_x32(text4=10019000, mode5=1)
    else:
        """State 3,5"""
        # talk:10019100:"You...have inherited the frenzied flame."
        assert t000003000_x32(text4=10019100, mode5=1)
    """State 1"""
    SetEventFlag(35009360, 1)
    """State 6"""
    return 0


def t000003000_x72():
    """State 0"""
    if (GetEventFlag(10000851) == 1 and not GetEventFlag(10009655) and not DoesPlayerHaveSpEffect(4270)
        and not DoesPlayerHaveSpEffect(4271) and not DoesPlayerHaveSpEffect(4272) and not DoesPlayerHaveSpEffect(4280)
            and not DoesPlayerHaveSpEffect(4282) and not DoesPlayerHaveSpEffect(4286)):
        """State 2"""
        def WhilePaused():
            RequestAnimation(20004, -1)
        assert t000003000_x48()
    elif ((GetEventFlag(3062) == 1 or GetEventFlag(3063) == 1 or GetEventFlag(3064) == 1 or GetEventFlag(3065)
          == 1) and not GetEventFlag(10009655) and not DoesPlayerHaveSpEffect(4270) and not DoesPlayerHaveSpEffect(4271)
          and not DoesPlayerHaveSpEffect(4272) and not DoesPlayerHaveSpEffect(4280) and not DoesPlayerHaveSpEffect(4282)
          and not DoesPlayerHaveSpEffect(4286)):
        """State 4"""
        def WhilePaused():
            RequestAnimation(20004, -1)
        assert t000003000_x48()
    # eventflag:400001:lot:100010:Rold Medallion
    elif (not GetEventFlag(11009260) and not GetEventFlag(400001) and (GetEventFlag(11002741) == 1 or
          GetEventFlag(11002742) == 1 or GetEventFlag(11002743) == 1 or GetEventFlag(11002744) == 1)):
        """State 5"""
        def WhilePaused():
            RequestAnimation(20004, -1)
        assert t000003000_x60()
    # eventflag:400001:lot:100010:Rold Medallion
    elif GetEventFlag(9104) == 1 and not GetEventFlag(400001):
        """State 3"""
        def WhilePaused():
            RequestAnimation(20004, -1)
        assert t000003000_x49()
    else:
        """State 1"""
        pass
    """State 6"""
    return 0


def t000003000_x73():
    """State 0,1"""
    assert t000003000_x41()
    """State 2"""
    return 0


def t000003000_x74():
    """State 0"""
    # eventflag:400001:lot:100010:Rold Medallion
    if GetEventFlag(9104) == 1 and not GetEventFlag(400001):
        """State 2"""
        def WhilePaused():
            RequestAnimation(20004, -1)
        assert t000003000_x49()
    else:
        """State 1"""
        pass
    """State 3"""
    return 0


def t000003000_x75():
    """State 0,1"""
    assert t000003000_x71()
    """State 2"""
    return 0


def t000003000_x76():
    # 获得外在律法
    """State 0"""
    if GetEventFlag(1043509200) == 1:
        """State 1"""
        if not GetEventFlag(60846):
            """State 3"""
            # gesture:104:Outer Order
            AcquireGesture(104)
            SetEventFlag(60846, 1)
            assert GetCurrentStateElapsedTime() > 1 and not IsMenuOpen(63)
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 5"""
    return 0


def t000003000_x77():
    """State 0,2"""
    # talk:10010600:"Very well."
    assert (t000003000_x79(text1=10010600, mode1=1) and (DoesPlayerHaveSpEffect(9601) == 1 or CheckSpecificPersonTalkHasEnded(0)
            == 1))
    """State 1"""
    RequestAnimationIf(GetWorkValue(1) > 1, 20002, -1)

    def WhilePaused():
        RequestAnimationIf(GetWorkValue(1) > 1, 20002, -1)

    def ExitPause():
        RequestAnimationIf(GetWorkValue(1) > 1, 20002, -1)
    assert t000003000_x80()
    """State 3"""
    return 0


def t000003000_x78():
    """State 0,1"""
    SetWorkValue(0, 0)
    SetWorkValue(1, 0)

    def WhilePaused():
        SetWorkValueIf(not GetWorkValue(
            1) > 1 and DoesPlayerHaveSpEffect(9604) == 1, 1, 1)
        SetWorkValueIf(not GetWorkValue(
            0) > 1 and DoesSelfHaveSpEffect(9605) == 1, 0, 1)
        GiveSpEffectToPlayer(9605)
        GiveSpEffectToPlayerIf(GetWorkValue(0) > 1, 9601)
        c5_121(GetWorkValue(1) > 1, 9602)

    def ExitPause():
        SetWorkValue(0, 0)
        SetWorkValue(1, 0)
    assert t000003000_x77()
    """State 2"""
    return 0


def t000003000_x79(text1=10010600, mode1=1):
    """State 0,4"""
    assert t000003000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    # talk:10010600:"Very well."
    TalkToPlayer(text1, -1, -1, 0)
    """State 3"""
    if not mode1:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0


def t000003000_x80():
    """State 0,3"""
    RequestAnimationIf(GetWorkValue(1) > 1, 20002, -1)

    def WhilePaused():
        RequestAnimationIf(GetWorkValue(1) > 1, 20002, -1)

    def ExitPause():
        RequestAnimationIf(GetWorkValue(1) > 1, 20002, -1)
    assert DoesPlayerHaveSpEffect(9601) == 1
    """State 4"""
    assert GetCurrentStateElapsedTime() > 11 and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2,1"""
    SetEventFlag(11109786, 1)
    SetEventFlag(104, 1)
    """State 5"""
    return 0


def t000003000_x81():
    """State 0"""
    # 物品 130 灵马口哨
    # goods:130:Spectral Steed Whistle
    if ComparePlayerInventoryNumber(3, 130, 0, 0, 0) == 1:
        """State 1,3"""
        # talk:10001100:"Then it's settled."
        assert t000003000_x31(text2=10001100, z1=4680, mode6=1)
        """State 4"""
        # lot:100000:Spectral Steed Whistle
        assert t000003000_x3(lot1=100000)
        """State 5"""
        # talk:10001105:"Use it to traverse great distances."
        assert t000003000_x32(text4=10001105, mode5=1)
    else:
        """State 2,7"""
        # 该对话不存在？
        # talk:10001110:"Then it's settled."
        assert t000003000_x31(text2=10001110, z1=4680, mode6=1)
        """State 6"""
        # lot:100000:Spectral Steed Whistle
        assert t000003000_x3(lot1=100000)
    """State 8"""
    return 0
