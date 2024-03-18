import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ex
from selenium.webdriver.remote.webelement import WebElement
from game_options import GameOptions
from pages.basicGame import Principal

@pytest.fixture
def selenium(selenium):
        selenium.implicitly_wait(10)
        selenium.maximize_window()
        selenium.get("https://rps-master-three.vercel.app")
        return selenium

@pytest.fixture
def basicGame(selenium):
     return Principal(selenium)

class TestRockPaperScissors:
    def test_VerifyDefaultVisibilityOfAssets(self, basicGame):
        assert type(basicGame.find_paper_btn()) == WebElement, "Element not found"
        assert type(basicGame.find_rock_btn()) == WebElement,  "Element not found"
        assert type(basicGame.find_scissors_btn()) == WebElement,  "Element not found"
        assert type(basicGame.find_result_lbl()) == WebElement,  "Element not found"
        assert type(basicGame.find_gamemode_btn()) == WebElement,  "Element not found"
        assert type(basicGame.find_reset_btn()) == WebElement,  "Element not found"
        assert type(basicGame.find_score_lbl()) == WebElement,  "Element not found"
        assert basicGame.get_score() == "0"

    def test_PlayGamePaper(self, basicGame):
        basicGame.click_paper_btn()
        computer_choice = basicGame.play_game(GameOptions.PAPER)
        print("Selected move by computer: {choice:s}".format(choice=computer_choice.value))
        msg = basicGame.get_result_msg()
        assert self.logic_game(computer_choice, msg), "Result text is not the same choice the result image"
        if "lose" in msg:
            assert "-" in basicGame.get_score(), "User must be on negative"
        else:
            assert "-" not in basicGame.get_score(), "User must be on positive"

    def logic_game(self, computer_choice, msg):
         match computer_choice:
              case GameOptions.PAPER:
                   return "paper" in msg
              case GameOptions.ROCK:
                   return "rock" in msg
              case GameOptions.SCISSORS:
                    return "scissors" in msg
            