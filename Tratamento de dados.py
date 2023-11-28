import pandas as pd 
import datetime 

df_SAP=''
df=''

df_SAP.loc[df_SAP['Centro de Trabalho'].str.startswith('RJ09'),'Unidade'] = 'PP5'
df_SAP.loc[df_SAP['Centro de Trabalho'].str.endswith('P'),'Unidade'] = 'PE9'
df_SAP['Unidade'].fillna('Q4', inplace=True) 

# Procv entre pranilhas DF receber Conclusao Desejada
df['Conclusao Desejada'] = pd.merge(
df,                     # Df left
df_SAP,                 # Df Right
how='left',             # keep o Df left 
left_on='nota_sap',     # key do df Left
right_on='Nota'         # key do df right 
)['Conclusao Desejada'].to_list()  #Get Coll, #form List to eliminate index
                
# Limpar dados        
df['Conclusao Desejada'] = df['Conclusao Desejada'].fillna('-')
df['Conclusao Desejada'] = df['Conclusao Desejada'].str.replace('.', '/', regex=True)

df_SAP.loc[df_SAP['Centro de Trabalho'].str.contains('SUME|SULU|SUCA'),'Especialidade'] = 'Mecânica'
df_SAP.loc[df_SAP['Centro de Trabalho'].str.contains('SUIN'),'Especialidade'] = 'Instrumentação'


# Criar Coluna Vencida
df_SAP['Vencida'] = ['Sim' if x < datetime.now() else 'Nao' for x in 
pd.to_datetime(df_SAP['Conclusao Desejada'], format='%d.%m.%Y')]