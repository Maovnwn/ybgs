import random
bb = random.uniform(1.12, 1.25)
bb2 = random.uniform(1.35, 1.578)
#bb = random.randint(30,31)
Basic   = {
        "Token"                : "ca1c9e37e67963e9ebdfab968e83c91bb0a4b5ee370af5f1cc558e55ccd91809e480a72072165c32fb290be551a88ef5",
        "Currency"             : "trx",
        "Reset If Profit"      : 0.00000001,
        "Reset If Lose"        : 0,
        "Reset If Win Streak"  : 0,
        "Reset If Lose Streak" : 0,

        "Target Balance"       : 1000,
        "Target Profit"        : 0.1,
        "Target Lose"          : 0,

        "Auto Change Betset"   : "ON",


        ## If Profit/Lose Target Reached
        "Re-Play"              : "OFF",
        "Refresh Seed"         : "ON",

        # 10 digit/char (fill free)
        # fill with `0` if you want random seed

        "Seed"                 : 0
}

Betset  = [{
        "Name"                  : "hiji (1) | 66",
        "Auto Change Betset If" : {
                                 "Win Streak"  : 1,
                                 "Lose Streak" : 0,
                                 "Profit"      : 0,
                                 "Lose"        : 0,
                                 ## "Interval"    : 0,

                                 "Reset Base Bet": "OFF",
        },

        "Base Bet"              : 0.00004,
        "Max Base Bet"          : 0,

        "Chance"                : {
                                 "Min": 1,
                                 "Max": 30
        },
        "HiLo"                  : "H",  # AUTO / H / L

        "Multiply If Win"       : 0,
        "Multiply If Lose"      : bb,
        },
        {
        "Name"                  : "dua (2) | 70",
        "Auto Change Betset If" : {
                                 "Win Streak"  : 0,
                                 "Lose Streak" : 0,
                                 "Profit"      : 0.00000001,
                                 "Lose"        : 0,
                                 ## "Interval"    : 0,

                                 "Reset Base Bet": "ON",
        },

        "Base Bet"              : 0.000054,
        "Max Base Bet"          : 0,

        "Chance"                : {
                                 "Min": 20,
                                 "Max": 30
        },
        "HiLo"                  : "H",  # AUTO / H / L

        "Multiply If Win"       : 0,
        "Multiply If Lose"      : bb2,
        },
        
]

Extra   = {
        ## None for default or `your "User-Agent"`
        "User-Agent"            : None
}
#•••••••••••••••••••••••••••••••••••••••••••••••
#  BL`378_project
#  --
#  https://t.me/Taraje_dah (tg_group)
#  https://t.me/taraje_channel (tg_channel)
#•••••••••••••••••••••••••••••••••••••••••••••••
__CONFIG_VERSION__ = "2.0"

