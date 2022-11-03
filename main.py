import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

USERNAME = "FoodandBeerWorld"
PASSWORD = "aBEge7g+J;vkLF)"
URL = "https://www.instagram.com"

chrome_driver_path = "/Users/CarlosMartinez/Desktop/Coding/chromedriver"


class instagram_follow_bot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def get_followers(self):
        self.driver.get(URL)
        time.sleep(2)
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(3)
        try:
            not_now_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")
            not_now_btn.click()
        except NoSuchElementException:
            pass
        time.sleep(3)
        search_input = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input")
        search_input.send_keys("Food")
        time.sleep(3)
        first_choice = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div")
        first_choice.click()
        time.sleep(5)
        followers_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers_btn.click()
        time.sleep(1)
        while True:
            time.sleep(2)
            follow_btns = self.driver.find_elements(By.CSS_SELECTOR, "li button")
            for button in follow_btns:
                try:
                    button.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                    cancel_button.click()


bot = instagram_follow_bot()
bot.get_followers()



