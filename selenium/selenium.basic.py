from selenium import webdriver
import time



driver = webdriver.Chrome()



url = "http://instagram.com"

driver.get(url)

time.sleep(1)      # 3 saniyte durur.
driver.maximize_window()      # tarayici acildiktan sonra ekrani buyutur.

driver.save_screenshot("instagram-homepage.png")   # ss alip buraya kaydeder.

url = "http://instagram.com/yusuf_ozen03"    # baska bir sayfaya yonlendirir.
driver.get(url)

print(driver.title)   # girdigimiz sayfanin basligini yazdirir.

if "yusuf" in driver.title:
    driver.save_screenshot("yusuf-ozem.png")



time.sleep(2)
driver.minimize_window()
time.sleep(1)

driver.back()   # sayfaya tekrar doner.
time.sleep(1)
driver.close()      # actigin tarayiciyi kapatir.
