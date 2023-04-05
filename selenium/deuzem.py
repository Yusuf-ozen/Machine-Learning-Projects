from deuUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Deuzem:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password



    def signedOnline(self):
        self.browser.get("https://online.deu.edu.tr/portal")
        time.sleep(1)
        self.browser.maximize_window()
        time.sleep(1)
        userEnter = self.browser.find_element_by_xpath("//*[@id='eid']")
        passEnter = self.browser.find_element_by_xpath("//*[@id='pw']")
        

        userEnter.send_keys(self.username)
        passEnter.send_keys(self.password)
        passEnter.send_keys(Keys.ENTER)
        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@id='topnav']/li[2]/a[2]/span").click()
        canliDers = self.browser.find_element_by_xpath("//*[@id='toolMenu']/ul/li[11]/a/span[2]")
        canliDers.click()


deuzem = Deuzem(username, password)
deuzem.signedOnline()



