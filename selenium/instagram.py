from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password


    def signIn(self):
        # url = "https://www.instagram.com/accounts/login/"
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        usernameInput= self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        # passing = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        # passing.click()
        time.sleep(2)
        

        passing = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        time.sleep(1)
        passage = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        time.sleep(1)
        

    def getFollowers(self):
        self.browser.get("https://www.instagram.com/yusuf_ozen03/")

        error = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/ul/li[2]/a/span").click()
        # followersLink.click()


insta = Instagram(username, password)
insta.signIn()
insta.getFollowers()




