
class WarCraft3Layer:
    '''
        재질을 구성하는 하나의 레이어.  
        재질은 레이어의 집합.  
        '''
    def __init__(self):
        self.filterMode         = None
        self.shadingFlags       = None
        self.texture_id         = None
        self.textureAnimationId = None
        self.coordId            = None
        self.alpha              = None
        self.material_alpha     = None
        self.material_texture_id = None
        self.emissive_gain      = None
        self.fresnel_color      = None
        self.fresnel_opacity    = None
        self.fresnel_team_color = None
        self.emissions          = None
        self.fresnel_alpha      = None
        self.map_ids            = None
