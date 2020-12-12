import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random

#time to refresh page (seconds)
Timer = random.randint(50, 120)

#youtube link
link = 'https://www.youtube.com/watch?v=fw0FoRpeIhc&autoplay=1'

#number of views
views = 130

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(link)

driver2 = webdriver.Chrome(ChromeDriverManager().install())
driver2.get(link)

driver3 = webdriver.Chrome(ChromeDriverManager().install())
driver3.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    driver2.refresh()
    driver3.refresh()
    print(i*3)