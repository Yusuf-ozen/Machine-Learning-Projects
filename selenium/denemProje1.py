secim = int(input("1- DEUZEME GIRIS  2 - LINKEDINE GIRIS  3 - INSTAGRAMA GIRIS  4 - FACEBOOKA GIRIS\n1 den 4 e kadar bir sayi seciniz : "))


if(secim == 1):
    print("Deuzem giris ekranina hosgeldiniz")


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







elif(secim == 2):

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
            self.browser.maximize_window()
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






elif(secim == 3):
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
        

            passing = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
            time.sleep(1)
            passage = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
            time.sleep(1)
        

        def getFollowers(self):
            self.browser.get("https://www.instagram.com/yusuf_ozen03/")

            # error = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/ul/li[2]/a/span").click()
            # followersLink.click()


    insta = Instagram(username, password)
    insta.signIn()
    #insta.getFollowers()




elif(secim == 4):
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





else:
    print("YANLIS NUMARA GIRDINIZ PROGRAMI TEKRAR CALISTIRINIZ!!!")



































































































