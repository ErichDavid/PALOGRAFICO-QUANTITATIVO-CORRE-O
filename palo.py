from time import sleep
import sys
while True:

    print("APLICAÇÃO TESTE PARA CORREÇÃO DO PALOGRAFICO")
    print(".")
    print("Carregando...")
    sleep(2)
    print(".")
    login = str(input("LOGIN:"))
    senha = int(input("SENHA:"))
    if login == "admin" and senha == 123:
       print("Acesso concedido!")
       break
    else:
       print("Senha ou Login invalidos tente novamente.")

print(".")
print("Carregando...")
sleep(3)
print(".")

while True:
    print("DIGITE A SOMA DE CADA SINAL:")
    print(".")

    sinal1 = int(input("PRIMERO SINAL:"))
    print(".")
    sinal2 = int(input("SEGUNDO SINAL:"))
    print(".")
    sinal3 = int(input("TERCEIRO SINAL:"))
    print(".")
    sinal4 = int(input("QUARTO SINAL:"))
    print(".")
    sinal5 = int(input("QUINTO SINAL:"))
    print(".")
    print("Carregando...")
    sleep(3)
    print(".")

    sub1 = abs(sinal1 - sinal2)
    sub2 = abs(sinal2 - sinal3)
    sub3 = abs(sinal3 - sinal4)
    sub4 = abs(sinal4 - sinal5)

    totalsoma = sinal1 + sinal2 + sinal3 + sinal4 + sinal5
    totalsub = sub1 + sub2 + sub3 + sub4
    op1 = totalsub * 100
    op2 = op1 / totalsoma

    print("SUBTRAÇÕES:")
    print("SUBTRAÇÃO 1º: {}".format(sub1))
    print("SUBTRAÇÃO 2º: {}".format(sub2))
    print("SUBTRAÇÃO 2º: {}".format(sub3))
    print("SUBTRAÇÃO 3º: {}".format(sub4))
    print(".")
    print("RESULTADO:")
    print(".")
    print("TOTAL DA SUBTRAÇÃO: {}".format(totalsub))
    print(".")
    print("PRODUTIVIDADE: {}".format(totalsoma)) 
    print(".")
    r = round(op2,2) 
    print("OSCILAÇÃO: {}".format(r))
    print(".")
    e = input("[1]-sair [2]-refazer:")
    if e == "1":
        break
    elif e == "2":
       print(".")
       print("Carregando...")
       print(".")
       sleep(2)
