# api/combat.py
combat_log_data = {}

def register(lua_env):
    def combat_log_get_current_event_info():
        return combat_log_data.get("event", None)

    def trigger_combat_log_event(event_name, sourceGUID, sourceName, destGUID, destName, spellID, spellName, spellSchool):
        # Simulate a basic SPELL_DAMAGE or similar event
        combat_log_data["event"] = (
            event_name,         # Event Name
            False,              # HideCaster
            sourceGUID,
            sourceName,
            0x511,              # SourceFlags
            0x0,                # SourceRaidFlags
            destGUID,
            destName,
            0x512,              # DestFlags
            0x0,                # DestRaidFlags
            spellID,
            spellName,
            spellSchool,
            100,                # Amount (if damage)
            0,                  # Overkill
            0,                  # SchoolMask
            False,              # Critical
            False,              # Glancing
            False               # Crushing
        )
        # Fire the event globally
        lua_env.globals()['TriggerEvent']("COMBAT_LOG_EVENT_UNFILTERED")

    lua_env.globals()['CombatLogGetCurrentEventInfo'] = combat_log_get_current_event_info
    lua_env.globals()['TriggerCombatLogEvent'] = trigger_combat_log_event
