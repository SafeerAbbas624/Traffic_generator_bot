import os

from selenium import webdriver
from proxy import WEBRTC
from proxy import FINGERPRINT
from proxy import ACTIVE
from proxy import create_proxy_folder

# Getting the driver ready with loaded all data
def get_driver(agent, proxy, proxy_folder):
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_experimental_option(
        "excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    prefs = {"intl.accept_languages": 'en_GB,en',
             "credentials_enable_service": False,
             "profile.password_manager_enabled": False,
             "profile.default_content_setting_values.notifications": 2,
             "download_restrictions": 3}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('extensionLoadTimeout', 120000)
    options.add_argument(f"user-agent={agent}")
    options.add_argument("--mute-audio")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-features=UserAgentClientHint')
    options.add_argument("--disable-web-security")
    webdriver.DesiredCapabilities.CHROME['loggingPrefs'] = {
        'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
    options.add_extension(WEBRTC)
    options.add_extension(FINGERPRINT)
    options.add_extension(ACTIVE)
    create_proxy_folder(proxy, proxy_folder)
    options.add_argument(f"--load-extension={os.getcwd()}/{proxy_folder}")

    driver = webdriver.Chrome(options=options)
    # driver.set_window_size(400, 800)
    # # overriding dimensions of screen
    # set_device_metrics_override = dict({
    #     "width": 375,
    #     "height": 812,
    #     "deviceScaleFactor": 50,
    #     "mobile": True
    # })
    # driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', set_device_metrics_override)
    return driver
