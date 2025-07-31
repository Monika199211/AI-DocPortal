from pathlib import Path
import yaml

def load_config(config_path: Path = Path("config") / "config.yaml") -> dict:
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config

load_config()
