from faceUserInfo import username, password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


# driver = webdriver.Chrome()

# url = "http://facebook.com"

# driver.get(url)


class Facebook:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password


    def signFace(self):
        self.browser.get("http://facebook.com")
        time.sleep(1)
        userInput = self.browser.find_element_by_xpath("//*[@id='email']")
        passInput = self.browser.find_element_by_xpath("//*[@id='pass']")



        userInput.send_keys(self.username)
        passInput.send_keys(self.password)
        passInput.send_keys(Keys.ENTER)
        time.sleep(2)


    def friends(self):
        self.browser.get("https://www.facebook.com/friends")
        time.sleep(2)
        friendEnter = self.browser.find_element_by_xpath("//*[@id='mount_0_0_y+']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[4]/a/div[1]/div[2]/div[1]/div/div/div/spans")
        friendEnter.click()
        time.sleep(2)


face = Facebook(username, password)
face.signFace()
face.friends()

