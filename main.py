# Import the modules
import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from driver import get_driver
from spoof import spoof_timezone_geolocation

# Proxies of England
proxies = ['svynvhhz:42y0esy8gk38@45.43.84.141:6766',
           'svynvhhz:42y0esy8gk38@64.43.90.86:6601',
           'svynvhhz:42y0esy8gk38@64.43.89.129:6388',
           'svynvhhz:42y0esy8gk38@45.43.81.70:5717',
           'svynvhhz:42y0esy8gk38@154.85.125.137:6348',
           'svynvhhz:42y0esy8gk38@138.128.153.166:5200',
           'svynvhhz:42y0esy8gk38@107.181.128.177:5189',
           'svynvhhz:42y0esy8gk38@45.43.84.118:6743',
           'svynvhhz:42y0esy8gk38@64.137.93.245:6702',
           'svynvhhz:42y0esy8gk38@154.85.124.64:5925',
           'svynvhhz:42y0esy8gk38@155.254.49.32:6592',
           'svynvhhz:42y0esy8gk38@107.181.132.122:6100',
           'svynvhhz:42y0esy8gk38@45.43.68.138:5778',
           'svynvhhz:42y0esy8gk38@154.92.114.242:5937',
           'svynvhhz:42y0esy8gk38@154.92.114.28:5723',
           'svynvhhz:42y0esy8gk38@45.43.65.72:6586',
           'svynvhhz:42y0esy8gk38@45.43.70.86:6373',
           'svynvhhz:42y0esy8gk38@45.43.82.65:6059',
           'svynvhhz:42y0esy8gk38@45.43.84.198:6823',
           'svynvhhz:42y0esy8gk38@107.181.148.31:5891',
           'svynvhhz:42y0esy8gk38@216.173.111.208:6918',
           'svynvhhz:42y0esy8gk38@107.181.132.231:6209',
           'svynvhhz:42y0esy8gk38@107.181.142.239:5832',
           'svynvhhz:42y0esy8gk38@107.181.152.237:5274',
           'svynvhhz:42y0esy8gk38@45.43.71.5:6603',
           'svynvhhz:42y0esy8gk38@155.254.49.202:6762',
           'svynvhhz:42y0esy8gk38@198.105.100.63:6314',
           'svynvhhz:42y0esy8gk38@198.105.108.214:6236',
           'svynvhhz:42y0esy8gk38@155.254.49.226:6786',
           'svynvhhz:42y0esy8gk38@198.105.100.178:6429',
           'svynvhhz:42y0esy8gk38@45.43.84.142:6767',
           'svynvhhz:42y0esy8gk38@107.181.148.63:5923',
           'svynvhhz:42y0esy8gk38@155.254.49.7:6567',
           'svynvhhz:42y0esy8gk38@216.173.111.83:6793',
           'svynvhhz:42y0esy8gk38@64.43.91.208:6979',
           'svynvhhz:42y0esy8gk38@198.105.111.64:6742',
           'svynvhhz:42y0esy8gk38@64.43.91.98:6869',
           'svynvhhz:42y0esy8gk38@107.181.154.183:5861',
           'svynvhhz:42y0esy8gk38@107.181.130.156:5777',
           'svynvhhz:42y0esy8gk38@107.181.141.4:6401',
           'svynvhhz:42y0esy8gk38@45.43.81.90:5737',
           'svynvhhz:42y0esy8gk38@154.85.125.30:6241',
           'svynvhhz:42y0esy8gk38@216.173.111.131:6841',
           'svynvhhz:42y0esy8gk38@107.181.142.201:5794',
           'svynvhhz:42y0esy8gk38@45.43.82.41:6035',
           'svynvhhz:42y0esy8gk38@45.43.64.192:6450',
           'svynvhhz:42y0esy8gk38@64.43.90.245:6760',
           'svynvhhz:42y0esy8gk38@154.92.116.184:6496',
           'svynvhhz:42y0esy8gk38@198.105.101.56:5685',
           'svynvhhz:42y0esy8gk38@198.105.101.30:5659',
           'svynvhhz:42y0esy8gk38@107.181.148.223:6083',
           'svynvhhz:42y0esy8gk38@64.43.90.91:6606',
           'svynvhhz:42y0esy8gk38@154.92.112.78:5099',
           'svynvhhz:42y0esy8gk38@107.181.132.100:6078',
           'svynvhhz:42y0esy8gk38@64.137.92.33:6232',
           'svynvhhz:42y0esy8gk38@107.181.152.122:5159',
           'svynvhhz:42y0esy8gk38@45.43.83.199:6482',
           'svynvhhz:42y0esy8gk38@154.85.125.44:6255',
           'svynvhhz:42y0esy8gk38@64.137.92.212:6411',
           'svynvhhz:42y0esy8gk38@156.238.10.14:5096',
           'svynvhhz:42y0esy8gk38@107.181.130.22:5643',
           'svynvhhz:42y0esy8gk38@45.43.64.176:6434',
           'svynvhhz:42y0esy8gk38@154.92.116.31:6343',
           'svynvhhz:42y0esy8gk38@104.143.226.90:5693',
           'svynvhhz:42y0esy8gk38@104.143.224.121:5982',
           'svynvhhz:42y0esy8gk38@45.43.65.79:6593',
           'svynvhhz:42y0esy8gk38@198.105.100.197:6448',
           'svynvhhz:42y0esy8gk38@155.254.48.199:6105',
           'svynvhhz:42y0esy8gk38@138.128.153.82:5116',
           'svynvhhz:42y0esy8gk38@154.85.125.17:6228',
           'svynvhhz:42y0esy8gk38@107.181.152.204:5241',
           'svynvhhz:42y0esy8gk38@107.181.154.27:5705',
           'svynvhhz:42y0esy8gk38@64.43.90.248:6763',
           'svynvhhz:42y0esy8gk38@154.92.116.164:6476',
           'svynvhhz:42y0esy8gk38@107.181.143.2:6133',
           'svynvhhz:42y0esy8gk38@104.143.226.76:5679',
           'svynvhhz:42y0esy8gk38@64.137.92.108:6307',
           'svynvhhz:42y0esy8gk38@45.43.64.40:6298',
           'svynvhhz:42y0esy8gk38@45.43.64.145:6403',
           'svynvhhz:42y0esy8gk38@107.181.132.217:6195',
           'svynvhhz:42y0esy8gk38@64.43.90.208:6723',
           'svynvhhz:42y0esy8gk38@198.105.100.42:6293',
           'svynvhhz:42y0esy8gk38@154.85.125.89:6300',
           'svynvhhz:42y0esy8gk38@154.92.116.92:6404',
           'svynvhhz:42y0esy8gk38@107.181.154.118:5796',
           'svynvhhz:42y0esy8gk38@138.128.153.78:5112',
           'svynvhhz:42y0esy8gk38@107.181.132.146:6124',
           'svynvhhz:42y0esy8gk38@154.85.124.87:5948',
           'svynvhhz:42y0esy8gk38@154.85.125.63:6274',
           'svynvhhz:42y0esy8gk38@104.143.224.1:5862',
           'svynvhhz:42y0esy8gk38@154.85.124.204:6065',
           'svynvhhz:42y0esy8gk38@107.181.154.112:5790',
           'svynvhhz:42y0esy8gk38@45.43.70.252:6539',
           'svynvhhz:42y0esy8gk38@107.181.130.253:5874',
           'svynvhhz:42y0esy8gk38@156.238.10.198:5280',
           'svynvhhz:42y0esy8gk38@154.92.114.221:5916',
           'svynvhhz:42y0esy8gk38@107.181.152.139:5176',
           'svynvhhz:42y0esy8gk38@45.43.70.47:6334',
           'svynvhhz:42y0esy8gk38@107.181.143.167:6298',
           'svynvhhz:42y0esy8gk38@45.43.70.219:6506',

           ]

