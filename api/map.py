# api/map.py

def register(lua_env):
    unit_map_data = {
        "player": {
            "mapID": 1001,
            "position": (0.45, 0.55, 0.0),  # x, y, z
        },
        "target": {
            "mapID": 1002,
            "position": (0.75, 0.20, 0.0),
        }
    }

    lua_env.globals()['C_Map'] = {
        'GetBestMapForUnit': lambda unit: unit_map_data[unit]["mapID"] if unit in unit_map_data else None,
        'GetPlayerMapPosition': lambda mapID, unit: unit_map_data[unit]["position"] if unit in unit_map_data and unit_map_data[unit]["mapID"] == mapID else (None, None, None)
    }

    lua_env.globals()['UnitPosition'] = lambda unit: unit_map_data[unit]["position"] if unit in unit_map_data else (None, None, None)
