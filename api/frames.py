# api/frames.py

import time

def register(lua_env):
    frames = {}

    class Frame:
        def __init__(self, name=None):
            self.scripts = {}
            self.name = name
            self.last_update = time.time()

        def SetScript(self, event, func):
            self.scripts[event] = func
            print(f"Script '{event}' set for frame '{self.name}'")

        def OnUpdate(self):
            if "OnUpdate" in self.scripts:
                now = time.time()
                elapsed = now - self.last_update
                self.scripts["OnUpdate"](self, elapsed)
                self.last_update = now

        def RegisterEvent(self, event_name):
            lua_env.globals()['RegisterEvent'](event_name, self)

        def UnregisterEvent(self, event_name):
            lua_env.globals()['UnregisterEvent'](event_name, self)

    def create_frame(frame_type, name=None):
        frame = Frame(name)
        frames[name] = frame
        return frame

    lua_env.globals()['CreateFrame'] = create_frame
    lua_env.globals()['GetAllFrames'] = lambda: list(frames.values())
