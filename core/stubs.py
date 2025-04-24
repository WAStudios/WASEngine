# WASEngine/core/stubs.py

def register_sandbox(lua_runtime):
    # Ensure WeakAuras is globally recognized everywhere
    lua_runtime.execute("""
    _G.WeakAuras = _G.WeakAuras or {}
    WeakAuras = _G.WeakAuras  -- Sync local WeakAuras to global
    WeakAuras.Private = WeakAuras.Private or {}
    """)

    # LibStub Stub
    lua_runtime.execute("""
    LibStub = LibStub or function(libname, silent)
        local libs = _G._Libs or {}
        _G._Libs = libs
        if not libs[libname] then
            libs[libname] = {
                Embed = function(self, target)
                    return target
                end
            }
        end
        return libs[libname]
    end
    """)

    # Basic WoW API
    lua_runtime.execute("""
    function GetAddOnMetadata(addon, field)
        return "FakeMetaData"
    end
    function IsAddOnLoaded(addon)
        return true
    end
    """)

    # Addon Env Simulation (select(2, ...))
    lua_runtime.execute("""
    select = function(index, ...)
        if index == 2 then
            return WeakAuras.Private
        end
        return nil
    end
    """)

    # C_AddOns Stub
    lua_runtime.execute("""
    C_AddOns = C_AddOns or {}
    C_AddOns.IsAddOnLoaded = function(name)
        return true
    end
    """)

    print("WASEngine sandbox stubs registered.")
