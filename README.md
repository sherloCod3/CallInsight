# "CallCenter Insights Project" 

Este projeto visa realizar uma análise abrangente dos dados `automaticamente, aleatoriamente e infinitamente gerados via script` por um call center, utilizando uma abordagem eficiente com Python, MSSQL Server e Power BI. Por meio da integração dessas poderosas ferramentas, nosso objetivo é extrair insights valiosos das interações do call center, proporcionando uma compreensão aprofundada do desempenho, padrões de chamadas, e tendências significativas. 

## :bar_chart: <samp>Dados Utilizados:</samp>
Os dados utilizados, como informado anteriormente, são gerados a partir de um script em Python. São dados fictícios e inseridos nas tabelas do MSSQL Server para que, automaticamente e dinamicamente, a cada 1 segundo, sejam inseridos simualações de atendimentos nas tabelas do SQL Server, alimentando o dashboard do Power BI.

## :technologist:‎ <samp>Tecnologias Utilizadas:</samp>

- <b>Python:</b> Implementação de scripts para manipulação e processamento avançado dos dados.
- <b>MSSQL Server:</b> Armazenamento seguro e eficiente de grandes conjuntos de dados provenientes das chamadas.
- <b>Power BI:</b> Visualização interativa e dinâmica dos resultados, permitindo a fácil interpretação e tomada de decisões estratégicas.

## :page_facing_up: <samp>Instruções:</samp>
Eu criei um banco de dados com uma simulação gerada de atendimentos, caso deseje iniciar do zero, deverá executar os seguintes procedimentos:
- alterar no script "temp.py" o nome da instância/servidor que utiliza em seu banco de dados:
  `'Server=DESKTOP-14UFHVO\SQLEXPRESS;'` - alterando "DESKTOP-14UFHVO\SQLEXPRESS", pelo nome do servidor correto;
- alterar o Driver se utilizar outro gerenciador de SQL, e caso necessário, as devidas alterações;
- para facilitar, restaure o banco de dados que forneci, execute `DELETE from chamadas` para zerar as informações geradas;
- se desejar pode inserir novos dados (IDs, nomes de empresa, locais, atendentes, etc) nas tabelas do banco de dados;
- conectar seu Power BI com o servidor e Banco de Dados do Call Center para que possa atualizar;
- a atualização do Power BI está a cada 1 segundo, assim como a inserção de novos dados pelo script em Python (time.sleep(1))
  se desejar, pode alterar para qualquer outro período que desejar.

## :dart:‎ <samp>Objetivos do Projeto:</samp>

- Identificar padrões de chamadas e comportamentos do cliente para otimizar a eficiência operacional.
- Avaliar o desempenho dos operadores e identificar oportunidades de treinamento.
- Criar dashboards personalizados no Power BI para fornecer informações em tempo real aos gestores e tomadores de decisão.
- Implementar automação em Python para agilizar a coleta, processamento e análise contínua dos dados do call center.
- Este projeto não apenas oferecerá uma análise aprofundada, mas também proporcionará uma base sólida para a implementação de estratégias proativas, impulsionando a eficiência e a qualidade nas operações do call center.

## :desktop_computer:‎ <samp>Screenshot:</samp>
|![Screenshot 2024-01-18 145803](https://github.com/sherloCod3/CallInsight/assets/107740398/c9f9e0eb-b2ce-4ef5-b238-458b758195e4)|
|---|
|![Screenshot 2024-01-18 150440](https://github.com/sherloCod3/CallInsight/assets/107740398/50d601bb-5d65-466f-85fc-80ae2cff9bb3)|
|---|

