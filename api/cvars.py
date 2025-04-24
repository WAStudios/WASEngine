# api/cvars.py

def register(lua_env):
    cvars = {
        "scriptErrors": "1",
        "uiScale": "0.8",
    }

    addons = {
        "WeakAuras": {
            "Title": "WeakAuras",
            "Version": "5.19.7",
            "Author": "WeakAuras Team"
        }
    }

    lua_env.globals()['GetCVar'] = lambda name: cvars.get(name, "0")
    lua_env.globals()['SetCVar'] = lambda name, value: cvars.update({name: str(value)})
    lua_env.globals()['GetCVarBool'] = lambda name: cvars.get(name, "0") == "1"

    lua_env.globals()['GetAddOnMetadata'] = lambda addon, field: addons.get(addon, {}).get(field, None)
    lua_env.globals()['IsAddOnLoaded'] = lambda name: name in addons
