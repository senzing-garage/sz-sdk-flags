#! /usr/bin/env python3

"""
Used to generate go/main.go
"""


INPUT_FILE = "szerrors.json"
OUTPUT_FILE = "go/szerrortypes.go"


def spaces_not_tabs():
    """Because tabs are used in OUTPUT_HEADER, linters get confused with spaces vs. tabs.  This solves it."""


# -----------------------------------------------------------------------------
# --- Main
# -----------------------------------------------------------------------------
