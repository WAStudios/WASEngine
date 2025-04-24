# api/time.py

import threading
import time

def register(lua_env):
    lua_env.globals()['GetTime'] = lambda: time.time()

    def c_timer_after(delay, func):
        def delayed_call():
            time.sleep(delay)
            func()
        threading.Thread(target=delayed_call).start()

    lua_env.globals()['C_Timer'] = {
        'After': c_timer_after
    }
