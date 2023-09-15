import pandas as pd
import time
from tqdm import tqdm

from selenium import webdriver
from selenium.webdriver.common.by import By

from helpers import DATA_DIR

print(DATA_DIR / 'raw' / 'townships_non-landed_KL.xlsx')

df = pd.read_excel(DATA_DIR / 'raw' / 'townships_non-landed_KL.xlsx')

start = time.time()
transactions = []

driver = webdriver.Chrome()
column_names = ['project_name', 'spa_date', 'address', 'building_type', 'tenure', 'rooms', 'lot_size', 'price_psf', 'price']
for project_name, url in tqdm(zip(df['project_name'], df['url_link']), total=len(df['url_link'])):
    
    driver.get(url)

    next_page = True

    while next_page:
        for i in range(20):
            try:
                spa_date = driver.find_element(By.CSS_SELECTOR, f"#ptd_list_detail_table > tbody > tr:nth-child({i+1}) > td:nth-child(1)").text
                address = driver.find_element(By.CSS_SELECTOR, f"#ptd_list_detail_table > tbody > tr:nth-child({i+1}) > td:nth-child(2)").text
                building_type = driver.find_element(By.CSS_SELECTOR, f"#ptd_list_detail_table > tbody > tr:nth-child({i+1}) > td:nth-child(3)").text
                tenure = driver.find_element(By.CSS_SELECTOR, f"#ptd_list_detail_table > tbody > tr:nth-child({i+1}) > td:nth-child(4)").text
                rooms = driver.find_element(By.CSS_SELECTOR, f"#ptd_list_detail_table > tbody > tr:nth-child({i+1}) > td:nth-child(5)").text
                lot_size = driver.find_element(By.CSS_SELECTOR, f"#ptd_list_detail_table > tbody > tr:nth-child({i+1}) > td:nth-child(6)").text
                price_psf = driver.find_element(By.CSS_SELECTOR, f"#ptd_list_detail_table > tbody > tr:nth-child({i+1}) > td:nth-child(7)").text
                price = driver.find_element(By.CSS_SELECTOR, f"#ptd_list_detail_table > tbody > tr:nth-child({i+1}) > td:nth-child(8)").text
                transactions.append([project_name, spa_date, address, building_type, tenure, rooms, price_psf, price])
            except:
                pass
                # print("Less than 20 rows available.")
        
        try:
            driver.find_element(
                By.CSS_SELECTOR, 
                "#post-467083 > div:nth-child(3) > div.ptd_list_table_title.table > div.ptd_table_toolbar > div > a.next.page-numbers"
            ).click()
        except:
            next_page = False
            # print("At the end of the pagination.")

    df2 = pd.DataFrame(transactions, columns=column_names)
    df2.to_excel(DATA_DIR / 'transactions_non-landed_KL.xlsx', index=False)

driver.close()

end = time.time()
print(f"Time taken: {end - start} seconds")

df2 = pd.DataFrame(transactions, columns=column_names)
df2.to_excel(DATA_DIR / 'transactions_non-landed_KL_full.xlsx', index=False)
print(transactions)

