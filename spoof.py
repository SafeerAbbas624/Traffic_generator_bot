import random

import requests
from faker import Faker
from selenium.common import WebDriverException
from requests import RequestException



# Spoofing of timezone and geolocation
def spoof_timezone_geolocation(proxy_type, proxy, driver):
    fake = Faker()
    try:
        proxy_dict = {
            "http": f"{proxy_type}://{proxy}",
            "https": f"{proxy_type}://{proxy}",
        }
        resp = requests.get(
            "http://ip-api.com/json", proxies=proxy_dict, timeout=30)

        if resp.status_code == 200:
            location = resp.json()
            tz_params = {'timezoneId': location['timezone']}
            latlng_params = {
                "latitude": location['lat'],
                "longitude": location['lon'],
                "accuracy": random.randint(20, 100)
            }
            info = f"ip-api.com | Lat : {location['lat']} | Lon : {location['lon']} | TZ: {location['timezone']}"
        else:
            raise RequestException

    except RequestException:
        location = fake.location_on_land()
        tz_params = {'timezoneId': location[-1]}
        latlng_params = {
            "latitude": location[0],
            "longitude": location[1],
            "accuracy": random.randint(20, 100)
        }
        info = f"Random | Lat : {location[0]} | Lon : {location[1]} | TZ: {location[-1]}"

    try:
        driver.execute_cdp_cmd('Emulation.setTimezoneOverride', tz_params)

        driver.execute_cdp_cmd(
            "Emulation.setGeolocationOverride", latlng_params)

    except WebDriverException:
        pass

    return print(info)

