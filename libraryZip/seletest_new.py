from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import pandas as pd
from selenium.webdriver.firefox.service import Service
  
# 读取数据  
df = pd.read_csv('libraryZip/filtered_data.csv')  
  
# 设置 geckodriver.exe 的路径和日志文件的路径  
geckodriver_path = 'D:/0 Hallie Jin/0 Hallie/geckodriver-v0.34.0-win64/geckodriver.exe'  
service = Service(geckodriver_path)    
driver = webdriver.Firefox(service=service)

wait = WebDriverWait(driver, 2)
   
  
# 遍历DataFrame中的前10行  
for index, row in df.iloc[0:10].iterrows():  
    driver.get('https://www.google.com/maps')
    sleep(2)
    search_box = wait.until(EC.element_to_be_clickable((By.ID, 'searchboxinput')))
    search_box.clear()
    search_box.send_keys(row['Address'])
    search_box.send_keys(Keys.ENTER)
    sleep(3)  # Wait for search results to load

    try:
        # 尝试寻找匹配XPath的元素
        zip_code_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[3]/button/div/div[2]/div[1]')))
        zip_code = zip_code_element.text
        df.at[index, 'zip'] = zip_code
    except:
        try:
            # 点击搜索结果列表中的第一个结果
            first_result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.w6Uhzf > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)')))
first_result.click()

try:
    # 再次尝试寻找匹配XPath的元素
    zip_code_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'Io6YTe') and contains(@class, 'fontBodyMedium') and contains(@class, 'kR99db')]")))
    zip_code = zip_code_element.text
    df.at[index, 'zip'] = zip_code
except:
    try:
        # 如果还是找不到，尝试点击由CSS选择器.hfpxzc指定的元素
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.hfpxzc')))
        next_button.click()
        
        # 等待页面加载并再次尝试匹配XPath
        zip_code_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'Io6YTe') and contains(@class, 'fontBodyMedium') and contains(@class, 'kR99db')]")))
        zip_code = zip_code_element.text
        df.at[index, 'zip'] = zip_code
    except Exception as e:
        print(f"Error extracting zip code for address: {row['Address']} after attempting all strategies. Error: {e}")  
  
# 将数据保存到Excel文件  
df.to_excel('libraryZip/aaa.xlsx', index=False)  
  
# 关闭浏览器  
driver.quit()  
