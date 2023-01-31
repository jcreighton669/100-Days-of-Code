from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://python.org/")

event_times = driver.find_elements(by="class name", value="event-widget time")
# for time in event_times:
#     print(time.text)

event_names = driver.find_elements(by="class name", value="event-widget li a")
# for event in event_names:
#     print(event.text)

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

driver.quit()