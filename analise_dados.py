import pandas as pd
import plotly.express as px

# importandno biblioteca de análise gráfica para melhor visualização

comando_leitura = pd.read_csv('telecom_users.csv') 
# não precisamos do caminho do arquivo uma vez que, o csv encontra-se na mesma pasta do código.

comando_leitura = comando_leitura.drop(['Unnamed: 0'], axis=1)
# axis significa eixo, axis 0 = apaga a linha indicada e axis = 1 a coluna
# OBS: base original do csv não é afetada.

print(comando_leitura)

comando_leitura['TotalGasto'] = pd.to_numeric(comando_leitura['TotalGasto'], errors='coerce')
# transformando a coluna indicada apenas em números, e caso apareça algum erro, force a transformação

comando_leitura = comando_leitura.dropna(how='all', axis=1)
# com o dropna iremos excluir todas as colunas que possuírem só espaços vazios
comando_leitura = comando_leitura.dropna(how='any', axis=0)
# por padrão poderíamos apenas deixas os () vazios, magora iremos excluir qualquer linha que tiver algum espaço vazio

# analisaremos agora quantos clientes cancelaram o contrato com a empresa
print(comando_leitura['Churn'].value_counts()) # retorna valores em floats
print(comando_leitura['Churn'].value_counts(normalize=True).map('{:.1%}'.format)) # retorna percentuais

for coluna in comando_leitura:
    if coluna != 'costumerID':
        grafico = px.histogram(comando_leitura, x=coluna, color='Churn')
        grafico.show()
        print(comando_leitura.pivot_table(index='Churn', columns=coluna, aggfunc='count')['customerID'])
        # criando a tabela com os dados do gráfico