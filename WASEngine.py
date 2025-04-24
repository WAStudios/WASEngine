import os
from core.icon_extractor import ensure_icon

# Test icon name (use one you know exists)
icon_name = "Interface\\Icons\\Spell_Frost_FrostBolt02"

# Attempt to extract and convert
icon_path = ensure_icon(icon_name)

if icon_path and os.path.exists(icon_path):
    print(f"SUCCESS: Icon extracted and converted to PNG at: {icon_path}")
else:
    print("FAILURE: Icon extraction or conversion failed.")
