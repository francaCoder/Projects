"""
Você foi escolhido para fazer uma urna que deve mostrar o resultado das eleições entre os candidatos A B C
contando o voto de cada um através de uma função, que recebe o argumento 'votos' representando uma lista que contém
todos os votos entre os candidatos

Conte o voto de cada candidato e retorne o candidato vencedor
"""


class Election:
    def __init__(self):
        self.candidates = [["A", 0], ["B", 0], ["C", 0]]
        self.votes = ["A", "B", "C", "B", "B", "B", "A", "C", "B", "C"]

    def count_votes(self):
        for vote in self.votes:
            if vote == "A":
                self.candidates[0][1] += 1
            if vote == "B":
                self.candidates[1][1] += 1
            if vote == "C":
                self.candidates[2][1] += 1

    def result(self):
        winner = max(self.candidates[0][1], self.candidates[1][1], self.candidates[2][1])
        for c in self.candidates:
            if c[1] == winner:
                print(f"The winner was candidate → '{c[0]}' with {c[1]} votes.")


election = Election()
election.count_votes()
election.result()




