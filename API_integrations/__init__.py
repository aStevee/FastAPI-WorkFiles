import sys


if len(sys.argv) > 0:

    """In the future change this file to cordinate witch files we want"""
    from calculations import *
    from graphic_deign import *
else:
    raise SystemError("Ther's an error in API Integrations!")
