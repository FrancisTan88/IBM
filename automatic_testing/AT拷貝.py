# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By

# options_o = Options()
# options_o.add_argument("--disable-notifications")  #不啟用通知

# chrome = webdriver.Chrome('./chromedriver', options=options_o)
# chrome.get("https://sit01-websubmission.chailease.com.my/websubmission-ui/")


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# options = Options()
# # options.add_argument("start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://sit01-websubmission.chailease.com.my/websubmission-ui/")

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# ser = Service("C:\\chromedriver")
# op = Options()
# s = webdriver.Chrome(service=ser, options=op)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# s = Service('./chromedriver')
# driver = webdriver.Chrome(service=s)
# url = 'https://www.google.com'
# driver.get(url)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

op = Options()
op.add_argument("start-maximized")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)
driver.get("https://www.youtube.com/")