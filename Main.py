from Participante import Participante
from Resposta import Resposta

class Festa:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.participantes = []

    def add_participante(self, participante):
        self.participantes.append(participante)

    def encontrar_match(self, participante):
        matches = {}
        for outro_participante in self.participantes:
            if outro_participante == participante:
                continue
            num_respostas_iguais = 0
            for resposta_participante in participante.perfil:
                for resposta_outro_participante in outro_participante.perfil:
                    if resposta_participante.pergunta == resposta_outro_participante.pergunta and resposta_participante.resposta == resposta_outro_participante.resposta:
                        num_respostas_iguais += 1
            matches[outro_participante] = num_respostas_iguais

        max_match = max(matches.values())
        matches = {participante: respostas for participante, respostas in matches.items() if respostas == max_match}
        return matches

    def exibir_match(self, matches):
        if not matches:
            print("Não foi dessa vez chefe")
        else:
            print("Match(es):")
            for match in matches.keys():
                print(match.nome)
        
def add_pergunta(perguntas):
    pergunta = input("Digite a pergunta que deseja adicionar: ")
    perguntas.append(pergunta)

def add_participante(festa, perguntas):
    nome = input("Digite o nome do participante: ")
    participante = Participante(nome, [])
    participante.responder_perguntas(perguntas)
    festa.add_participante(participante)

def encontrar_match(festa, perguntas):
    nome_participante = input("Digite o nome do participante para encontrar um match: ")
    participante = None
    for p in festa.participantes:
        if p.nome == nome_participante:
            participante = p
            break
    if participante is None:
        print(f"Participante '{nome_participante}' não encontrado.")
        return
    matches = festa.encontrar_match(participante)
    festa.exibir_match(matches)

def menu():
    perguntas = []
    festa = Festa("Festa", "Descrição da festa")

    while True:
        print("Escolha uma opção:")
        print("1. Adicionar pergunta")
        print("2. Adicionar participante")
        print("3. Encontrar match")
        opcao = input("Digite a opção desejada (ou '4' para sair): ")
        if opcao == "1":
            add_pergunta(perguntas)
        elif opcao == "2":
            add_participante(festa, perguntas)
        elif opcao == "3":
            encontrar_match(festa, perguntas)
        elif opcao == "4":
            break
        else:
            print("Opção inválida")

menu()