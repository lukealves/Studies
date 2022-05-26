
class Conta:
   #Função Construtora: recebe como argumento os valores dos atributos da classe.
   #Isto é, numero, titular, saldo e limite
    def __init__(self, numero, titular, saldo, limite):
        print ("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #metodos

    #Metodo Extrato: recebe como argumento uma referência do próprio objeto
    #Imprime o saldo da conta
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    #Metodo Deposita: Recebe como argumento uma referência do próprio objeto e o valor
    #Adicionará o valor ao saldo da conta.
    def deposita(self, valor):
        self.__saldo += valor

    #Metodo Saca: Recebe como argumento uma referência do próprio objeto e o valor.
    #Subtrairá o valor do saldo da conta.
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if  (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    #Propriedades
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}