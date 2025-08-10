import yaml
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / "config.yaml"

#Loading the contents of the file

with open (CONFIG_FILE,"r") as f:
    CONFIG = yaml.safe_load(f)

