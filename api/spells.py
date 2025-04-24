# api/spells.py

import time

def register(lua_env, spells):
    cooldowns = {}

    def get_spell_info(spellID):
        return spells.get(spellID, (f"Spell {spellID}", "Interface\\Icons\\INV_Misc_QuestionMark", 0, 0, 0, spellID))

    def get_spell_texture(spellID):
        info = spells.get(spellID)
        if info:
            return info[1]
        return "Interface\\Icons\\INV_Misc_QuestionMark"

    lua_env.globals()['GetSpellInfo'] = get_spell_info
    lua_env.globals()['GetSpellTexture'] = get_spell_texture
    lua_env.globals()['GetSpellCooldown'] = lambda spellID: cooldowns.get(spellID, (0, 0, False))
    lua_env.globals()['IsUsableSpell'] = lambda spellID: (True, False)
    lua_env.globals()['SetSpellCooldown'] = lambda spellID, duration: cooldowns.update({spellID: (time.time(), duration, True)})
