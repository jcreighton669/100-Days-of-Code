from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
service = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# num_articles = driver.find_element(by="id", value="articlecount")
# # print(num_articles.text)
#
# search = driver.find_element(by="name", value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("https://www.appbrewery.co/p/newsletter")
newsletter_signup = driver.find_element(
    By.ID,
    value="member_email"
)
newsletter_signup.send_keys("justincreighton2006@gmail.com")
# newsletter_signup.send_keys(Keys.ENTER)
subscribe = driver.find_element(
    By.NAME,
    value="commit"
)
subscribe.click()
print("Completed")