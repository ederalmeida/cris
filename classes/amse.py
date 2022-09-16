from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os


class amse_site():
    def __init__ (self):
        self.dir_path = os.getcwd()
        self.chrome = self.dir_path + '/apoio/webdriver/chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r"user-data-dir="+self.dir_path+"/apoio/webdriver/profile/wpp")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://amse.ons.org.br/intunica/')
        self.login = 'rmiranda'

    def logon(self):
        login = self.driver.find_element(By.ID, 'txtLogin')
        login.send_keys(self.login)

    def teste():
        print(os.getcwd())