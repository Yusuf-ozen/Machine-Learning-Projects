from selenium import webdriver


driver = webdriver.Chrome()    # secmek istediğin driver i tanımlıyorsun.

url = "http://sadikturan.com"      # gitmek istedğin siteyi yaz.

driver.get(url)            # driver dan get url ile gidiyorsun.
