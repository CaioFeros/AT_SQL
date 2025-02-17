import sqlite3
import pandas as pd

# Crie uma conexão com o banco de dados ou crie um novo
conn = sqlite3.connect('banco_de_dados.db')

# Carregue o arquivo CSV em um DataFrame pandas
df = pd.read_csv('dados.csv')

# Use o método `to_sql` do DataFrame para inserir os dados no banco de dados
df.to_sql('venda', conn, if_exists='replace', index=False)

# Execute as consultas SQL
cursor = conn.cursor()


                           # ETAPA 1

# 01 - A partir dos dados carregados na estrutura do item 09, apresente o conteúdo das duas variáveis indicadas.

cursor.execute("SELECT yrsold, MSzoning FROM venda LIMIT 10;")
resultado = cursor.fetchall()
print("Consulta 1: Consulta das duas variaveis:")
for i in resultado:
  
    print(i)
print()

# 02 - A partir dos dados carregados na estrutura do item 09, apresente o conteúdo das duas variáveis indicadas.

cursor.execute("SELECT MSzoning, COUNT(*) FROM venda GROUP BY MSZONING;")
result = cursor.fetchall()
print("Consulta 2: Consulta contador categorica:")
for i in result:
  
    print(i)
print()

# 03 - A partir dos dados carregados na estrutura do item 09, apresente os valores máximo, mínimo e a média dos valores da variável numérica escolhida.

cursor.execute("SELECT MIN(yrsold) AS ano_minimo, AVG(yrsold) AS ano_medio FROM venda;")
result = cursor.fetchone()
print("Consulta 3: Ano minimo e maximo:")
print("Ano Mínimo:", result[0])
print("Ano Médio:", round(result[1]))
print()


# 04 - A partir da tabela criada no item 01, elimine os dados que pertencem à categoria mais representativa da base, em quantidade de elementos.


cursor.execute("DELETE FROM venda WHERE yrsold = (SELECT yrsold FROM venda GROUP BY yrsold ORDER BY COUNT(yrsold) DESC LIMIT 1);")
cursor.connection.commit()
print("Ano mais presente deletado")
print()


# ETAPA 2 - LOCKER STUDIO

# ETAPA 3

# 10 - A partir dos dados carregados na estrutura do item 09, apresente o conteúdo das duas variáveis indicadas.

cursor.execute("SELECT yrsold, MSZoning FROM venda limit 10;") 
result = cursor.fetchall()
print("Consulta 1: Lista das duas variaveis:")
lista_dados = []
for i in result:
  lista_dados.append(i)
print(lista_dados)
print()

# 11 - A partir dos dados carregados na estrutura do item 09, apresente os valores máximo, mínimo e a média dos valores da variável numérica escolhida.

cursor.execute("SELECT MIN(yrsold) AS ano_minimo, AVG(yrsold) AS ano_medio, MAX(yrsold) AS ano_Maximo FROM venda;")
result = cursor.fetchone()
print("Consulta 2: Ano minimo e maximo:")
print("Ano Mínimo:", result[0])
print("Ano Médio:", round(result[1]))
print("Ano Maximo:", result[2])
print()

# 12 - A partir dos dados carregados na estrutura do item 09, apresente uma listagem de itens únicos da variável categórica escolhida.

cursor.execute("SELECT DISTINCT MSZoning FROM venda;")
result = cursor.fetchall()
lista_distintos = []
print("Consulta 3: Listagem de itens unicos de MS Zoning:")
for i in result:
  lista_distintos.append(i)
print(lista_distintos)
print()

 # ETAPA 4

# 13 - A partir dos dados carregados na estrutura do item 09, crie uma lista contendo apenas os dados da variável numérica.

cursor.execute("SELECT yrsold FROM venda limit 10;") 
result = cursor.fetchall()
print("Consulta 4: Lista da variavel numerica:")
lista_dados_num = []
for i in result:
  lista_dados_num.append(i)
print(lista_dados_num)
print()

# 14 - A partir dos dados carregados na estrutura do item 09, crie uma nova lista, agora contendo apenas os dados da variável categórica.

cursor.execute("SELECT MSZoning FROM venda limit 10;") 
result = cursor.fetchall()
print("Consulta 5: Lista da variavel categorica:")
lista_dados_cate = []
for i in result:
  lista_dados_cate.append(i)
print(lista_dados_cate)
print()

# 15 - A partir da lista dos dados da variável numérica do item 13, crie uma estrutura de repetição que apresente na tela a soma dos valores acima da média dos valores da própria variável.

cursor.execute("SELECT AVG(yrsold) AS ano_medio FROM venda;")
ano_medio = cursor.fetchone()
ano_medio = ano_medio[0]  # Pegue o valor médio do resultado da consulta
print("Consulta 6: Soma maior que o Ano medio:")
print("Ano Médio:", ano_medio)
cursor.execute("SELECT yrsold FROM venda;")
yrsold_total = cursor.fetchall()
soma_yrsold = 0
li_yrsold_sum = []
for i in yrsold_total:
    if i[0] > ano_medio:  # Compare cada valor de yrsold individualmente com ano_medio
        soma_yrsold += i[0]  # Adicione o valor a soma_yrsold
print("Soma de yrsold maior que o Ano Médio:", soma_yrsold)
print()

# 16 - A partir da lista dos dados da variável categórica do item 14, crie uma função que, ao ser aplicada na lista (a lista deve ser passada para a função), retorne a contagem de ocorrência dos itens individuais da variável categórica escolhida.

print("Consulta 7: Contagem de ocorrencia de cada item")
def contar_ocorrencias(lista):
    contagem = {}
    
    for item in lista:
        if item in contagem:
            contagem[item] += 1
        else:
            contagem[item] = 1
    
    return contagem

resultado = contar_ocorrencias(lista_dados_cate)
for item, ocorrencias in resultado.items():
    print(f"{item}: {ocorrencias} vezes")


# Feche a conexão com o banco de dados quando terminar
conn.close()
