from selenium import webdriver
import time

# start web browser
browser=webdriver.Firefox()

# get source code
browser.get("https://en.wikipedia.org")
html = browser.page_source
time.sleep(2)
print(html)

# close web browser
browser.close()

















