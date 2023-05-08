from Resposta import Resposta
class Participante:
    def __init__(self, nome, perfil):
        self.nome = nome
        self.perfil = perfil
        
    def responder_perguntas(self, perguntas):
        perfil = []
        for pergunta in perguntas:
            resposta = input(f'{pergunta:} ').upper()
            while resposta not in ["SIM", 'NÃO']:
                print("Resposta inválida. É SIM ou NÃO")
                resposta = input(f'{pergunta}: ').upper()
            perfil.append(Resposta(pergunta,resposta))
        self.perfil = perfil