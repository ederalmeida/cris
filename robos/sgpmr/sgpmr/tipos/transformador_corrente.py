from sgpmr.base import SGPMRBase
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time


class TransformadorCorrente(SGPMRBase):
    def run(self):
        resultado_arquivo = self.EXCEL_FOLDER + 'transformador_corrente_resultado.csv'
        df_dados = self.get_excel_file(filename='Planilhas TC´s Victor3.xlsx')
        df_dados_2 = pd.DataFrame()
        for _, dados in df_dados.iterrows():
            self.menu_principal()
            # dados
            seq = dados['Seq']
            agrupamento_obra = dados['Agrupamento da Obra']
            tipo_equipamento = dados['Tipo de Equipamento']
            agente = dados['Agente']
            instalacao = dados['Instalação']
            instalacao = instalacao.strip()

            modulo = dados['Módulo']
            modulo = modulo.strip()

            tensao_nominal = dados['Tensão Nominal (kV)']
            if '.' in tensao_nominal:
                tensao_nominal = tensao_nominal.replace('.', ',')
            tipo_agente = dados['Tipo de Agente']

            funcao_transmissao = dados['Função de Transmissão']
            funcao_transmissao = funcao_transmissao.strip()

            outra_funcao = dados['Outra Função']
            origem_indicacao = dados['Origem da Indicação']
            prazo = dados['Prazo']
            revitalizacao_necessaria = dados['Revitalização Necessária']
            justificativa = dados['Justificativa']
            tipo_revitalizacao = dados['Tipo da Revitalização']
            motivacao = dados['Motivação da Revitalização']
            observacao = dados['Observação']

            data_necessidade_sistemica = dados['Data de Necessidade Sistêmica']
            data_necessidade_sistemica = pd.to_datetime(data_necessidade_sistemica, format='%Y-%m-%d')
            data_necessidade_sistemica = data_necessidade_sistemica.strftime('%d/%m/%Y')

            projeto_originou_indicacao = dados['Projeto que Originou a Indicação']

            custo_estimado = dados['Custo Estimado (R$)']
            custo_estimado = pd.to_numeric(custo_estimado)
            custo_estimado = '{0:.2f}'.format(custo_estimado)
            custo_estimado = custo_estimado.replace('.', '')

            valor_nm_cris_cc = dados['Valor Nominal da Crista da Corrente de Curto-circuito (kA)']
            valor_nm_cris_cc = pd.to_numeric(valor_nm_cris_cc)
            valor_nm_cris_cc = '{0:.2f}'.format(valor_nm_cris_cc)
            valor_nm_cris_cc = valor_nm_cris_cc.replace('.', '')

            quantidade = dados['Quantidade']
            cod_ident = dados['Código de Identificação']
            fabricante = dados['Fabricante']
            modelo = dados['Modelo']
            num_serie = dados['Nº Série']
            ano_inicio_oper = dados['Ano Início Operação']
            taxa_deprec = dados['Taxa Depreciação (%)']
            taxa_deprec = pd.to_numeric(taxa_deprec)
            taxa_deprec = '{0:.2f}'.format(taxa_deprec)
            taxa_deprec = str(taxa_deprec).replace('.', '')

            ano_fim_vida = dados['Ano Fim Vida Útil']

            capacidade_nom_cc = dados['Capacidade Nominal de Curto-Circuito (kA)']
            capacidade_nom_cc = pd.to_numeric(capacidade_nom_cc)
            capacidade_nom_cc = '{0:.2f}'.format(capacidade_nom_cc)
            capacidade_nom_cc = capacidade_nom_cc.replace('.', '')

            capacidade_nom_corr = dados['Capacidade Nominal de Corrente (A)']
            capacidade_nom_corr = pd.to_numeric(capacidade_nom_corr)
            capacidade_nom_corr = '{0:.2f}'.format(capacidade_nom_corr)
            capacidade_nom_corr = capacidade_nom_corr.replace('.', '')

            capacidade_nom_cc_novo = dados['Capacidade Nominal de Curto-circuito (kA) *']
            capacidade_nom_cc_novo = pd.to_numeric(capacidade_nom_cc_novo)
            capacidade_nom_cc_novo = '{0:.2f}'.format(capacidade_nom_cc_novo)
            capacidade_nom_cc_novo = capacidade_nom_cc_novo.replace('.', '')

            capacidade_nom_corr_novo = dados['Capacidade Nominal de Corrente (A) **']
            capacidade_nom_corr_novo = pd.to_numeric(capacidade_nom_corr_novo)
            capacidade_nom_corr_novo = '{0:.2f}'.format(capacidade_nom_corr_novo)
            capacidade_nom_corr_novo = capacidade_nom_corr_novo.replace('.', '')

            print(f'Cadastrando {seq}...')

            # btn novo cadastro
            btn_novo = self.driver.find_element_by_xpath('/html/body/div[2]/nav/div[2]/ul/li[1]/button')
            btn_novo.click()

            self.aguardar_loading(xpath='/html/body/div[3]/div[2]/div/div/div')

            # campos
            try:
                fd_agrupamento_obra = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[1]/span')
                fd_agrupamento_obra.click()
                fd_agrupamento_obra_resp = self.driver.find_element_by_xpath(r"//li[text()='" + agrupamento_obra + "']")
                fd_agrupamento_obra_resp.click()
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em agrupamento obra']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_tp_equip = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/span')
                fd_tp_equip.click()
                fd_tp_equip_resp = self.driver.find_element_by_xpath(r"//li[text()='" + tipo_equipamento + "']")
                fd_tp_equip_resp.click()
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em tipo de equipamento']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_agente = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[1]/div/div/div[4]/div[1]/div/div[1]/span')
                fd_agente.click()
                fd_agente_resp = self.driver.find_element_by_xpath(r"//li[text()='" + agente + "']")
                fd_agente_resp.click()
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em agente']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                self.aguardar_loading(xpath='/html/body/div[4]/div[2]/div/div/div')

                fd_instalacao = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[1]/div/div/div[4]/div[2]/div/div[1]/span')
                fd_instalacao.click()
                fd_instalacao_resp = self.driver.find_element_by_xpath(r"//li[text()='" + instalacao + "']")
                fd_instalacao_resp.click()
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em instalacao']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                self.aguardar_loading(xpath='/html/body/div[4]/div[2]/div/div/div')

                fd_modulo = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[1]/div/div/div[6]/div[1]/div/div[1]/span')
                fd_modulo.click()
                time.sleep(2)
                fd_modulo_resp = self.driver.find_element_by_xpath(r"//li[text()='" + modulo + "']")
                time.sleep(0.2)
                fd_modulo_resp.click()
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em modulo']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_tensao = self.self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[1]/div/div/div[6]/div[2]/div/div[1]/span')
                fd_tensao.click()
                time.sleep(2)
                fd_tensao_resp = self.driver.find_element_by_xpath(r"//li[text()='" + tensao_nominal + "']")
                fd_tensao_resp.click()
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em tensao nominal']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_tipo_agente = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[1]/div/div/div[6]/div[3]/div/div[1]/span')
                fd_tipo_agente.click()
                time.sleep(2)
                fd_tipo_agente_resp = self.driver.find_element_by_xpath(r"//li[text()='" + tipo_agente + "']")
                fd_tipo_agente_resp.click()
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em tipo de agente']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_ft = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[1]/div/div/div[7]/div[1]/div/div[1]/span')
                fd_ft.click()
                time.sleep(2)
                fd_ft_resp = self.driver.find_element_by_xpath(r"//li[text()='" + funcao_transmissao + "']")
                fd_ft_resp.click()
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em FT']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                if funcao_transmissao == 'OUTRA FUNÇÃO':
                    time.sleep(1)
                    fd_outra_funcao = self.driver.find_element_by_xpath(
                        '/html/body/div[3]/div[2]/form/div/div/div[2]/div[1]/div/div/div[7]/div[2]/input')
                    fd_outra_funcao.send_keys(outra_funcao)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em outra funcao']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_origem_indicacao = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/input')
                fd_origem_indicacao.send_keys(origem_indicacao)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em origem indicacao']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_prazo = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/span')
                fd_prazo.click()
                time.sleep(2)
                fd_prazo_resp = self.driver.find_element_by_xpath(r"//li[text()='" + prazo + "']")
                fd_prazo_resp.click()
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em prazo']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            fd_revitalizacao = self.driver.find_element_by_xpath(
                '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/textarea')
            fd_revitalizacao.send_keys(revitalizacao_necessaria)

            fd_justificativa = self.driver.find_element_by_xpath(
                '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/textarea')
            fd_justificativa.send_keys(justificativa)

            try:
                fd_tipo_revitalizacao = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[1]/div[5]/div[2]/div/div[1]/span')
                fd_tipo_revitalizacao.click()
                time.sleep(2)
                fd_tipo_revitalizacao_resp = self.driver.find_element_by_xpath(r"//li[text()='" + tipo_revitalizacao + "']")
                fd_tipo_revitalizacao_resp.click()
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em tipo de revitalizacao']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_motivacao = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[1]/div[5]/div[3]/div/div[1]/span')
                fd_motivacao.click()
                time.sleep(2)
                fd_motivacao_resp = self.driver.find_element_by_xpath(r"//li[text()='" + motivacao + "']")
                fd_motivacao_resp.click()
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em motivacao']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            fd_observacao = self.driver.find_element_by_xpath(
                '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[1]/div[7]/div/textarea')
            fd_observacao.send_keys(observacao)

            try:
                fd_dt_necessidade = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[1]/div[8]/div[1]/input')
                fd_dt_necessidade.click()
                for i in range(10):
                    fd_dt_necessidade.send_keys(Keys.BACKSPACE)
                time.sleep(0.1)
                fd_dt_necessidade.send_keys(data_necessidade_sistemica)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em data necessidade']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_projeto_originario = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[1]/div[8]/div[2]/div/div[1]/span')
                fd_projeto_originario.click()
                time.sleep(2)
                fd_projeto_originario_resp = self.driver.find_element_by_xpath(
                    r"//li[text()='" + projeto_originou_indicacao + "']")
                fd_projeto_originario_resp.click()
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em projeto que originou indicacao']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_custo_estimado = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[1]/div[8]/div[3]/input')
                for digito in custo_estimado:
                    fd_custo_estimado.send_keys(Keys.END, digito)
                    time.sleep(0.1)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em custo estimado']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            # ABA INFORMACOES DOS EQUIPAMENTOS
            self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/ul/li[2]/a').click()

            try:
                fd_valor_nm_cr = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/input')
                for digito in valor_nm_cris_cc:
                    fd_valor_nm_cr.send_keys(Keys.END, digito)
                    time.sleep(0.1)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em valor nm cris cc']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_qtd = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[3]/input')
                fd_qtd.send_keys(quantidade)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em quantidade']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_cd_id = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[4]/input')
                fd_cd_id.send_keys(cod_ident)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em cod ident']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_fabric = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/textarea')
                fd_fabric.send_keys(fabricante)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em fabricante']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_modelo = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div[1]/input')
                fd_modelo.send_keys(modelo)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em modelo']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_num_serie = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div[2]/input')
                fd_num_serie.send_keys(num_serie)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em numero serie']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_ano_inicio = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div[1]/input')
                fd_ano_inicio.send_keys(ano_inicio_oper)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em ano inicio']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_tx_deprec = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div[2]/input')
                for digito in taxa_deprec:
                    fd_tx_deprec.send_keys(Keys.END, digito)
                    time.sleep(0.1)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em taxa deprec']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_ano_fim = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div[3]/input')
                fd_ano_fim.send_keys(ano_fim_vida)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em ano fim vida']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_cap_nm_cc = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[2]/div[5]/div[1]/input')
                for digito in capacidade_nom_cc:
                    fd_cap_nm_cc.send_keys(Keys.END, digito)
                    time.sleep(0.1)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em capacidade nominal cc']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_cap_nm_cor = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[2]/div[5]/div[2]/input')
                for digito in capacidade_nom_corr:
                    fd_cap_nm_cor.send_keys(Keys.END, digito)
                    time.sleep(0.1)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em capacidade nominal corrente']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            # ABA ESPECIFICACOES NOVO EQUIPAMENTO
            self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/ul/li[4]/a').click()

            try:
                fd_cap_nm_cc_novo = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[4]/div[1]/div[2]/input')
                for digito in capacidade_nom_cc_novo:
                    fd_cap_nm_cc_novo.send_keys(Keys.END, digito)
                    time.sleep(0.1)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em capacidade nom cc (*)']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            try:
                fd_cap_nm_cor_novo = self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/form/div/div/div[2]/div[2]/div/div/div[4]/div[1]/div[4]/input')
                for digito in capacidade_nom_corr_novo:
                    fd_cap_nm_cor_novo.send_keys(Keys.END, digito)
                    time.sleep(0.1)
            except:
                print(f'ERRO EM {seq}')
                temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
                temp['SGPMR_CODIGOS'] = ['Erro em capacidade nom corrente (**)']
                df_dados_2 = df_dados_2.append(temp)
                df_dados_2.to_csv(resultado_arquivo, index=False)
                continue

            # ENVIAR
            self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div/div/div[3]/div/button[3]').click()

            self.aguardar_toast()
            toast = self.driver.find_element_by_id('toast-container')

            time.sleep(2)
            temp = pd.DataFrame(columns=df_dados.columns, data=[dados])
            temp['SGPMR_CODIGOS'] = [toast.text]
            df_dados_2 = df_dados_2.append(temp)
            df_dados_2.to_csv(resultado_arquivo, index=False)
