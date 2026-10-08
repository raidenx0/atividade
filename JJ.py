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
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor de saque deve ser maior que zero!")
        elif valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def transferir(self, conta_destino, valor):
        if valor <=0:
            print("O valor da transferencia deve ser maior que zero!")
        elif valor > self.saldo:
            print("Saldo insulficiente pra realizar transferencia!")
        else:
            self.saldo -= valor
            conta_destino.saldo += valor

            print(f"Transferencia de R$ {valor:.2f} realizada com sucesso!")
            print(f"De {self.titular}")
            print(f"Para: {conta_destino.titular}")

    def consultar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Numero da conta: {self.numero}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        
conta1 = ContaBancaria("Junin", "3321")
conta2 = ContaBancaria("Astrofonildo", "7764")

conta1.depositar(250)
conta1.transferir(conta2, 50)

print("\n--- CONTA 1 ---")
conta1.consultar_saldo()

print("\n--- CONTA 2 ---")
conta2.consultar_saldo()
