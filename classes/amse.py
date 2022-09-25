import os
import time
import pyautogui as pg
import PySimpleGUI as sg
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class amse_site():
    def __init__ (self):
        self.dir_path = os.getcwd()
        self.chrome = self.dir_path + r'/apoio/webdriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r"user-data-dir="+self.dir_path+"/apoio/webdriver/profile/wpp")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://amse.ons.org.br/intunica/')
        self.imagem_liquidacao = self.dir_path + '/imagens/amse_botao_liquidacao.png'
        self.imagem_informacao = self.dir_path + '/imagens/amse_botao_informacao.png'
        self.imagem_codigo_usuario = self.dir_path + '/imagens/amse_codigo_usuario.png'

    def logon(self, login_informado, passwd_informado):
        self.driver.find_element(By.ID, 'txtLogin').send_keys(login_informado)  # preenchendo login
        self.driver.find_element(By.ID, 'txtSenha').send_keys(passwd_informado) # preenchendo senha
        self.driver.find_element(By.ID, 'btnOk').click()                        # clicando ok
        self.driver.implicitly_wait(2)
        self.driver.switch_to.frame('PerfFoco')
        Select(self.driver.find_element(By.ID,'drpDownSistema')).select_by_value('AMSE      ')
        Select(self.driver.find_element(By.ID, 'ddwListaPerfis')).select_by_value('AMSE_AGETR - AMSE - Agentes de Transmissão                                                                       ')
        self.driver.find_element(By.ID, 'ImageBtnConfirmar').click()
        self.driver.switch_to.frame('topFrame')
        self.driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr[5]/td/table/tbody/tr/td[2]/div').click()
        self.driver.implicitly_wait(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('FormTrabalho')
        self.driver.implicitly_wait(1)
        button = self.driver.find_element(By.XPATH, '//*[@id="mni_2592"]')
        self.driver.execute_script("arguments[0].click();", button)
        self.driver.implicitly_wait(11)

    def inserir_documento_inadimplente(self, documento):
        Select(self.driver.find_element(By.ID, 'cmp_pesquisa_age_ddl_pesquisa')).select_by_visible_text(documento.concessao)
        campo_cliente = self.driver.find_element(By.NAME, 'txt_usuaria')
        campo_cliente.clear()
        campo_cliente.send_keys(documento.cliente)
        self.driver.find_element(By.ID, 'cmp_pesquisa_age_ibt_lupapesquisa').click()
        #pg.press('enter')
        self.driver.implicitly_wait(2)
        Select(self.driver.find_element(By.NAME, 'cbo_mes_ano_Apur')).select_by_value(documento.competencia)
        self.driver.implicitly_wait(6)
        Select(self.driver.find_element(By.NAME, 'cbo_vencimento')).select_by_value(documento.vencimento)
        self.driver.find_element(By.NAME, 'ibt_pesquisar').click()
        time.sleep(5)