import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ex
from selenium.webdriver.remote.webelement import WebElement
from game_options import GameOptions

class Principal:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.paper_btn = None
        self.rock_btn = None
        self.scissors_btn = None
        self.score_lbl = None
        self.reset_btn = None
        self.wait = WebDriverWait(driver, 10)

    def find_paper_btn(self):
        self.paper_btn = self.wait.until(ex.element_to_be_clickable((By.ID, "paper")))
        return self.paper_btn
    
    def find_rock_btn(self):
        self.rock_btn = self.wait.until(ex.element_to_be_clickable((By.ID, "rock")))
        return self.rock_btn
    
    def find_scissors_btn(self):
        self.scissors_btn = self.wait.until(ex.element_to_be_clickable((By.ID, "scissors")))
        return self.scissors_btn

    def find_score_lbl(self):
        self.score_lbl = self.wait.until(ex.visibility_of_element_located((By.CLASS_NAME, "score")))
        return self.score_lbl
    
    def find_reset_btn(self):
        self.reset_btn = self.wait.until(ex.element_to_be_clickable((By.CLASS_NAME, "reset")))
        return self.reset_btn
    
    def find_gamemode_btn(self):
        self.gameMode_btn = self.wait.until(ex.element_to_be_clickable((By.CLASS_NAME, "game-mode-toggle")))
        return self.gameMode_btn
    
    def find_rules_btn(self):
        self.rules_btn = self.wait.until(ex.element_to_be_clickable((By.CLASS_NAME, "rules")))
        return self.rules_btn
    
    def find_result_lbl(self):
        self.result_lbl = self.wait.until(ex.visibility_of_element_located((By.XPATH, "//section[contains(@class, 'result')]/p")))
        return self.result_lbl
    
    def find_result_img(self):
        self.result_img = self.wait.until(ex.visibility_of_element_located((By.XPATH, "//div[contains(@class,'computer-choice')]/div/img")))
        return self.result_img
    
    def click_paper_btn(self):
        if self.paper_btn == None:
            self.find_paper_btn()
        
        self.paper_btn.click()

    def click_rock_btn(self):
        if self.rock_btn == None:
            self.find_rock_btn()
        
        self.rock_btn.click()

    def click_scissors_btn(self):
        if self.scissors_btn == None:
            self.find_scissors_btn()
        
        self.scissors_btn.click()

    def click_reset_btn(self):
        if self.reset_btn == None:
            self.find_reset_btn()
        
        self.reset_btn.click()
    
    def get_score(self):
        if self.score_lbl == None:
            self.find_score_lbl()
        
        return self.score_lbl.text
    
    def get_result_msg(self):
        if self.score_lbl == None:
            self.find_result_lbl()
        
        return self.result_lbl.text
        
    def play_game(self, choice) -> GameOptions:
        match choice:
            case GameOptions.PAPER:
                self.click_paper_btn()
            case GameOptions.ROCK:
                self.click_rock_btn()
            case GameOptions.SCISSORS:
                self.click_scissors_btn()

        return GameOptions.from_css(self.find_result_img().get_attribute("alt").split(" ").pop())


    

#Hace una clase