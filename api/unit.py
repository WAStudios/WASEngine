# api/unit.py

import uuid
import time

def register(lua_env):
    units = {
        "player": {
            "name": "TestPlayer",
            "health": 900,
            "max_health": 1000,
            "exists": True,
            "guid": str(uuid.uuid4()),
            "class": ("Mage", "MAGE"),  # name, fileID
            "is_dead": False,
            "power": 100,
            "level": 70,
            "auras": [
                ("Arcane Intellect", "Interface\\Icons\\Spell_Holy_MagicalSentry", "HELPFUL", 3600, "player", True),
                ("Power Word: Fortitude", "Interface\\Icons\\Spell_Holy_WordFortitude", "HELPFUL", 1800, "player", False)
            ],
            "casting": None,  # (spellName, rank, icon, startTimeMS, endTimeMS, isTradeSkill, spellID)
            "channeling": None
        },
        "target": {
            "name": "DummyTarget",
            "health": 1200,
            "max_health": 1200,
            "exists": True,
            "guid": str(uuid.uuid4()),
            "class": ("Warrior", "WARRIOR"),
            "is_dead": False,
            "power": 50,
            "level": 72,
            "auras": [
                ("Weakened Soul", "Interface\\Icons\\Spell_Holy_AshesToAshes", "HARMFUL", 10, "player", False)
            ],
        }
    }

    # Simulate casting a spell manually
    def start_cast(unit, spellName, spellID, duration):
        start_time = time.time()
        end_time = start_time + duration
        units[unit]["casting"] = (
            spellName, None, "Interface\\Icons\\Spell_Holy_HolySmite", start_time * 1000, end_time * 1000, False, spellID
        )
        lua_env.globals()['TriggerEvent']("UNIT_SPELLCAST_START", unit)

    def stop_cast(unit):
        units[unit]["casting"] = None
        lua_env.globals()['TriggerEvent']("UNIT_SPELLCAST_STOP", unit)

    lua_env.globals()['UnitName'] = lambda unit: units[unit]["name"] if unit in units and units[unit]["exists"] else None
    lua_env.globals()['UnitExists'] = lambda unit: units[unit]["exists"] if unit in units else False
    lua_env.globals()['UnitHealth'] = lambda unit: units[unit]["health"] if unit in units else 0
    lua_env.globals()['UnitHealthMax'] = lambda unit: units[unit]["max_health"] if unit in units else 0
    lua_env.globals()['UnitGUID'] = lambda unit: units[unit]["guid"] if unit in units else None
    lua_env.globals()['UnitClass'] = lambda unit: units[unit]["class"] if unit in units else (None, None)
    lua_env.globals()['UnitIsDead'] = lambda unit: units[unit]["is_dead"] if unit in units else False
    lua_env.globals()['UnitPower'] = lambda unit: units[unit]["power"] if unit in units else 0
    lua_env.globals()['UnitLevel'] = lambda unit: units[unit]["level"] if unit in units else 0

    lua_env.globals()['UnitAura'] = lambda unit, index: units[unit]["auras"][index - 1] if unit in units and index <= len(units[unit]["auras"]) else None
    lua_env.globals()['UnitBuff'] = lambda unit, index: next((aura for i, aura in enumerate(units[unit]["auras"]) if aura[2] == "HELPFUL" and i == index - 1), None)
    lua_env.globals()['UnitDebuff'] = lambda unit, index: next((aura for i, aura in enumerate(units[unit]["auras"]) if aura[2] == "HARMFUL" and i == index - 1), None)

    lua_env.globals()['StartUnitCast'] = start_cast
    lua_env.globals()['StopUnitCast'] = stop_cast

    lua_env.globals()['UnitCastingInfo'] = lambda unit: units[unit]["casting"] if units[unit]["casting"] else None
    lua_env.globals()['UnitChannelInfo'] = lambda unit: units[unit]["channeling"] if units[unit]["channeling"] else None