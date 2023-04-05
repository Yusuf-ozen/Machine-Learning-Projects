from linkedUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Linkedin:

    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password



    def signLinkedin(self):
        self.browser.get("https://www.linkedin.com/home")
        time.sleep(1)
        self.browser.find_element_by_xpath("/html/body/nav/div/a[2]").click()
        time.sleep(2)
        userInput = self.browser.find_element_by_xpath("//*[@id='username']")
        passInput = self.browser.find_element_by_xpath("//*[@id='password']")


        userInput.send_keys(self.username)
        passInput.send_keys(self.password)
        passInput.send_keys(Keys.ENTER)
        # self.browser.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button").click()
        time.sleep(2)
        


    def friends(self):
        self.browser.get("https://www.linkedin.com/mynetwork/")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='ember75']/div/div[1]").click()
        search = self.browser.find_element_by_xpath("//*[@id='mn-connections-search-input']")
        






linked = Linkedin(username, password)

linked.signLinkedin()
linked.friends()

