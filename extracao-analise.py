import pandas as pd

#Trazer base de dados para o Python e verificar o que tem nela
tabela = pd.read_excel('Base de Dados.xlsx')
print(tabela)
#Pegar um panorama geral sobre a base de dados
faturamento_total = tabela['Valor Total'].sum()
print(faturamento_total)
#Começar análise Top -> Down - faturamento por produto
faturamento_por_tipo_de_cliente = tabela[['Tipos de Clientes', 'Valor Total']].groupby('Tipos de Clientes').sum()
print(faturamento_por_tipo_de_cliente)
#Entrando em detalhes
faturamento_por_produto = tabela[['Tipos de Clientes', 'Produto', 'Valor Total']].groupby(['Tipos de Clientes', 'Produto']).sum()
print(faturamento_por_produto)



