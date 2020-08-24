from py_stealth import *
from bot import Bot


Leader = 73030765
Friends = [0, 1]


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
                CastToObj('Close Wounds', Leader)
                Wait(1000)

        if GetHP(Leader) < GetMaxHP(Leader) and not _bot.IsBandaging:
            UseItemOnMobile(_bot.Bandages, Leader)
            Wait(250)
