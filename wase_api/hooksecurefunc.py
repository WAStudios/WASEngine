def register(lua_env):
    print("Registering hooksecurefunc...")
    lua_env.execute("""
        HookRegistry = HookRegistry or {}

        function hooksecurefunc(funcName, hookFunc)
            if type(funcName) ~= "string" then
                print("hooksecurefunc error: funcName is not a string", tostring(funcName))
                return
            end
            if type(hookFunc) ~= "function" then
                print("hooksecurefunc error: hookFunc is not a function", tostring(hookFunc))
                return
            end
            HookRegistry[funcName] = HookRegistry[funcName] or {}
            table.insert(HookRegistry[funcName], hookFunc)
            print("hooksecurefunc hooked:", funcName)
        end
    """)

    print("hooksecurefunc registered into Lua environment.")
