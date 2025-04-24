from lupa import LuaRuntime
from api import register_all
from core.spell_updater import ensure_spells_loaded
import time

class WASEngine:
    def __init__(self):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        register_all(self.lua)
        self.running = False

    def run_lua(self, lua_code):
        return self.lua.execute(lua_code)

    def start_main_loop(self, duration=5, update_interval=0.1):
        # Start OnUpdate thread properly
        self.lua.globals()['StartUpdateThread']()
        self.running = True
        start_time = time.time()
        while self.running and (time.time() - start_time) < duration:
            time.sleep(update_interval)
        self.running = False
