from py_stealth import *
from bot import Bot


Leader = 73030765
Friends = [999999, 999998]


if __name__ == '__main__':
    SetMoveThroughNPC(0)
    _bot = Bot(Leader, Friends)

    while True:

        if not Connected():
            while not Connected():
                Connect()
                Wait(5000)

        if _bot.AutoFollow:
            if GetX(Self()) != GetX(Leader) and GetY(Self()) != GetY(Leader):
                NewMoveXY(GetX(Leader), GetY(Leader), True, 0, True)

        if GetMana(Self()) > 60:
            UsePrimaryAbility()

        while IsPoisoned(Leader):
            if not _bot.IsBandaging and _bot.SameTile(Leader):
                UseItemOnMobile(_bot.Bandages, Leader)
                Wait(250)
            if GetMana(Self()) > 20:
                _bot.CastTo('Cleanse By Fire', Leader)
                Wait(500)

        if GetHP(Leader) < 100 and not _bot.IsBandaging:
            UseItemOnMobile(_bot.Bandages, Leader)
            Wait(250)

        while GetHP(Leader) < 40:
            if not _bot.IsBandaging and _bot.SameTile(Leader):
                UseItemOnMobile(_bot.Bandages, Leader)
                Wait(250)
            if not _bot.IsCasting and GetMana(Self()) > 20:
                _bot.CastTo('Close Wounds', Leader)
                Wait(500)

        if GetHP(Self()) < 100 and not _bot.IsBandaging:
            UseItemOnMobile(_bot.Bandages, Self())
            Wait(250)

        if FindTypesArrayEx([0x2006], [0xFFFF], [0xFFFF], False):
            _corpseList = GetFindedList()
            if len(_corpseList) < 0:
                for _corpse in _corpseList:
                    if FindTypesArrayEx([0xFFFF], [0xFFFF], _corpse, False):
                        _lootList = GetFindedList()
                        for _loot in _lootList:
                            _lootTooltip = GetTooltip(_loot)
                            if "Legendary" in _lootTooltip or "Splintering" in _lootTooltip:
                                Grab(_loot, 0)
                                Wait(500)
