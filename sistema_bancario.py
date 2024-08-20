#Sistema Bancario
#criando menu
menu ="""
(1) Depositar
(2) Sacar
(3) Extrato
(4) Sair
=>"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

#criando a logica 
while True:
    opcao = input (menu)
    if opcao == "1":
        valor = float(input("Informe o valor do deposito: "))
        if valor > 0 :
            saldo += valor 
            extrato += f" deposito : R$ { valor :.2f}\n"
        else :
            print (" Operação Falhou! Valor informado é invalido.")
    elif opcao == "2" :
                valor = float (input ( "informe o valor do saque: "))
                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
                excedeu_saques = numero_saques >= limite_saques
                if excedeu_saldo :
                    print ("Operação falhou! Voce não tem saldo sulficiente.")
                elif excedeu_limite :
                    print ("Operção falhou! o valor do saque excede o limite.")
                elif excedeu_saques :
                    print ("Operção falhou! Numero de saques excedidos.")
                elif valor > 0 :
                    saldo -= valor
                    extrato += f"saque: R$ {valor :.2f}\n"
                    numero_saques += 1
                else :
                    print ("Operação falhou! O valor informado é invalido.")
    elif opcao == "3":
        print ("\n ===============EXTRATO=================")
        print ("Não foram realizadas movimentações." if not extrato else extrato)
        print (f"\n Saldo : R$ {saldo :.2f}")
        print ("===================FIM=====================")
    elif opcao == "4":
        break
    else:
        print ("operação invalida! Por favor selecione novamente de 1 a 4")                                 
