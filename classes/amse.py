import os
import logging
import pyautogui as pg
import PySimpleGUI as sg
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from apoio import gravar_log_cadastro_documento_inadimplente as glcdi

class amse_site():
    def __init__ (self):
        os.environ['WDM_LOG'] = str(logging.NOTSET)
        self.dir_path = os.getcwd()
        #self.chrome = os.sep.join([self.dir_path, 'apoio', 'webdriver'])
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r"user-data-dir=" + os.sep.join([self.dir_path,'lib', 'apoio', 'webdriver', 'profile', 'wpp']))
        self.options.add_argument(r'log_level=0')
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.options)
        self.driver.get('http://amse.ons.org.br/intunica/')

    def logon(self, login_informado, passwd_informado):
        self.driver.find_element(By.ID, 'txtLogin').send_keys(login_informado)  # preenchendo login
        self.driver.find_element(By.ID, 'txtSenha').send_keys(passwd_informado) # preenchendo senha
        self.driver.find_element(By.ID, 'btnOk').click()                        # clicando ok
        self.driver.implicitly_wait(2)
        # TODO essa parte do try não está legal. Precisa ser melhorada.
        try:
            alerta_autenticacao = Alert(self.driver)
            sg.popup(alerta_autenticacao.text)
            alerta_autenticacao.accept()
            self.driver.close()
            return False
        except:
            pass
        self.driver.implicitly_wait(2)
        try:
            self.driver.switch_to.frame('PerfFoco')
            Select(self.driver.find_element(By.ID,'drpDownSistema')).select_by_value('AMSE      ')
            Select(self.driver.find_element(By.ID, 'ddwListaPerfis')).select_by_value('AMSE_AGETR - AMSE - Agentes de Transmissão                                                                       ')
            self.driver.find_element(By.ID, 'ImageBtnConfirmar').click()
        except:
            pass

        self.driver.switch_to.frame('topFrame')
        self.driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr[5]/td/table/tbody/tr/td[2]/div').click()
        self.driver.implicitly_wait(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('FormTrabalho')
        self.driver.implicitly_wait(1)
        button = self.driver.find_element(By.XPATH, '//*[@id="mni_2592"]')
        self.driver.execute_script("arguments[0].click();", button)
        self.driver.implicitly_wait(1)
        return True

    def inserir_documento_inadimplente(self, documento, caminho):
        try:
            concessao_site = self.driver.find_element(By.ID, 'lbl_empresa')
            concessao_ja_atribuida = True
        except:
            concessao_ja_atribuida = False
        
        if concessao_ja_atribuida:
            if concessao_site.text in documento.concessao:
                executar_insercao = True
            else:
                executar_insercao = False
        
        if not concessao_ja_atribuida:
            try:
                Select(self.driver.find_element(By.ID, 'cmp_pesquisa_age_ddl_pesquisa')).select_by_visible_text(documento.concessao)
                self.driver.find_element(By.ID, 'cmp_pesquisa_age_ibt_lupapesquisa').click()
                executar_insercao = True
            except:
                executar_insercao = False

        if not executar_insercao:
            glcdi.gravar_log(caminho, documento, 'Inadimplência não Cadastrada. Usuário não tem acesso a essa concessão!')
        else:
            campo_cliente = self.driver.find_element(By.NAME, 'txt_usuaria')
            campo_cliente.clear()
            campo_cliente.send_keys(documento.cliente)
            Select(self.driver.find_element(By.NAME, 'cbo_mes_ano_Apur')).select_by_value(documento.competencia)
            self.driver.implicitly_wait(1)
            Select(self.driver.find_element(By.NAME, 'cbo_vencimento')).select_by_value(documento.vencimento)
            self.driver.find_element(By.NAME, 'ibt_pesquisar').click()
            self.driver.find_element(By.ID, 'grdLiquidacao__ctl2_chk_pagou').click()
            Select(self.driver.find_element(By.ID,'grdLiquidacao__ctl2_ddl_tpocorr')).select_by_value('2')
            self.driver.find_element(By.ID, 'imgAtualizar').click()
            self.driver.find_element(By.ID, 'ibtAdimpTotal').click()
            alerta_sucesso = Alert(self.driver)
            alerta_sucesso.accept()
            self.driver.implicitly_wait(1)
            glcdi.gravar_log(caminho, documento, 'Inadimplência Cadastrada com sucesso!')

    def logoff(self):
        self.driver.close()