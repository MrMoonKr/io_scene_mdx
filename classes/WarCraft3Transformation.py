from typing import Optional, List


class WarCraft3Transformation:
    '''
        Store Animation Data
        '''
    def __init__( self ):
        self.tracks_count: int          = 0
        '''keyframe count'''
        self.interpolation_type: int    = 0
        '''keyframe interpolation type'''
        self.times: list[int]           = []
        '''keyframe times'''
        self.values: tuple[int|float]   = []
        '''keyframe vaues'''


