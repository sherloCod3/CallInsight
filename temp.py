"""Gerador de eventos de Call Center

Este script gera automaticamente eventos de Call center com base 
nos parâmetros informados no código.

Ele alimentará o banco de dados para que os eventos possam ser analisados
dinamicamente em tempo real a partir do Power BI.

Foram utilizados IDE Pycharm, MSSQL Server, Google Docs (ou Excel),
e PowerBI.
"""

import datetime
import time
import random
import pyodbc

con = pyodbc.connect('Driver={SQL Server};'
                     'Server=DESKTOP-14UFHVO\SQLEXPRESS;'
                     'Database=Call_Center;'
                     'Trusted_Connection=yes;')

cursor = con.cursor()

while 1 == 1:
    data = datetime.date.today()
    id_local = random.randint(111, 201)
    id_empresa = random.randint(11, 30)
    id_assunto_cliente = random.randint(111, 130)
    id_atendente = random.randint(111, 210)
    tempo_resposta = random.randint(1, 300)
    duracao_chamada = random.randint(1, 600)
    status = random.randint(1, 100)
    if status < 75:
        status = 1
    elif status < 85:
        status = 2
    elif status < 90:
        status = 3
    else:
        status = 4
    if status == 1:
        avaliacao = random.randint(5, 10)
    elif status == 2:
        avaliacao = random.randint(3, 8)
    elif status == 3:
        avaliacao = random.randint(1, 3)
    elif status == 4:
        avaliacao = random.randint(1, 5)

    print(data)
    cursor.execute('insert into chamadas values(GETDATE(),'
                   + str(id_local) + ','
                   + str(id_empresa) + ','
                   + str(id_assunto_cliente) + ','
                   + str(id_atendente) + ','
                   + str(tempo_resposta) + ','
                   + str(duracao_chamada) + ','
                   + str(status) + ','
                   + str(avaliacao) + ')'
                   )
    cursor.commit()
    time.sleep(1)
