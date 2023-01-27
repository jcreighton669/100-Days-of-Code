from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://python.org/")
events = driver.find_elements(by="class name", value="event-widget")

print(events)