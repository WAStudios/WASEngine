# api/events.py

def register(lua_env):
    event_registry = {}

    def register_event(event_name, frame):
        if event_name not in event_registry:
            event_registry[event_name] = []
        event_registry[event_name].append(frame)
        print(f"Frame '{frame.name}' registered for event '{event_name}'")

    def unregister_event(event_name, frame):
        if event_name in event_registry:
            if frame in event_registry[event_name]:
                event_registry[event_name].remove(frame)
                print(f"Frame '{frame.name}' unregistered from event '{event_name}'")

    def trigger_event(event_name, *args):
        frames = event_registry.get(event_name, [])
        print(f"Triggering event '{event_name}' for {len(frames)} frame(s)")
        for frame in frames:
            if "OnEvent" in frame.scripts:
                frame.scripts["OnEvent"](frame, event_name, *args)

    lua_env.globals()['RegisterEvent'] = register_event
    lua_env.globals()['UnregisterEvent'] = unregister_event
    lua_env.globals()['TriggerEvent'] = trigger_event
