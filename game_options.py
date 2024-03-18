from enum import Enum
class GameOptions(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"
    LIZARD = "lizard"
    SPOCK = "spock"
    #
    @classmethod
    def from_css(cls, comp_option):
        return cls(comp_option)