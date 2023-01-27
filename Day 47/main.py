from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com/AMOLEN-Printer-Filament-Triple-Printing/dp/B09Y8WQXK4/?_encoding=UTF8&pd_rd_w=hUXqb&content-id=amzn1.sym.18be86ac-b16e-400a-b42f-43f216645498&pf_rd_p=18be86ac-b16e-400a-b42f-43f216645498&pf_rd_r=154GTV45K0JCAKN7F6E0&pd_rd_wg=Duck9&pd_rd_r=ce0ae472-3778-4803-8cf7-defc565362b7&ref_=pd_gw_bmx_gp_r523mywo&th=1")
price = driver.find_element(by="class name", value="a-price")

print(price.text)