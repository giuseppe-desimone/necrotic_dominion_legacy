"""v0.12"""

import player as pg
from lv_1 import callbacks_l1 as c


def s03_actions():
    """Restituisce le azioni possibili nella stanza 0,3."""
    if 'spada' in pg.PG.inventory:
        actions = [
          {"text": "Tornare a est", "callback": c.go_04}
        ]
    else:
        actions = [
            {"text": "Tornare a est", "callback": c.go_04}
        ]
        if "chiave" in pg.PG.inventory:
            actions.append({"text": "Aprire la cassapanca", "callback": c.open_chest_with_key})
    return actions


def s04_actions():
    """Restituisce le azioni possibili nella stanza iniziale."""
    if 'chiave' in pg.PG.inventory or 'spada' in pg.PG.inventory:
        actions = [
            {"text": "Andare a est", "callback": c.go_05},
            {"text": "Andare a ovest", "callback": c.go_03},
            {"text": "Vai a sud in quello che sembra un corridoio buio", "callback": c.go_14}
        ]
    else:
        actions = [
            {"text": "Andare a est", "callback": c.go_05},
            {"text": "Andare ad ovest", "callback": c.go_03},
            {"text": "Vai a sud in quello che sembra un corridoio buio", "callback": c.go_14},
            {"text": "Raccogliere la chiave", "callback": c.pick_up_key}
        ]
    return actions

# def s04_actions():
#     actions = []
#     actions.push({"text": "Andare a est", "callback": c.go_05})
#     actions.push({"text": "Andare ad ovest", "callback": c.go_03})
#     actions.push({"text": "Vai a sud in quello che sembra un corridoio buio", "callback": c.go_14})
#     if not pg.PG.inventory.get("chiave") : actions.push({"text": "Raccogliere la chiave", "callback": c.pick_up_key}) 
#     if not pg.PG.inventory.get("spada") : actions.push({"text": "Raccogliere la chiave", "callback": c.pick_up_key}) 

#     return actions

def s05_actions():
    """Restituisce le azioni possibili nella stanza 0,5."""
    if c.v05 is True:
        actions = [
            {"text": "Vai ad ovest", "callback": c.go_04},
            {"text": "Entra nella porta ad est", "callback": c.go_06}
        ]
    else:
        actions = [
            {"text": "Vai ad ovest nell'atrio", "callback": c.go_04},
            {"text": "Aprire la porta", "callback": c.open_door_05}
        ]
    return actions


def s06_actions():
    if pg.l1_imp.PV > 0:
            actions = [
                    {"text": "Attacca l'imp", "callback": c.combat_06},
                    # {"text": "Vai ad ovest verso la stanza vuota", "callback": c.go_05}
                ]
    else:
        actions = []
        actions.append({"text": "Vai ad ovest verso la stanza vuota", "callback": c.go_05})
        
        if c.v06a is False:
                actions.append({"text": "Cerca tra i resti dell'imp", "callback": c.pick_up_key3})
        if c.v06 is False:
                actions.append({"text": "Abbeverati alla fontana", "callback": c.drink_06})

    return actions


def s14_actions():
    """Restituisce le azioni possibili nella stanza 1,4."""
    actions = [
        {"text": "Continua a percorrere il corridoio verso sud", "callback": c.go_24},
        {"text": "Vai verso l'atrio", "callback": c.go_04}
    ]
    return actions


def s24_actions():
    """Restituisce le azioni possibili nella stanza 2,4."""
    if c.v06a is True:
        if c.v24 is False:
            actions = [
                {"text": "Percorri il corridoio verso nord", "callback": c.go_14},
                {"text": "Aprire la porta a sud", "callback": c.open_door_24},
                {"text": "Aprire la porta a est", "callback": c.go_25}
            ]
        else:
            actions = [
                {"text": "Percorri il corridoio verso nord", "callback": c.go_14},
                {"text": "Entra nella porta a sud", "callback": c.go_34},
                {"text": "Aprire la porta a est", "callback": c.go_25}
            ]
    else:
        actions = [
            {"text": "Percorri il corridoio verso nord", "callback": c.go_14},
            {"text": "Aprire la porta a sud", "callback": c.open_door_nokey_24},
            {"text": "Aprire la porta a est", "callback": c.go_25}
        ]
    return actions


def s25_actions():
    """Restituisce le azioni possibili nella stanza 2,5."""
    if c.v25 is True:
        if pg.l1_oldguard.PV > 0:
            actions = [
                {"text": "Torna indietro nel corridoio", "callback": c.go_24},
                {"text": "Uccidi la guardia nel sonno", "callback": c.dialog_25_kill},
            ]
        else:
            actions = [
                {"text": "Torna indietro nel corridoio", "callback": c.go_24},
            ]
    else:
        if pg.l1_oldguard.PV > 0:
            actions = [
                {"text": "Torna indietro nel corridoio", "callback": c.go_24},
                {"text": "Parla con la guardia", "callback": c.dialog_25_start},
                {"text": "Attacca la guardia", "callback": c.dialog_25_combat}
            ]
        else:
            actions = [
                {"text": "Torna indietro nel corridoio", "callback": c.go_24},
                {"text": "Cerca nel cadavere", "callback": c.pick_up_key2},
            ]
    return actions


def s34_actions():
    """Restituisce le azioni possibili nella stanza 1,4."""
    if pg.l1_undead.PV > 0:
        actions = [
            {"text": "Attacca lo zombie", "callback": c.combat_36},
            # {"text": "Vai ad ovest verso la stanza vuota", "callback": c.go_05}
        ]
    else:
        actions = []
        actions.append({"text": "Vai ad ovest verso la stanza vuota", "callback": c.go_05})

        if c.v06a is False:
            actions.append({"text": "Cerca tra i resti dell'imp", "callback": c.pick_up_key3})
        if c.v06 is False:
            actions.append({"text": "Abbeverati alla fontana", "callback": c.drink_06})

    return actions



    actions = [
        {"text": "Vai verso le scale", "callback": c.go_34},
        {"text": "Torna indietro verso il corridoio", "callback": c.go_24}
    ]
    return actions
