"""
Copyright 2021 Charles McMarrow

This python module "backrooms" is a Esolang.

backrooms was inspired by:
    * backrooms Creepypasta/MEME
    * ASCIIDOTS Esolang
    * CISC Architecture

backrooms was designed to be:
    * hackable VIA memory overflow attacks, poor error handling, ect.
    * visually pleasing.
    * enjoyable to write small/medium programs.
    * capable to rewrite all of a program at run-time.
"""


# backrooms
from . import backrooms
from . import backrooms_builtins
from . import backrooms_error
from . import conscious
from . import portal
from . import rooms
from . import rules
from . import stack
from . import translator
from . import whisper

AUTHOR = "Charles McMarrow"

MAJOR, MINOR, MAINTENANCE = 1, 0, 0
VERSION = (MAJOR, MINOR, MAINTENANCE)
