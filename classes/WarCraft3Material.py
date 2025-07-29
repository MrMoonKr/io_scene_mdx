#from typing import List

from .WarCraft3Layer import WarCraft3Layer


class WarCraft3Material:
    def __init__( self ):
        self.name: str                      = None
        self.layers: list[WarCraft3Layer]   = []
        self.hd: bool                       = False
