import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random

#time to refresh page (seconds)
Timer = random.randint(160, 200)
sometimes = random.randint(0,1)

#youtube link
link = 'https://www.youtube.com/watch?v=fw0FoRpeIhc&autoplay=1'

#number of views
views = 130

cp = webdriver.ChromeOptions()
cp.add_argument("--incognito")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=cp)
driver.get(link)

if(sometimes==1):
    driver2 = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=cp)
    driver2.get(link)

# driver3 = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=cp)
# driver3.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    if(sometimes==1):
        time.sleep(5)
        driver2.refresh()
    # driver3.refresh()
    print(i*3)