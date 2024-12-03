from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas

driver = webdriver.Chrome()

driver.get('https://coindesk.com/indices')

rows = driver.find_elements(By.CLASS_NAME, 'group')

coin_abbreviations = [row.find_elements(By.TAG_NAME, 'p')[1].text for row in rows]
coin_names = [row.find_elements(By.TAG_NAME, 'p')[2].text for row in rows]
prices = [row.find_elements(By.TAG_NAME, 'p')[3].text for row in rows]
market_caps = [row.find_elements(By.TAG_NAME, 'p')[4].text for row in rows]
volumes = [row.find_elements(By.TAG_NAME, 'p')[5].text for row in rows]

coins_df = pandas.DataFrame({
    'Abbr': coin_abbreviations,
    'Coin Name': coin_names,
    'Prices': prices,
    'Market Caps': market_caps,
    'Volumes': volumes
})


print(coins_df)