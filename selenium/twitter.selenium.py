from twitterUserInfo import username, password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



class Twitter:

    def __init__(self, username, password):
        self.browserFile = webdriver.ChromeOptions()    # dili ingilizce olarak kullanabilmeyi saglar.
        self.browserFile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})  # Bu dili tarayici icinde aktif etmekyi saglar.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserFile)
        self.username = username
        self.password = password



    def signIn(self):
        self.browser.get("https://twitter.com/login")
        self.browser.maximize_window()
        time.sleep(1)
        userIn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
        # passIn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
        passIn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
        time.sleep(1)

        userIn.send_keys(self.username)
        passIn.send_keys(self.password)
        passIn.send_keys(Keys.ENTER)



twitter = Twitter(username, password)
twitter.signIn()