from fpdf import FPDF
import pandas as pd 
from datetime import datetime


adress_csv_cockpit = r'//...$/Gerenciador de Alarme/cockpit.xlsx'
adress_csv_sap = r'//...$/Gerenciador de Alarme/Resumo Nota-Alarme.csv'
adress_txt_conf_sap = r'//...$/Gerenciador de Alarme/conf.txt'
UPLOAD_FOLDER = './static/img/RelatorioCGA'
dic_link = {}
width_page = 190
df_SAP = {}
df=''

class PDF(FPDF):
    def header(self):
        # Logo
        logo = r'./funcoes/files/logo.png'
        self.image(logo, 10, 8, 40,link=pdf.add_link(page=1))
        
        # Title
        self.set_font('Arial', 'b', 16)
        self.cell(0, 10, 'Relatorio CGA', ln=1, align='C')
        
        # SubTitle
        self.set_font('Arial', '', 8)
        self.set_text_color(153, 153, 102)
        self.cell(0, 4, '03/07/2023 16:16:03', ln=1, align='C')
        pdf.ln(3)
        
    def footer(self):
        # Set possition of the footer
        self.set_y(-15)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 5, f'Page {self.page_no()}/{{nb}}', align='C')
        self.image(r'./funcoes/files/icon/Arrow Up.png', w=5, h=5, link=pdf.add_link(page=1))
        
    def sumario(self):
        ######################################## Criar Sumario
            #Title Sumario
        self.set_text_color(0, 0, 0)
        self.set_font('arial', 'b', 12)
        self.cell(0, 10, 'Sumario', align='C', ln=True) 
        self.ln(3)

        #Criar Sumario
        for unidade, df_unidade in df.groupby('Unidade'):
            # Title Unidade
            self.set_font('Arial', 'b', 12)
            self.set_text_color(0, 0, 0)
            x, y= self.get_x(), self.get_y()
            self.cell(0, 8, unidade, ln=1, border='L') 
            self.set_xy(x=x,y=y)
            self.cell(0, 8, '', ln=1, border='T') 
            
            for especialidade, df_especialidade in df_unidade.groupby('Especialidade'):
                # Title Especialidade
                self.set_font('Arial', 'b', 10)
                self.set_text_color(0, 0, 0)
                x, y= self.get_x(), self.get_y()
                self.cell(0, 8, " "*7+especialidade, ln=1, border='L')


                # Valores Tags
                for i, line in df_especialidade.iterrows():
                    # configuraçãoes  icone Status
                    self.set_font('couriernew', '', 8) # Formatação do Texto
                    dic_link[line['TAG']] = self.add_link() # Definir Link
                    adress_icon = f"./funcoes/files/icon/{line['Status']}_{line['Criticidade'][-1]}.png" # Definir Icone

                    # configuraçãoes  icone Status_SAP
                    if line['Conclusão Desej.'] == '-':
                        adress_icone_SAP = "./funcoes/files/icon/NaoAssociado.png"
                        texto_SAP = 'Sem Nota SAP'
                    else:
                        if datetime.now() > pd.to_datetime(line['Conclusão Desej.'], format='%d/%m/%Y'):
                            adress_icone_SAP = "./funcoes/files/icon/EmAtraso.png"
                            texto_SAP = 'Nota em Atraso'
                        else:
                            adress_icone_SAP = "./funcoes/files/icon/EmDia.png"
                            texto_SAP = 'Nota em Dia'



                    # Escrever dados
                    self.cell(width_page/4, 5, " "*7+line['TAG'], link= dic_link[line['TAG']], border='L')
                    self.cell(width_page/4, 5, " "*7+line['Data Atualização'], link= dic_link[line['TAG']], align='L')

                    self.set_x(x=self.get_x()+5) 
                    x, y= self.get_x()+6, self.get_y()
                    self.image(adress_icone_SAP, w=4 ,h=4, link=dic_link[line['TAG']])
                    self.set_xy(x=x,y=y)
                    self.cell(30, 5, texto_SAP, link=dic_link[line['TAG']])
                    

                    x, y= self.get_x()+6, self.get_y()
                    self.image(adress_icon, w=4 ,h=4, link=dic_link[line['TAG']])
                    self.set_xy(x=x,y=y)
                    self.cell(30, 5, line['Status'],ln=1, link=dic_link[line['TAG']])


                # Criar Sumario da Tabela SAP
                ID_Name = 'SAP-'+unidade+'-'+especialidade 
                dic_link[ID_Name] = self.add_link() # Definir Link

                # Filtrar df por Unidade e especialidade e definir quantas vencidas e quantas em dia.
                df_filtered = df_SAP[(df_SAP['Unidade']==unidade) & (df_SAP['Especialidade']==especialidade)] 
                Dic_Vencidas = df_filtered.groupby(['Vencida'])['Vencida'].count().to_dict()
                
                # Tratar erro caso nao tenha Alguma das Keys e ja escrever textos 
                Dic_Vencidas['Sim'] = 0 if not 'Sim' in Dic_Vencidas else Dic_Vencidas['Sim']
                Dic_Vencidas['Nao'] = 0 if not 'Nao' in Dic_Vencidas else Dic_Vencidas['Nao']

                text_2 = 'Notas Abertas:'+str(Dic_Vencidas['Nao']+Dic_Vencidas['Sim'])
                text_3 = 'Notas Em Dia:'+str(Dic_Vencidas['Nao'])
                text_4 = 'Notas Vencidas:'+str(Dic_Vencidas['Sim'])
                
                # Escrever No pdf
                self.cell(width_page/4, 5, " "*7+'Notas SAP', link= dic_link[ID_Name], border='L')
                self.cell(width_page/4, 5, " "*7+text_2 , link= dic_link[ID_Name], align='L')

                self.set_xy(x=self.get_x()+5+6, y=self.get_y())
                self.cell(30, 5, text_3 , link= dic_link[ID_Name])
                
                self.set_xy(x=self.get_x()+6, y=self.get_y())
                self.cell(30, 5, text_4,ln=1, link=dic_link[ID_Name])
                

            self.ln(3)
            
                
        self.add_page()

    def conteudo(self):
        ######################################## Criar Body
        # Definir parametros table
        cols = ['TAG','Especialidade','Criticidade','Status','Nota SAP','Conclusão Desej.','Data Atualização']
        w = width_page/len(cols)
        h = 7
        dic_dimension = {
            'TAG': 30,
            'Especialidade': 24,
            'Criticidade': 20,
            'Status': 35,
            'Nota SAP': 27,
            'Conclusão Desej.': 27,
            'Data Atualização': 27
        }



        for i, line in df.iterrows():
            # Setar Link
            self.set_link(dic_link[line['TAG']],y=self.get_y(), x=self.get_x())    
            
            # Formatação head Table
            self.set_font('Arial', 'b', 8)
            self.set_fill_color(217, 217, 217)
            
            
            for col in cols:
                # Criando head Table
                self.cell(dic_dimension[col], h, col, fill=True, border=1, align='C')
            self.ln(h)

            # Formatação body Table
            self.set_font('Arial', '', 8)
            self.set_fill_color(255, 255, 255)
            for col in cols:
                # Criando body Table
                self.cell(dic_dimension[col], h, line[col], fill=True, border=1, align='C')
            self.ln(h)
            
            # Formatação head Table comentario
            self.set_font('Arial', 'b', 8)
            self.set_fill_color(217, 217, 217)
            self.cell(0, h, 'Comentario', fill=True, border=1, align='C')
            self.ln(h)
            
            # Formatação body Table comentario
            self.set_font('Arial', '', 8)
            self.set_fill_color(255, 255, 255)
            self.multi_cell(0, h, line['Comentario'].encode('latin-1', 'replace').decode('latin-1').replace('&',';  '), fill=True, border=1, align='C')
            self.ln(h*2) 


    def table(self):
            self.add_page()

            # Definir parametros table
            list_Col_SAP = ['Nota','TAG SAP','Descricao Curta','Conclusao Desejada','Vencida','Status CGA']
            w = width_page/len(list_Col_SAP)
            h = 5
            dic_dimension_SAP = {
                'Nota': 20,
                'TAG SAP': 37.5,
                'Descricao Curta': 62.5,
                'Conclusao Desejada': 20,
                'Vencida': 15,
                'Status CGA': 35,
            }
            dic_col_SAP = {
                'Nota': 'Nota',
                'TAG SAP': 'TAG',
                'Descricao Curta': 'Descricao Curta',
                'Conclusao Desejada': 'Concl. Desej.',
                'Vencida': 'Vencida',
                'Status CGA': 'Status CGA'
            }
            
            # Titulo da Tabela
            self.set_font('Arial', 'b', 12)
            self.set_text_color(0, 0, 0)
            self.cell(width_page, h, 'Tabela SAP - RCP', align='C') 
            self.ln(h)
                        
            #Divisões das Tabelas
            for unidade, df_unidade in df_SAP.groupby('Unidade'):                
                # Escrever Unidade - Especialidade
                for especialidade, df_especialidade in df_unidade.groupby('Especialidade'):
                    # Setar Link
                    ID_Name = 'SAP-'+unidade+'-'+especialidade 
                    self.set_link(dic_link[ID_Name],y=self.get_y(), x=self.get_x()) 

                    # Formatar e Escrever Unidade e especialidade
                    self.set_font('Arial', 'b', 10)
                    self.set_text_color(0, 0, 0)
                    self.cell(0, h, unidade+' - '+especialidade)
                    self.ln(h*2)

                    # Formatar e Escrever Head da Tabela
                    self.set_font('Arial', 'b', 8)
                    self.set_fill_color(217, 217, 217)
                    for col in list_Col_SAP:   
                        self.cell(dic_dimension_SAP[col], h, dic_col_SAP[col], fill=True, border=1, align='C')
                    self.ln(h)
                    
                    # Formatar e Escrever Body da Tabela
                    self.set_font('Arial', '', 8)
                    self.set_fill_color(255, 255, 255)
                    for i, line in df_especialidade.iterrows():
                        for col in list_Col_SAP:
                            self.cell(dic_dimension_SAP[col], h, line[col], fill=True, border=1, align='C')
                        self.ln(h)

                    self.ln(h)
                    
            self.ln(h*3)               
                   
pdf = PDF('P', 'mm', 'A4') # Iniciar PDF
pdf.add_page() # Iniciar Pagina
pdf.alias_nb_pages() # Iniciar Contagem de pag P/ rodape

# Criar Suamario
pdf.sumario()

# Criar conteudo
pdf.conteudo() 

pdf.table()

# Salvar Arquivo
pdf.output(name='Relatorio CGA.pdf', dest = 'F')
    
#return  'Relatorio CGA.pdf'