class ContaBancaria:
    def __init__(self, titular, numero):
        self.titular = titular
        self.numero = numero
        self.saldo = 0
    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser maior que zero!")
        else:
            self.saldo += valor
            print("Depósito de R$ {valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor de saque deve ser maior que zero!")
        elif valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    
    def consultar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Numero da conta: {self.numero}")
        print(f"Saldo: R$ {self.saldo:.2f}")
conta = ContaBancaria("Junin", "3321")
conta.depositar(1)
conta.sacar(450)
conta.consultar_saldo()