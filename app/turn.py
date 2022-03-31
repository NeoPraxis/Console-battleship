from shot import Shot
from player import Player

class Turn:
    
    def __init__(self, shot: Shot, player: Player):
        if not isinstance(shot, Shot):
            raise TypeError('shot (first argument) must be of type Shot')

        if not isinstance(player, Player):
            raise TypeError('player (second argument) must be of type Player')

        self.shot = shot
        self.player = player
        
