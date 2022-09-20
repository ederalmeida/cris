from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import os
import time
import pyautogui as pg


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
        login = self.driver.find_element(By.ID, 'txtLogin')
        login.send_keys(login_informado)
        passwd = self.driver.find_element(By.ID, 'txtSenha')
        passwd.send_keys(passwd_informado)
        botao_ok_login = self.driver.find_element(By.ID, 'btnOk')
        botao_ok_login.click()
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
        campo_codigo_usuario = self.driver.find_element(By.NAME, 'txt_usuaria')
        campo_codigo_usuario.clear()
        campo_codigo_usuario.send_keys(documento.cliente)
        pg.press('enter')
        self.driver.implicitly_wait(2)
        campo_apuracao = self.driver.find_element(By.NAME, 'cbo_mes_ano_Apur')
        campo_apuracao_combo = Select(campo_apuracao)
        campo_apuracao_combo.select_by_value(documento.competencia)
        self.driver.implicitly_wait(6)
        campo_vencimento = self.driver.find_element(By.NAME, 'cbo_vencimento')
        campo_vencimento_combo = Select(campo_vencimento)
        campo_vencimento_combo.select_by_value(documento.vencimento)
        botao_pesquisar = self.driver.find_element(By.NAME, 'ibt_pesquisar')
        botao_pesquisar.click()
        time.sleep(5)

        
    def liquidacao_antiga(self):
        localizacao_botao_liquidacao = pg.locateOnScreen(self.imagem_liquidacao, confidence=0.7)
        if localizacao_botao_liquidacao != None:
            pg.click(x=localizacao_botao_liquidacao[0] + 5, y=localizacao_botao_liquidacao[1] + 5)
        time.sleep(1)
        localizacao_botao_informacao = pg.locateOnScreen(self.imagem_informacao, confidence=0.7)
        if localizacao_botao_informacao != None:
            pg.click(x=localizacao_botao_informacao[0] + 5, y=localizacao_botao_informacao[1] + 5)
        time.sleep(10)