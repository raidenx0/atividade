class paciente:
    def __init__(self, nome, idade, numero):
        self.nome = nome
        self.idade = idade
        self.numero = numero

    def consultar_dados(self):
        print(f"paciente: {self.nome}, idade: {self.idade}")

junin = paciente("junin", 30,1)
gilberto = paciente("gilberto", 12, 2)
cabron = paciente("cabron", 76, 3)

class medico:
    def __init__(self, nome, especialização, id, horarios):
        self.nome = nome
        self.especialização = especialização
        self.id = id
        self.horarios = horarios
        self.disponivel = bool
    

    def consultar_medico(self):
        print(f"medico: {self.nome}, especialização: {self.especialização}, horarios: {self.horarios}")

astrofonildo = medico("astrofonildo", "dentista", 1, 14)

class consulta:
    def __init__(self, paciente, medico, horario):
        self.paciente = paciente
        self.medico = medico
        self.horario = horario
    
    
    
junin.consultar_dados()
gilberto.consultar_dados()
cabron.consultar_dados()

astrofonildo.consultar_medico()