import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

list_money = [
    {
        "name": "bitcoin",
        "code": "BTC",
        "status": True
    },
    {
        "name": "ethereum",
        "code": "ETH",
        "status": True
    },
    {
        "name": "darwinia-network-native-token",
        "code": "RING",
        "status": False
    }
]

driver = webdriver.Chrome()
driver.implicitly_wait(10)

for money in list_money:
    if money["status"] == True:
        driver.get("https://www.coingecko.com/es/monedas/"+money["name"])
        price = driver.find_element(By.XPATH, '//div[@class="text-3xl"]//span[@class="no-wrap"]').text
        price_final = price.split(" ")
        print(money["name"] + " | " + price_final[0] + " | " + str(time.time()))





driver.implicitly_wait(30)

driver.quit()