# Fake Mobile devices useragent to make any request as portable mobile Device
useragent = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 '
    'Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPad; CPU OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 '
    'Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPad; CPU OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.5735.124 '
    'Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/114.1 '
    'Mobile/15E148 Safari/605.1.15',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 '
    'YaBrowser/23.5.6.403.10 SA/3 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 '
    'Chrome/110.0.5481.154 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 '
    'OPR/99.0.0.0',
    'Opera/9.80 (Android; Opera Mini/7.5.33942/191.308; U; en) Presto/2.12.423 Version/12.16',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/534.24 '
    'XiaoMi/MiuiBrowser/13.30.1-gn',
    'Mozilla/5.0 (Linux; Android 10; JNY-LX1; HMSCore 6.11.0.302) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/99.0.4844.88 HuaweiBrowser/13.0.5.303 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 11; en-us; itel P661W Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, '
    'like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 PHX/12.9',
    'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile '
    'Safari/537.36 EdgA/113.0.1774.63',
    'Mozilla/5.0 (Linux; arm_64; Android 12; CPH2205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 '
    'YaBrowser/23.3.3.86.00 SA/3 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) '
    'Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/10.4.2.0',
    'Mozilla/5.0 (Linux; U; Android 13; vi-vn; CPH2159 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/91.0.4472.88 Mobile Safari/537.36 HeyTapBrowser/45.9.5.1.1',
    'Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/114.0 Firefox/114.0',
    'Mozilla/5.0 (Linux; Android 5.1.1; KFSUWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/108.4.6 like '
    'Chrome/108.0.5359.220 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36,'
    'gzip(gfe)',
    'Mozilla/5.0 (Linux; Android 13; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; moto g stylus 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36v',
    'Mozilla/5.0 (Linux; Android 12; moto g stylus 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
    'Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; moto g 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; moto g power (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
    'Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; moto g power (2021)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
    'Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; DE2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile '
    'Safari/537.36',
    'Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) '
    'Version/10.0 Mobile/19E241 Safari/602.1',
    'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) '
    'Version/10.0 Mobile/19A346 Safari/602.1',
    'Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) '
    'Version/10.0 Mobile/15E148 Safari/602.1',
    'Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) '
    'Version/10.0 Mobile/15E148 Safari/602.1',
    'Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) '
    'Version/10.0 Mobile/15E148 Safari/602.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 '
    'Mobile/15A372 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 '
    'Mobile/15A5341f Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 '
    'Mobile/15A5370a Safari/604.1',
    'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058',
    'Mozilla/5.0 (Linux; Android 12; SM-X906C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 '
    'Chrome/52.0.2743.98 Safari/537.36',
]

