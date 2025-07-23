from typing import Optional, List


class WarCraft3Transformation:
    '''
        Store Animation Data
        '''
    def __init__( self ):
        self.tracks_count: int          = 0
        self.interpolation_type: int    = 0
        self.times: List[int]           = []
        self.values                     = []


