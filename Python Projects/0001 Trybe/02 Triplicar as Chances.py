"""
Uma função chamada 'Triple_chances' que recebe uma lista de chances como argumento e mostra cada chance (a partir da segunda chance) multiplicada por 3
"""


chances = [2, 3, 5, 8, 10]

def triple_chances(chances):
    for chance in chances[1:]:
        print(chance*3)


triple_chances(chances)