# Random proxy selection
proxy = random.choice(proxies)


# Random useragent selection
agent = random.choice(useragent)




# Keywords to put it in google search
key = [
    "Put Your keywords here seprated by inverted commas."
]

# Websites to click on after google search
sites = ["Put your link here you want the bot to click on. seprated by commas."
         ]

while True:
    driver = get_driver(agent=agent, proxy=proxy, proxy_folder='Auth')
    try:

        spoof_timezone_geolocation('http', proxy, driver)
        driver.get('https://www.yahoo.com/')
        time.sleep(10)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="header-search-button"]/div/span[1]').click()
        time.sleep(4.75)
        search = driver.find_element(By.XPATH, '//*[@id="header-search-input"]')
        search.send_keys('Google.com')
        time.sleep(5)
        search.send_keys(Keys.ENTER)
        time.sleep(8)
        driver.find_element(By.XPATH, '//*[@id="main-algo"]/section[1]/section[1]/div[1]/div/div/span').click()
        time.sleep(30)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # driver.find_element(By.XPATH, '').click()
        time.sleep(5)
        # Search button click
        search = driver.find_element(By.XPATH, "//*[@name='q']")
        search.click()

        # Getting Random keyword to write in google search bar
        keywords = random.choice(key)
        # Writing keyword in search bar
        search.send_keys(keywords)
        time.sleep(5)
        # Clicking enter to get search results
        search.send_keys(Keys.ENTER)

        # Waiting time for the search results
        time.sleep(15)

        # Clicking on the URL if found

        for _ in range(1, 20):
            try:
                url_text = driver.find_element(By.XPATH, '//*[@role="text"]').text
                print(url_text)
                if url_text in sites:
                    driver.find_element(By.XPATH, '//*[@role="text"]').click()
                else:
                    # scrolling down up to show random movement as user.
                    driver.execute_script("return document.body.scrollHeight / 12")
                    time.sleep(5)
                pass
            except:
                pass

        # Closing browser
        driver.quit()
        time.sleep(60)
    except:
        driver.quit()
        continue
