from session import Session
from exceptions import ExitGameException

class Game:
    
    def __init__(self):
        pass

    def play_a_game(self):
        session = Session()
        try:
            session.start_new_game()
        except ExitGameException:
            pass
        self.play_a_game()
        