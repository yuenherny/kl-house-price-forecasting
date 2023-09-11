import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from helpers import DATA_DIR

url = "https://www.brickz.my/transactions/residential/kuala-lumpur/non-landed/?range=1933+Oct-"
print(DATA_DIR)

start = time.time()

projects = []
next_page = True

driver = webdriver.Chrome()
driver.get(url)

while next_page:
    for i in range(10):
        try:
            project_name = driver.find_element(By.CSS_SELECTOR, f"#ptd_list_table > tbody > tr:nth-child({i+1}) > td:nth-child(1) > a").text
            location = driver.find_element(By.CSS_SELECTOR, f"#ptd_list_table > tbody > tr:nth-child({i+1}) > td:nth-child(1) > span").text
            url_link = driver.find_element(By.CSS_SELECTOR, f"#ptd_list_table > tbody > tr:nth-child({i+1}) > td:nth-child(1) > a").get_attribute("href")
            tenure = driver.find_element(By.CSS_SELECTOR, f"#ptd_list_table > tbody > tr:nth-child({i+1}) > td:nth-child(2) > span").text
            median_psf = driver.find_element(By.CSS_SELECTOR, f'#ptd_list_table > tbody > tr:nth-child({i+1}) > td:nth-child(3) > span').text
            median_price = driver.find_element(By.CSS_SELECTOR, f'#ptd_list_table > tbody > tr:nth-child({i+1}) > td:nth-child(4) > span').text
            filed_transactions = driver.find_element(By.CSS_SELECTOR, f'#ptd_list_table > tbody > tr:nth-child({i+1}) > td:nth-child(5) > a').text
            
            projects.append([project_name, location, url_link, tenure, median_psf, median_price, filed_transactions])
        except:
            print("Less than 10 rows available.")
    
    try:
        driver.find_element(
            By.CSS_SELECTOR, 
            "#post-467083 > div:nth-child(3) > div.ptd_list_table_title.table > div.ptd_table_toolbar > div > a.next.page-numbers"
        ).click()
    except:
        next_page = False
        print("At the end of the pagination.")
driver.close()

end = time.time()
print(f"Time taken: {end - start} seconds")

column_names = ['project_name', 'location', 'url_link', 'tenure', 'median_psf', 'median_price', 'filed_transactions']
df = pd.DataFrame(projects, columns=column_names)
df.to_excel(DATA_DIR / 'raw' / 'townships_non-landed_KL.xlsx', index=False)
