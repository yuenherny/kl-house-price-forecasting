"""Helper functions for notebooks."""
import os
from pathlib import Path
import re

ROOT_DIR = Path(os.getcwd()).parent
DATA_DIR = ROOT_DIR / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'


def convert_mixed_fraction_to_decimal(value):
    """Convert a mixed fraction to a decimal."""
    match = re.match(r'(\d+)½', value)
    if match:
        whole_part = float(match.group(1))
        fractional_part = 0.5  # Since ½ represents 1/2
        return whole_part + fractional_part

    match = re.match(r'(\d+)¾', value)
    if match:
        whole_part = float(match.group(1))
        fractional_part = 0.75  # Since ¾ represents 3/4
        return whole_part + fractional_part

    match = re.match(r'(\d+)⅖', value)
    if match:
        whole_part = float(match.group(1))
        fractional_part = 0.4  # Since ⅖ represents 2/5
        return whole_part + fractional_part

    # Return 0 for cases where the format doesn't match
    return value
