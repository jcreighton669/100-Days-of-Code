from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

service = Service("C:/Development/chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie")

options = Options()
options.add_experimental_option(name="detach", value=True)

cookie = driver.find_element(By.ID, value="cookie")

# item_names = [
#     "Cursor",
#     "Grandma",
#     "Factory",
#     "Mine",
#     "Shipment",
#     "Alchemy lab",
#     "Portal",
#     "Time machine",
#     "Elder Pledge"
# ]
item_names = [
    "product0",
    "product1",
    "product2",
    "product3",
    "product4",
    "product5",
    "product6",
    "product7",
    "product8",
    "product9",
    "product10",
    "product11",
    "product12",
    "product13",
    "product14",
    "product15",
    "product16",
    "product17",
]

items = [None] * len(item_names)
# item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_element(By.ID, value="store")
        item_prices = []

        # for price in all_prices:
        #     element_text = price.text
        #     if element_text != "":
        #         cost = int(element_text.split("-")[1].strip().replace(",", ""))
        #         item_prices.append(cost)

        cookie_upgrades = {}
        # for n in range(len(item_prices)):
        #     cookie_upgrades[item_prices[n]] = item_ids[n]

        money_element = driver.find_element(By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, value=to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, value="cps").text
        print(cookie_per_s)
        break
