# 📊 Análise de Faturamento por Tipo de Cliente e Produto 💰

Este projeto realiza uma análise detalhada de faturamento com base em uma **planilha de vendas**. O objetivo é entender como o faturamento é distribuído entre diferentes tipos de clientes e produtos. 💼📈

## 🔍 Sobre o Projeto

Neste projeto, utilizamos dados extraídos de uma planilha **Excel** (`Base de Dados.xlsx`) para realizar as seguintes análises:

- **Faturamento Total**: Analisamos o faturamento total da base de dados.
- **Faturamento por Tipo de Cliente**: Verificamos como o faturamento se distribui entre os diferentes tipos de clientes.
- **Faturamento por Produto**: Detalhamos o faturamento por produto dentro de cada tipo de cliente.

## 🛠️ Tecnologias Utilizadas

- **Python** 🐍
  - **Pandas** 📊 para análise e manipulação dos dados
  - **Excel** 📑 para armazenamento dos dados

## 📂 Como Rodar o Projeto

1. **Clonar o repositório**:
   - Abra seu terminal e execute:
     ```
     git clone https://github.com/VictorJeremias/extracao-analise-dados.git
     ```

2. **Instalar as dependências**:
   - Crie um ambiente virtual:
     ```
     python -m venv env
     ```
   - Ative o ambiente virtual:
     - No Windows:
       ```
       .\env\Scripts\activate
       ```
     - No macOS/Linux:
       ```
       source env/bin/activate
       ```
   - Instale o **Pandas**:
     ```
     pip install pandas
     ```

3. **Colocar o arquivo Excel**:
   - Coloque o arquivo `Base de Dados.xlsx` no mesmo diretório onde o código Python está localizado.

4. **Rodar o código**:
   - Execute o código Python:
     ```
     extracao-analise.py
     ```

## 📊 Análises Realizadas

- **Faturamento Total**: Calculamos o total de faturamento a partir da coluna "Valor Total".
- **Faturamento por Tipo de Cliente**: Analisamos a soma do faturamento agrupado por "Tipos de Clientes".
- **Faturamento por Produto**: Detalhamos o faturamento por produto e tipo de cliente.

## 💡 Detalhamento do Código

1. **Carregamento dos Dados**: Utilizamos o **Pandas** para importar os dados de um arquivo **Excel**.
2. **Cálculo do Faturamento Total**: A soma de todas as vendas foi calculada para obter o faturamento total.
3. **Faturamento por Tipo de Cliente**: Agrupamos os dados por tipo de cliente e somamos os valores totais de faturamento.
4. **Faturamento por Produto**: Aprofundamos a análise, detalhando o faturamento por tipo de cliente e produto.


📊 Agora você pode analisar facilmente os dados de faturamento! 🚀
