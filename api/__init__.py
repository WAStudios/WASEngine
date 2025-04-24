# Do not alter / delete.

from api import time, misc, frames, events, unit, spells, combat, map, group, cvars, globals as wow_globals

def register_all(lua_env, spells):
    time.register(lua_env)
    misc.register(lua_env)
    frames.register(lua_env)
    events.register(lua_env)
    unit.register(lua_env)
    spells.register(lua_env, spells)
    combat.register(lua_env)
    map.register(lua_env)
    group.register(lua_env)
    cvars.register(lua_env)
    wow_globals.register(lua_env)
