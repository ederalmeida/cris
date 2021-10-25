import pandas as pd
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


class SGPMRBase:
    def __init__(self):
        load_dotenv()
        self.LOGIN_PAGE = os.environ.get('LOGIN_PAGE')
        self.BASE_PAGE = os.environ.get('BASE_PAGE')
        self.USERNAME = os.environ.get('SGPMRUSERNAME')
        self.PASSWORD = os.environ.get('SGPMRPASSWORD')
        self.EXCEL_FOLDER = os.environ.get('EXCEL_FOLDER')
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option('prefs', {
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True
        }
                                               )
        self.driver = webdriver.Chrome(options=chrome_options)

    def aguardar_loading(self, xpath: str):
        WebDriverWait(self.driver, 1200).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, xpath)
            )
        )

        WebDriverWait(self.driver, 1200).until_not(
            expected_conditions.presence_of_element_located(
                (By.XPATH, xpath)
            )
        )

    def aguardar_toast(self):
        WebDriverWait(self.driver, 1200).until(
            expected_conditions.presence_of_element_located(
                (By.ID, 'toast-container')
            )
        )

    def get_excel_file(self, filename: str) -> pd.DataFrame:
        return pd.read_excel(
            self.EXCEL_FOLDER + filename,
            dtype=str,
            keep_default_na=False
        )

    def login(self):
        self.driver.get(self.LOGIN_PAGE)
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div/input').send_keys(self.USERNAME)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/input[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[1]/input').send_keys(self.PASSWORD)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/input[1]').click()
        time.sleep(5)

    def menu_principal(self):
        self.driver.get(self.BASE_PAGE)
        self.aguardar_loading(xpath='/html/body/div[3]/div[2]/div/div/div')

    def run(self):
        pass
