from typing import Optional


class WarCraft3Sequence:
    '''애니메이션 트랙 정보'''
    def __init__(self):
        self.name: Optional[str] = None
        '''애니메이션 트랙 이름'''
        self.movement_speed: int = 0
        '''이동 속도'''
        self.interval_start: int = 0
        '''시작 프레임 번호'''
        self.interval_end: int = 0
        '''끝 프레임 번호'''
