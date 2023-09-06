"""Helper functions for notebooks."""
import os
from pathlib import Path

ROOT_DIR = Path(os.getcwd()).parent
DATA_DIR = ROOT_DIR / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
