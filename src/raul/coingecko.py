import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from google.cloud import datastore

# datetime.datetime.utcnow()

CATEGORIA_COIN = 'cryptocurrency'
CATEGORIA_COIN_DATA = 'data_cryptocurrency'

client = datastore.Client()
query = client.query(kind=CATEGORIA_COIN)
query.add_filter("status", "=", True)
list_coin = list(query.fetch())
print(list_coin)

if len(list_coin) > 0:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    for coin in list_coin:
        driver.get("https://www.coingecko.com/es/monedas/"+coin["name"])
        driver.implicitly_wait(10)
        price = driver.find_element(By.XPATH, '//div[@class="text-3xl"]//span[@class="no-wrap"]').text
        price_final = price.split(" ")
        #print(money["name"] + " | " + price_final[0] + " | " + str(time.time()))

        key = client.key(CATEGORIA_COIN_DATA, coin["code"])
        query = client.query(kind=CATEGORIA_COIN_DATA, ancestor=key)
        array_historic = []
        if len(list(query.fetch())) > 0:
            array_historic = list(query.fetch())[0]["coingecko"]["price"]["historic"]

        array_historic.append({
           "timestamp": datetime.datetime.now().timestamp(),
           "amount": price_final[0]
         }
        )

        entity = datastore.Entity(key=key)
        entity.update({
            'coingecko': {
                'price': {
                    'historic': array_historic,
                    'update_at': datetime.datetime.now().timestamp()
                },
                'markets': {} 
            },
            'status': 'OK'
        })
        client.put(entity)
        result = client.get(key)
        print(result)
    driver.quit()
   
else:
    print("No existe monedas registradas")




