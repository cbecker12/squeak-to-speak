import json
import sys
from pathlib import Path

def get_base_directory():

    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent

    return Path(__file__).resolve().parent

BASE_DIR = get_base_directory()

CONFIG_FILE = BASE_DIR / "config.json"

if not CONFIG_FILE.exists(): 
    raise FileNotFoundError( 
        f"Could not find config.json\n" 
        f"Expected location:\n{CONFIG_FILE}" 
    ) 

with CONFIG_FILE.open(encoding="utf-8") as file:
    CONFIG = json.load(file)

HOST = CONFIG["server"]["host"]
PORT = CONFIG["server"]["port"]
KEY_MAP = CONFIG["keyboard"]["key_map"] 
