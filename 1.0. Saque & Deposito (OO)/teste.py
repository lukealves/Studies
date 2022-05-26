
#Função "cria_conta": Recebe como argumento: numero, titular, saldo e limite.
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

#Função "deposita": Recebe como argumento a conta e o valor e adiciona o valor ao saldo da conta.
def deposita(conta, valor):
    conta["saldo"] += valor

#Função "saca": Recebe como argumento a conta e o valor e subtrai o valor do saldo da conta.
def saca(conta, valor):
    conta["saldo"] -= valor

#Função "extrato": recebe como argumento a conta e imprime o seu saldo.
def extrato(conta):
    print ("Saldo {}".format(conta["saldo"]))