
import random
from . import Introduction, Desicion, Result, Bot, C


class PlayerBot(Bot):
    def play_round(self):
        if self.player.round_number == 1:
            yield Introduction
        yield Desicion, dict(bid_for_oil=random.randint(2000, 5500))
        yield Result
        
