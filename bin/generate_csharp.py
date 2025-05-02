#! /usr/bin/env python3

"""
Used to generate csharp/SzExceptionMapper.cs
"""


INPUT_FILE = "szerrors.json"
OUTPUT_FILE = "csharp/SzExceptionMapper.cs"
PAD_CLASS = 35


def spaces_not_tabs():
    """Because tabs are used in OUTPUT_HEADER, linters get confused with spaces vs. tabs.  This solves it."""


# -----------------------------------------------------------------------------
# --- Main
# -----------------------------------------------------------------------------
