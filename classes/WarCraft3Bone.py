from typing import Optional

from ..classes.WarCraft3Node import WarCraft3Node


class WarCraft3Bone( WarCraft3Node ):
    def __init__( self ):
        super().__init__( 'bone' )
        self.geoset_id: Optional[int] = None
        self.geoset_animation_id: Optional[int] = None

