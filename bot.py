from py_stealth import *


class Bot:
    def __init__(self, _leader, _friends):
        UseObject(Backpack())
        Wait(500)
        SetEventProc('evbuffdebuffsystem', self.OnBuff)
        SetEventProc('evspeech', self.OnSpeech)
        SetEventProc('evpartyinvite', self.OnInvite)
        self._isBandaging = False
        self._isCasting = False
        self._usingPrimary = False
        self._autoFollow = False
        self._leader = _leader
        self._friends = _friends
        self._id = Self()
        self._bandages = 0

    @property
    def IsBandaging(self):
        return self._isBandaging

    @property
    def IsCasting(self):
        return self._isCasting

    @property
    def AutoFollow(self):
        return self._autoFollow

    @property
    def Bandages(self):
        if FindTypesArrayEx([0x0E21], [0xFFFF], [Backpack()], False):
            self._bandages = GetFindedList()
        return self._bandages[0]

    def SameTile(self, _target):
        if GetX(Self()) == GetX(_target) and GetY(Self()) == GetY(_target):
            return True
        else:
            return False

    def OnBuff(self, _senderID, _attributeID, _bool):
        if _attributeID == '1069':
            self._isBandaging = True
        elif _attributeID == '1101':
            self._isBandaging = False

    def CastTo(self, _spell, _target):
        self._isCasting = True
        CastToObj(_spell, _target)
        self._isCasting = False

    def OnSpeech(self, _text, _senderName, _senderID):
        if _senderID != self._leader and _senderID not in self._friends:
            return
        if _text.endswith('drop'):
            PartyLeave()
        elif _text.endswith('bandages'):
            PartySay(f'I have {GetQuantity(self.Bandages[0])} bandages left.')
        elif _text.endswith('follow'):
            NewMoveXY(GetX(self._leader), GetY(self._leader), True, 0, True)
        elif _text.endswith('follow toggle'):
            self._autoFollow = not self._autoFollow
        elif _text.endswith('eoo'):
            Cast('Enemy Of One')
            Wait(1000)
        elif _text.endswith('use ladder'):
            if IsObjectExists(1073868310):
                NewMoveXY(6432, 1699, True, 0, True)
                UseObject(1073868310)
                Wait(250)
            elif IsObjectExists(1073869466):
                NewMoveXY(6305, 1672, True, 0, True)
                UseObject(1073869466)
                Wait(250)
            else:
                PartySay('Ladder not found')
        elif _text.endswith('use rope'):
            if IsObjectExists(1073868317):
                NewMoveXY(6432, 1633, True, 0, True)
                UseObject(1073868317)
                Wait(250)
            elif IsObjectExists(1073869466):
                NewMoveXY(6305, 1672, True, 0, True)
                UseObject(1073869466)
                Wait(250)
            else:
                PartySay('Rope not found')
        elif _text.endswith('step down'):
            Step(0, False)
        elif _text.endswith('toggle primary'):
            self._usingPrimary = not self._usingPrimary
        elif _text.endswith('help'):
            PartySay(f'drop, bandages, follow, follow toggle, eoo, use ladder, use rope, step down, toggle primary')

    def OnInvite(self, _senderID):
        if _senderID == self._leader or _senderID in self._friends:
            PartyAcceptInvite()
