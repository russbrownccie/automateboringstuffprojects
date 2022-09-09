from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://inventwithpython.com')

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
# driver_path = '/usr/local/bin/chromedriver'
# drvr = webdriver.Chrome(options = options, executable_path = driver_path)
# drvr.get('https://stackoverflow.com')
#
# const webdriver = require('selenium-webdriver');
# const chromeOptions = new chrome.Options()
# chromeOptions.setChromeBinaryPath('/usr/bin/brave-browser')
#
# let driver = new webdriver.Builder()
#     .forBrowser('brave')
#     .setChromeOptions(chromeOptions)
#     .build();
#
# driver.get('http://example.com');