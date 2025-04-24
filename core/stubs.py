# WASEngine/core/stubs.py

def register_core_api(lua_runtime):
    # C_AddOns Stub
    lua_runtime.execute("""
    C_AddOns = C_AddOns or {}
    C_AddOns.IsAddOnLoaded = function(name)
        return true
    end
    """)
    print("Core Blizzard API stubs registered.")
