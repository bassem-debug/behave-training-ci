from selenium import webdriver

from browser import Browser
from pages.home_page import HomePage





def before_scenario(context, scenario):
    option = webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    option.add_argument('headless')

    context.browser = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe", chrome_options=option)
    context.browser.implicitly_wait(30)
    context.browser.set_page_load_timeout(50)
    context.hp=HomePage(context.browser)
def after_scenario(context,scenario):
    context.browser.close()

