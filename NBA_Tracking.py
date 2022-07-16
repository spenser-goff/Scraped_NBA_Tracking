from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://www.nba.com/stats/players/catch-shoot/?Season={}&SeasonType=Regular%20Season'
years = ['2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19']
col_names = []
row_entries = []
for year in years[0:1]:
    driver = webdriver.Firefox(executable_path=r"C:\Users\spens\Basketball\geckodriver.exe")

    print(year)
    driver.get(url.format(year))
    time.sleep(5)
    driver.switch_to.window(driver.current_window_handle)
    driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/div/table/thead/tr/th[5]').click()
    res = Select(driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select'))
    res.select_by_visible_text('All')
    time.sleep(0.95)
    th_elements = driver.find_elements_by_xpath('/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/div/table/thead/tr/th')
    #print(type(th_elements))
    #print(len(th_elements))

    for elt in th_elements:
        col_names.append(str(elt.text))
    tr_elements = driver.find_elements_by_xpath('/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/div/table/tbody/tr')
    #print(type(tr_elements))
    #print(len(tr_elements))
    for elt in tr_elements:
        row = str(elt.text)
        row_entries.append(row.split(' '))
    time.sleep(2)
    driver.quit()

for name in col_names:
    print(name)