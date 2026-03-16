class Conta: 
 
    def __init__(self, saldo): 
        self.__saldo = saldo 
 
    def sacar(self, valor): 
        if valor <= self.__saldo: 
            self.__saldo -= valor 

    def get_saldo(self):
        return self.__saldo
 
conta = Conta(1000) 
conta.sacar(20)
print(conta.get_saldo())  
