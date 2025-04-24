# api/frames.py

import time

def register(lua_env):
    frames = {}

    class Frame:
        def __init__(self, frame_type="Frame", name=None, parent=None):
            self.frame_type = frame_type
            self.name = name or f"Frame_{len(frames)}"
            self.parent = parent
            self.children = []
            self.scripts = {}
            self.last_update = time.time()
            self.visible = True
            self.frame_level = 0
            self.frame_strata = "MEDIUM"
            self.width = 0
            self.height = 0
            self.position = None
            self.mouse_enabled = False
            self.secure_template = None
            self.regions = []

            if parent:
                parent.children.append(self)

            frames[self.name] = self
            if self.name:
                lua_env.globals()[self.name] = self  # Global access in Lua

            print(f"Created frame '{self.name}' of type '{self.frame_type}'")

        # --- Script Handling ---
        def SetScript(self, event, func):
            self.scripts[event] = func
            print(f"Script '{event}' set for frame '{self.name}'")

        def GetScript(self, event):
            return self.scripts.get(event, None)

        # --- Event and Update Simulation ---
        def OnUpdate(self):
            if "OnUpdate" in self.scripts and self.IsShown():
                now = time.time()
                elapsed = now - self.last_update
                self.scripts["OnUpdate"](self, elapsed)
                self.last_update = now

        def TriggerEvent(self, event_name, *args):
            if "OnEvent" in self.scripts and self.IsShown():
                print(f"Frame '{self.name}' handling event '{event_name}'")
                self.scripts["OnEvent"](self, event_name, *args)

        # --- Event Registration ---
        def RegisterEvent(self, event_name):
            lua_env.globals()['RegisterEvent'](event_name, self)

        def UnregisterEvent(self, event_name):
            lua_env.globals()['UnregisterEvent'](event_name, self)

        # --- Visibility ---
        def Show(self):
            self.visible = True
            print(f"Frame '{self.name}' shown")
            if "OnShow" in self.scripts:
                self.scripts["OnShow"](self)

        def Hide(self):
            self.visible = False
            print(f"Frame '{self.name}' hidden")
            if "OnHide" in self.scripts:
                self.scripts["OnHide"](self)

        def IsShown(self):
            if self.parent and not self.parent.IsShown():
                return False
            return self.visible

        # --- Parent ---
        def SetParent(self, parent):
            if self.parent:
                self.parent.children.remove(self)
            self.parent = parent
            parent.children.append(self)
            print(f"Frame '{self.name}' parent set to '{parent.name}'")

        # --- Frame Level ---
        def SetFrameLevel(self, level):
            self.frame_level = level
            print(f"Frame '{self.name}' frame level set to {level}")

        def GetFrameLevel(self):
            return self.frame_level

        # --- Frame Strata ---
        def SetFrameStrata(self, strata):
            self.frame_strata = strata
            print(f"Frame '{self.name}' strata set to '{strata}'")

        def GetFrameStrata(self):
            return self.frame_strata

        # --- Size ---
        def SetWidth(self, width):
            self.width = width

        def SetHeight(self, height):
            self.height = height

        def SetSize(self, width, height):
            self.width = width
            self.height = height

        def GetWidth(self):
            return self.width

        def GetHeight(self):
            return self.height

        # --- Position / Anchoring ---
        def SetPoint(self, anchor, relativeTo=None, relativePoint=None, xOffset=0, yOffset=0):
            self.position = {
                "anchor": anchor,
                "relativeTo": relativeTo.name if relativeTo else None,
                "relativePoint": relativePoint,
                "xOffset": xOffset,
                "yOffset": yOffset
            }
            print(f"Frame '{self.name}' positioned: {self.position}")

        def ClearAllPoints(self):
            self.position = None
            print(f"Frame '{self.name}' cleared all points")

        # --- Mouse Interaction ---
        def EnableMouse(self, enable):
            self.mouse_enabled = enable
            print(f"Frame '{self.name}' mouse interaction {'enabled' if enable else 'disabled'}")

        def IsMouseEnabled(self):
            return self.mouse_enabled

        # --- Regions: Textures / FontStrings ---
        def CreateTexture(self):
            texture = {"type": "Texture", "visible": True, "parent": self}
            self.regions.append(texture)
            print(f"Texture created for frame '{self.name}'")
            return texture

        def CreateFontString(self):
            fontstring = {"type": "FontString", "text": "", "visible": True, "parent": self}
            self.regions.append(fontstring)
            print(f"FontString created for frame '{self.name}'")
            return fontstring

        # --- Secure Template Stub ---
        def SetAttribute(self, key, value):
            # Stub for secure templates
            self.secure_template = self.secure_template or {}
            self.secure_template[key] = value
            print(f"Frame '{self.name}' secure attribute set: {key} = {value}")

    # --- Frame Factory ---
    def create_frame(frame_type="Frame", name=None, parent=None, template=None):
        frame = Frame(frame_type, name, parent)
        if template:
            frame.secure_template = template  # Template awareness
            print(f"Frame '{frame.name}' using template '{template}'")
        # Inject region creation
        frame.CreateTexture = lambda: frame.CreateTexture()
        frame.CreateFontString = lambda: frame.CreateFontString()
        return frame

    # --- Utilities ---
    def run_updates():
        for frame in frames.values():
            frame.OnUpdate()

    def trigger_frame_event(frame_name, event_name, *args):
        frame = frames.get(frame_name)
        if frame:
            frame.TriggerEvent(event_name, *args)

    # Inject into Lua
    lua_env.globals()['CreateFrame'] = create_frame
    lua_env.globals()['GetAllFrames'] = lambda: list(frames.values())
    lua_env.globals()['RunFrameUpdates'] = run_updates
    lua_env.globals()['TriggerFrameEvent'] = trigger_frame_event