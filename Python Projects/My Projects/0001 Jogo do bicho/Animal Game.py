# Eu sei que tem vários erros de português, depois eu arrumo, estou só testando a lógica por enquanto :)
# Vários números na milhar com a mesma aposta

from pprint import pprint
from random import randint
from time import sleep

# Centena pode valer do 1 - 7
# Milhar - 1 - 6
def line(word):
    print(f"-=-=-=-= {word} =-=-=-=-")


line("Bem Vindo ao Jogo do Bicho")

# thousands = [[[randint(0, 9) for c in range(1, 5)] for c in range(6)]]
# thousands_result = {}
# for c in range(0, 6):
#     thousands_result[f'{c+1}º Thousand'] = f"{thousands[0][c][0]}{thousands[0][c][1]}{thousands[0][c][2]}{thousands[0][c][3]}"

thousands_result = {
    "1º Thousand": "9901",
    "2º Thousand": "3602",
    "3º Thousand": "1403",
    "4º Thousand": "1704",
    "5º Thousand": "9907",
    "6º Thousand": "9910",
}

bet = float(input("Quanto você quer apostar? R$"))

groups = [
    {"Index": 1, "Name": "Avestruz", "Numbers": ["01", "02", "03", "04"]},
    {"Index": 2, "Name": "Águia", "Numbers": ["05", "06", "07", "08"]},
    {"Index": 3, "Name": "Burro", "Numbers": ["09", "10", "11", "12"]},
    {"Index": 4, "Name": "Borboleta", "Numbers": ["13", "14", "15", "16"]},
    {"Index": 5, "Name": "Cachorro", "Numbers": ["17", "18", "19", "20"]},
    {"Index": 6, "Name": "Cabra", "Numbers": ["21", "22", "23", "24"]},
    {"Index": 7, "Name": "Carneiro", "Numbers": ["25", "26", "27", "28"]},
    {"Index": 8, "Name": "Camêlo", "Numbers": ["29", "38", "31", "32"]},
    {"Index": 9, "Name": "Cobra", "Numbers": ["33", "34", "35", "36"]},
    {"Index": 10, "Name": "Coelho", "Numbers": ["37", "38", "39", "40"]},
    {"Index": 11, "Name": "Cavalo", "Numbers": ["41", "42", "43", "44"]},
    {"Index": 12, "Name": "Elefante", "Numbers": ["45", "46", "47", "48"]},
    {"Index": 13, "Name": "Galo", "Numbers": ["49", "50", "51", "52"]},
    {"Index": 14, "Name": "Gato", "Numbers": ["53", "54", "55", "56"]},
    {"Index": 15, "Name": "Jacaré", "Numbers": ["57", "58", "59", "60"]},
    {"Index": 16, "Name": "Leão", "Numbers": ["61", "62", "63", "64"]},
    {"Index": 17, "Name": "Macaco", "Numbers": ["65", "66", "67", "68"]},
    {"Index": 18, "Name": "Porco", "Numbers": ["69", "70", "71", "72"]},
    {"Index": 19, "Name": "Pavão", "Numbers": ["73", "74", "75", "76"]},
    {"Index": 20, "Name": "Peru", "Numbers": ["77", "78", "79", "80"]},
    {"Index": 21, "Name": "Touro", "Numbers": ["81", "82", "83", "84"]},
    {"Index": 22, "Name": "Tigre", "Numbers": ["85", "86", "87", "88"]},
    {"Index": 23, "Name": "Urso", "Numbers": ["89", "90", "91", "92"]},
    {"Index": 24, "Name": "Veado", "Numbers": ["93", "94", "95", "96"]},
    {"Index": 25, "Name": "Vaca", "Numbers": ["97", "98", "99", "00"]},
]

print()
line("Opções de Jogo")
options = int(input("""[1] Aposta no Grupo
[2] Apostar na Dezena
[3] Apostar na Centena
[4] Apostar no Milhar
[5] Duque de Grupo
[6] Duque de Dezena
[7] Terno de Dezena
[8] Terno de Grupo
Número escolhido:
"""))
while options not in range(1, 9):
   options = int(input("Por favor, escolha um número entre 1 e 8 Representando as opções de jogos acima."
                       "\nNúmero escolhido: "))

print()
if options == 1:
    sleep(1)
    line(f"Regras")
    print(f"Apostando na 1º milhar, caso você ganhe, seu prêmio será de 18x sua aposta: R${int(bet*18)},00 \nApostando em todas Milhares, caso você ganhe, seu prêmio será de 3,6x sua aposta: R${int(bet*3.6)},00")
    print()
    choice = int(input("""Número [1] Para escolher o grupo por número: 
Número [2] Para escolher o grupo por nome: 
Escolha: """))
    while choice not in range(1, 4):
        print("Por favor, escolha um número que representa uma das opções abaixo.")
        choice = int(input("""Número [1] Para escolher o grupo por número: 
Número [2] Para escolher o grupo por nome: 
Escolha: """))

    if choice == 1:
        final_choice = []
        while True:
            group = int(input("Qual é o número do grupo? ").strip())
            while group not in range(1, 26):
                group = int(input("[ERROR] Escolha um número entre 1 e 25 representando o número de cada grupo."
                                  "\nQual é o número do grupo? "))
            want_continue = str(input(f"O grupo escolhido foi o do {groups[group-1]['Name']}, quer continuar? [Y/N] ")).strip().upper()[0]
            if want_continue == "Y":
                final_choice.append(groups[group-1])
                break
    elif choice == 2:
        final_choice = []
        verification = []
        for group in groups:
            verification.append(group['Name'].upper())
        while True:
            group = str(input("Qual é o nome do grupo? ")).strip().upper()
            while group not in verification:
                group = str(input("Qual é o nome do grupo? ")).strip().upper()
            want_continue = str(input(f"Grupo escolhido foi o {group.lower().capitalize()}, quer continuar? [Y/N] ")).strip().upper()[0]
            if want_continue == "Y":
                final_choice.append(groups[verification.index(group)])
                break

    decision = int(input("""Número [1] Para apostar somente na primeira milhar: 
Número [2] Para apostar nas 6 milhares: 
Escolha: """))
    while decision not in range(1, 4):
        print()
        print("Por favor, escolha um número que represente uma das opções abaixo.")
        decision = int(input("""Número [1] Para apostar na 1ª Milhar: 
Número [2] Para apostar nas 6 Milhares: 
Escolha: """))
# Falta o 3

    line("result")
    pprint(thousands_result)
    print()
    if decision == 1:
        for number in final_choice[0]['Numbers']:
            if number in thousands_result[f'1º Thousand'][2:]:
                print("DEU NA CABEÇA")
                print(f"1º Thousand: {thousands_result['1º Thousand']}")
                print(f"Seu prêmio foi de {int(bet*18)},00")
                break
            else:
                print("Você não acertou na  1º milhar")
                break
    elif decision == 2:
        dozens_drawn = []
        for number in thousands_result.values():
            dozens_drawn.append(number[2:])

        exist = False
        numbers_group = final_choice[0]['Numbers']
        for num in numbers_group:
            if num in dozens_drawn:
                exist = True
                qual_index = int(dozens_drawn.index(num) + 1)
                if qual_index == 1:
                    news = str(input("Eu tenho uma notícia boa e uma ruim pra você....\nQual você quer premeiro, Good or Bad? ")).strip().upper()[0]
                    while news not in "GB":
                        news = str(input("Please, choice: Good or Bad? ")).strip().upper()[0]
                    if news == "G":
                        print(f"Você ganhou sua aposta, e seu prêmio foi de R${int(bet*3.6)},00")
                        sleep(2)
                        print(f"Mas sua aposta tinha dado na cabeça...")
                        sleep(2)
                        print(f"Poderia ter ganhado R${int((bet*18) - (bet*3.6))},00 a mais se tivesse apostado somente na primeira, mesmo assim parabéns.")
                        break
                    else:
                        print(f"Você poderia ter ganhado R${int((bet*18) - (bet*3.6))},00 a mais se tivesse apostado somente na primeira milhar...")
                        sleep(2)
                        print(f"Mas mesmo assim parabéns, você ganhou {int(bet*3.6)},00")
                        break
                elif qual_index >= 2:
                    print(f"Parabéns! Você ganhou na {qual_index}º Milhar")
                    print(f"{qual_index}º Thousand: {thousands_result[f'{qual_index}º Thousand']}")
                    sleep(2.5)
                    print(f"Seu prêmio foi de R${int(bet*3.6)},00")
                    break
        if not exist:
            sleep(1)
            print("Checking...")
            sleep(2)
            print("Você não acertou nenhuma das dezenas ;( \nBoa sorte para a próxima vez...")

elif options == 2:
    sleep(1)
    line("Regras")
    print(f"Apostando na primeira milhar, caso você ganhe, seu prêmio será de 60x sua aposta: R${int(bet*60)},00 \nApostando da 1ª à 5ª Milhar, caso você ganhe, seu prêmio será de 12x sua aposta: R${int(bet*12)},00")
    print()
    verification = []
    final_choice = 0
    while True:
        ten = str(input("Escolha a dezena: "))
        verification.append(ten)
        if len(verification[0]) == 2:
            final_choice = ten
            break
        else:
            print("Por favor, escolha dois números entre 00 e 99 para formar a dezena.")
            verification.clear()

    print()
    decision = int(input("""Número [1] Para apostar na 1ª Milhar: 
Número [2] Para apostar nas 6 Milhares: 
Escolha: """))
    while decision not in range(1, 4):
        print()
        print("Por favor, escolha um número que represente uma das opções abaixo.")
        decision = int(input("""Número [1] Para apostar na 1ª Milhar: 
Número [2] Para apostar nas 6 Milhares: 
Escolha: """))

    line("result")
    pprint(thousands_result)
    print()
    if decision == 1:
        if final_choice == thousands_result['1º Thousand'][2:]:
            print("Deu na cabeça")
            print(f"1º Thousand: {thousands_result['1º Thousand']}")
            print(f"Seu prêmio foi de R${int(bet*60)},00")
        else:
            print("Você não acertou a dezena da 1º Milhar")
    elif decision == 2:
        dozen_drawn = []
        for number in thousands_result.values():
            dozen_drawn.append(number[2:])
        if final_choice in dozen_drawn:
            qual_index = int(dozen_drawn.index(final_choice) + 1)
            if qual_index == 1:
                news = str(input("Eu tenho uma notícia boa e uma ruim pra você....\nQual você quer premeiro, Good or Bad? ")).strip().upper()[0]
                while news not in "GB":
                    news = str(input("Please, choice: Good or Bad? ")).strip().upper()[0]
                if news == "G":
                    print(f"Você ganhou sua aposta, e seu prêmio foi de R${int(bet*12)},00")
                    sleep(2)
                    print(f"Mas sua aposta tinha dado na cabeça...")
                    sleep(2)
                    print(f"Poderia ter ganhado R${int((bet*60) - (bet*12))},00 a mais se tivesse apostado somente na primeira, mesmo assim parabéns.")
                else:
                    print(f"Você poderia ter ganhado R${int((bet*60) - (bet*12))},00 a mais se tivesse apostado somente na primeira milhar...")
                    sleep(2)
                    print(f"Mas mesmo assim parabéns, você ganhou R${int(bet*12)},00")
            elif qual_index >= 2:
                print(f"Parabéns! Você ganhou na {qual_index}º Milhar")
                print(f"{qual_index}º Thousand: {thousands_result[f'{qual_index}º Thousand']}")
                sleep(2.5)
                print(f"Seu prêmio foi de R${int(bet*12)},00")
        else:
            print("Você não acertou a dezena em nenhuma milhar")

elif options == 3:
    sleep(1)
    line("Regras")
    print(f"Apostando na primeira milhar, caso você ganhe, seu prêmio será de 600x sua aposta: R${int(bet*600)},00 \nApostando em todas Milhares, caso você ganhe, seu prêmio será de 120x sua aposta: R${int(bet*120)},00")
    print()
    verification = []
    final_choice = 0
    while True:
        hundreds = str(input("Escolha 3 números para a centena: "))
        verification.append(hundreds)
        if len(verification[0]) == 3:
            final_choice = hundreds
            break
        else:
            print("Por favor, escolha três números para formar a centena que você deseja apostar.")
            verification.clear()

    print()
    decision = int(input("""Número [1] Para apostar na 1ª Milhar:
Número [2] Para apostar em todas as Milhares: 
Escolha: """))
    while decision not in range(1, 4):
        print()
        print("Por favor, escolha um número que represente uma das opções abaixo.")
        decision = int(input("""Número [1] Para apostar na 1ª Milhar: 
Número [2] Para apostar em todas as Milhares: 
Escolha: """))
    print()

    line("result")
    pprint(thousands_result)
    print()
    if decision == 1:
        if final_choice == thousands_result['1º Thousand'][1:]:
            print("Deu na cabeça")
            print(f"1º Thousand: {thousands_result['1º Thousand']}")
            print(f"Seu prêmio foi de R${int(bet*600)},00")
        else:
            print("Você não acertou a dezena da 1º Milhar")
    elif decision == 2:
        hundreds_drawn = []
        for number in thousands_result.values():
            hundreds_drawn.append(number[1:])

        if final_choice in hundreds_drawn:
            qual_index = int(hundreds_drawn.index(final_choice) + 1)
            print(qual_index)
            if qual_index == 1:
                news = str(input("Eu tenho uma notícia boa e uma ruim pra você....\nQual você quer premeiro, Good or Bad? ")).strip().upper()[0]
                while news not in "GB":
                    news = str(input("Please, choice: Good or Bad? ")).strip().upper()[0]
                if news == "G":
                    print(f"Você ganhou sua aposta, e seu prêmio foi de R${int(bet*120)},00")
                    sleep(2)
                    print(f"Mas sua aposta tinha dado na cabeça...")
                    sleep(2)
                    print(f"Poderia ter ganhado R${int((bet*600) - (bet*120))},00 a mais se tivesse apostado somente na primeira, mesmo assim parabéns.")
                else:
                    print(f"Você poderia ter ganhado R${int((bet*600) - (bet*120))},00 a mais se tivesse apostado somente na primeira milhar...")
                    sleep(2)
                    print(f"Mas mesmo assim parabéns, você ganhou R${int(bet*120)},00")
            elif qual_index >= 2:
                print(f"Parabéns! Você ganhou na {qual_index}º Milhar")
                print(f"{qual_index}º Thousand: {thousands_result[f'{qual_index}º Thousand']}")
                sleep(2.5)
                print(f"Seu prêmio foi de R${int(bet*120)},00")
        else:
            print("Você não acertou a centena")

elif options == 4:
    sleep(1)
    line("Regras")
    print(
        f"Apostando na primeira milhar, caso você ganhe, seu prêmio será de 4000x sua aposta: R${int(bet*4000)},00 \nApostando da 1ª à 5ª Milhar, caso você ganhe, seu prêmio será de 800x sua aposta: R${int(bet*800)},00")
    print()

    verification = []
    final_choice = 0
    while True:
        four_numbers = str(input("Escolha 4 números para o milhar: "))
        verification.append(four_numbers)
        if len(verification[0]) == 4:
            final_choice = four_numbers
            break
        else:
            print("Por favor, escolha quatro números para formar a milhar que você deseja apostar.")
            verification.clear()

    print()
    decision = int(input("""Número [1] Para apostar na 1ª Milhar:
Número [2] Para apostar em todas as Milhares: """))
    while decision not in range(1, 4):
        print()
        print("Por favor, escolha um número que represente uma das opções abaixo.")
        decision = int(input("""Número [1] Para apostar na 1ª Milhar: 
Número [2] Para apostar em todas as Milhares: 
Escolha: """))

    line("result")
    pprint(thousands_result)
    print()
    if decision == 1:
        if final_choice == thousands_result['1º Thousand']:
            print("Deu na cabeça")
            print(f"1º Thousand: {thousands_result['1º Thousand']}")
            print(f"Seu prêmio foi de R${int(bet*4000)},00")
        else:
            print("Você não acertou a milhar da 1º Milhar")
    elif decision == 2:
        hundreds_drawn = []
        for number in thousands_result.values():
            hundreds_drawn.append(number)

        if final_choice in hundreds_drawn:
            qual_index = int(hundreds_drawn.index(final_choice) + 1)
            if qual_index == 1:
                news = str(input("Eu tenho uma notícia boa e uma ruim pra você....\nQual você quer premeiro, Good or Bad? ")).strip().upper()[0]
                while news not in "GB":
                    news = str(input("Please, choice: Good or Bad? ")).strip().upper()[0]
                if news == "G":
                    print(f"Você ganhou sua aposta, e seu prêmio foi de R${int(bet * 120)},00")
                    sleep(2)
                    print(f"Mas sua aposta tinha dado na cabeça...")
                    sleep(2)
                    print(f"Poderia ter ganhado R${int((bet*4000) - (bet*800))},00 a mais se tivesse apostado somente na primeira, mesmo assim parabéns.")
                else:
                    print(f"Você poderia ter ganhado R${int((bet*4000) - (bet*800))},00 a mais se tivesse apostado somente na primeira milhar...")
                    sleep(2)
                    print(f"Mas mesmo assim parabéns, você ganhou R${int(bet*800)},00")
            elif qual_index >= 2:
                print(f"Parabéns! Você ganhou na {qual_index}º Milhar")
                print(f"{qual_index}º Thousand: {thousands_result[f'{qual_index}º Thousand']}")
                sleep(2.5)
                print(f"Seu prêmio foi de R${int(bet*800)},00")
        else:
            print("Você não acertou nenhuma milhar")

elif options == 5:
    sleep(1)
    line("Regras")
    print(
        f"Cada grupo que você escolher terá 4 dezenas, se uma dezena de cada grupo estiver no final de \nduas das cinco milhares, você ganha. Seu prêmio será de 18,5x sua aposta: R${int(bet*18.5)},00")
    print()
    choice = int(input("""Número [1] Para escolher os grupo por número: 
Número [2] Para escolher os grupo por nome: 
Escolha: """))
    while choice not in range(1, 4):
        print()
        print("Por favor, escolha um número que representa uma das opções abaixo.")
        choice = int(input("""Número [1] Para escolher o grupo por número: 
Número [2] Para escolher o grupo por nome: 
Escolha: """))

    if choice == 1:
        final_choice = []
        while True:
            group1 = int(input("Qual é o número do 1º grupo? ").strip())
            while group1 not in range(1, 26):
                group1 = int(input("[ERROR] Escolha um número entre 1 e 25 representando o número de cada grupo."
                                  "\nQual é o número do 1º grupo? "))
            want_continue = str(input(f"O 1º grupo escolhido foi o do {groups[group1-1]['Name']}, quer continuar? [Y/N] ")).strip().upper()[0]
            while want_continue not in "YN":
                want_continue = str(input(f"O 1º grupo escolhido foi o do {groups[group1 - 1]['Name']}, quer continuar? [Y/N] ")).strip().upper()[0]
            if want_continue == "Y":
                final_choice.append(groups[group1 - 1])
                break
        while True:
            group2 = int(input("Qual é o número do 2º grupo? ").strip())
            while group2 == group1:
                print("Escolha um grupo diferente do anterior")
                group2 = int(input("Qual é o número do 2º grupo? ").strip())
            while group2 not in range(1, 26):
                group2 = int(input("[ERROR] Escolha um número entre 1 e 25 representando o número de cada grupo."
                                  "\nQual é o número do 2º grupo? "))
            want_continue = str(input(f"O 2º grupo escolhido foi o do {groups[group2 - 1]['Name']}, quer continuar? [Y/N] ")).strip().upper()[0]
            while want_continue not in "YN":
                want_continue = str(input(f"O 2º grupo escolhido foi o do {groups[group2 - 1]['Name']}, quer continuar? [Y/N] ")).strip().upper()[0]
            if want_continue == "Y":
                final_choice.append(groups[group2 - 1])
                break
        print()
        print(f"Escolhas → {final_choice}")
        print()
    elif choice == 2:
        final_choice = []
        verification = []
        for group in groups:
            verification.append(group['Name'].upper())
        while True:
            group1 = str(input("Qual é o nome do 1º grupo? ")).strip().upper()
            while group1 not in verification:
                group1 = str(input("Qual é o nome do grupo? ")).strip().upper()
            want_continue = str(input(f"Grupo escolhido foi o {group1.lower().capitalize()}, quer continuar? [Y/N] ")).strip().upper()[0]
            while want_continue not in "YN":
                want_continue = str(input(f"Grupo escolhido foi o {group1.lower().capitalize()}, quer continuar? [Y/N] ")).strip().upper()[0]
            if want_continue == "Y":
                final_choice.append(groups[verification.index(group1)])
                break
        while True:
            group2 = str(input("Qual é o nome do 2º grupo? ")).strip().upper()
            while group2 not in verification:
                group2 = str(input("Qual é o nome do 2º grupo? ")).strip().upper()
            want_continue = str(input(f"Grupo escolhido foi o {group2.lower().capitalize()}, quer continuar? [Y/N] ")).strip().upper()[0]
            while want_continue not in "YN":
                want_continue = str(input(f"Grupo escolhido foi o {group2.lower().capitalize()}, quer continuar? [Y/N] ")).strip().upper()[0]
            if want_continue == "Y":
                final_choice.append(groups[verification.index(group2)])
                break
        print(final_choice)

    line("result")
    pprint(thousands_result)
    print()

    dozens_drawn = []
    for number in thousands_result.values():
        dozens_drawn.append(number[2:])

    verification = [[], []]
    for number in final_choice[0]['Numbers']:
        if number in dozens_drawn:
            verification[0] = 1
            # Testar com varias dezenas certas

    for number in final_choice[1]['Numbers']:
        if number in dozens_drawn:
            verification[1] = 1

    if verification[0] == 1 and verification[1] == 1:
        print("Congrats, You won!")
        print(f"You got the {groups[group1-1]['Name']} group number and a {groups[group2-1]['Name']} group number right.")
        print(f"Seu prêmio foi de R${int(bet*18.5)},00")
    elif verification[0] == 1 and verification[1] != 1:
        print("Chegou perto")
        print(f"Você só acertou um número do grupo do(a) {groups[group1-1]['Name']} mas não acertou nenhum do(a) {groups[group2-1]['Name']}.")
        print("Boa Sorte da próxima vez!")
    elif verification[0] != 1 and verification[1] == 1:
        print("Chegou perto")
        print(f"Você só acertou um número do grupo do(a) {groups[group2-1]['Name']} mas não acertou nenhum do(a) {groups[group1-1]['Name']}.")
        print("Boa Sorte da próxima vez!")
    else:
        print("Você perdeu, nenhuma dezena dos grupos estavam nas milhares. \nBoa Sorte na próxima vez!")

elif options == 6:
    sleep(1)
    line("Regras")
    print(
        f"Para esse tipo de aposta você precisa escolher duas dezenas, se as duas dezenas escolhidas \nestiverem presentes no final de duas das 5 milhares você ganha. \nCaso você ganhe, seu prêmio será de 300x sua aposta: R${int(bet*300)},00")
    print()
    verification = []
    final_choice = []
    while True:
        ten1 = str(input("Escolha a 1º dezena: "))
        verification.append(ten1)
        if len(verification[0]) == 2:
            final_choice.append(ten1)
            break
        else:
            print("Por favor, escolha dois números entre 00 e 99 para formar a 1º dezena.")
            verification.clear()
    while True:
        ten2 = str(input("Escolha a 2º dezena: "))
        while ten2 == final_choice[0]:
            print("Escolha uma dezena diferente da primeira.")
            ten2 = str(input("Escolha a 2º dezena: "))
        verification.append(ten2)
        if len(verification[1]) == 2:
            final_choice.append(ten2)
            break
        else:
            print("Por favor, escolha dois números entre 00 e 99 para formar a 2º dezena.")
            verification.pop()

    line("result")
    pprint(thousands_result)
    print()

    dozens_drawn = []
    for number in thousands_result.values():
        dozens_drawn.append(number[2:])

    verification = [[], []]
    if final_choice[0] in dozens_drawn:
        verification[0] = 1

    if final_choice[1] in dozens_drawn:
        verification[1] = 1

    if verification[0] == 1 and verification[1] == 1:
        print("Congrats, You won!")
        print(f"You got both numbers right → {final_choice[0]} and {final_choice[1]}!")
        print(f"Seu prêmio foi de R${int(bet*300)},00")
    elif verification[0] == 1 and verification[1] != 1:
        print("Chegou perto")
        print(f"Você só acertou a primeira dezena '{final_choice[0]}' mas não acertou a segunda '{final_choice[1]}'.")
        print("Boa Sorte da próxima vez!")
    elif verification[0] != 1 and verification[1] == 1:
        print("Chegou perto")
        print(f"Você só acertou a segunda dezena '{final_choice[1]}' mas não acertou a primeira '{final_choice[0]}'.")
        print("Boa Sorte da próxima vez!")
    else:
        print("Você perdeu, nenhuma dezena que você escolheu estava nas milhares. \nBoa Sorte na próxima vez!")

elif options == 7:
    sleep(1)
    line("Regras")
    print(
        f"Para esse tipo de aposta você precisa escolher três dezenas, se as três dezenas escolhidas \nestiverem presentes no final de três das 5 milhares você ganha. \nCaso você ganhe, seu prêmio será de 3000x sua aposta: R${int(bet*3000)},00")
    print()
    verification = []
    final_choice = []
    while True:
        ten1 = str(input("Escolha a 1º dezena: "))
        verification.append(ten1)
        if len(verification[0]) == 2:
            final_choice.append(ten1)
            break
        else:
            print("Por favor, escolha dois números entre 00 e 99 para formar a 1º dezena.")
            verification.clear()
    while True:
        ten2 = str(input("Escolha a 2º dezena: "))
        while ten2 == final_choice[0]:
            print("Escolha uma dezena diferente da primeira.")
            ten2 = str(input("Escolha a 2º dezena: "))
        verification.append(ten2)
        if len(verification[1]) == 2:
            final_choice.append(ten2)
            break
        else:
            print("Por favor, escolha dois números entre 00 e 99 para formar a 2º dezena.")
            verification.pop()
    while True:
        ten3 = str(input("Escolha a 3º dezena: "))
        while ten3 == final_choice[0] or ten3 == final_choice[1]:
            print("Escolha uma dezena diferente das que você já escolheu.")
            ten3 = str(input("Escolha a 3º dezena: "))
        verification.append(ten3)
        if len(verification[2]) == 2:
            final_choice.append(ten3)
            break
        else:
            print("Por favor, escolha dois números entre 00 e 99 para formar a 3º dezena.")
            verification.pop()
    print(final_choice)

    line("result")
    pprint(thousands_result)
    print()

    dozens_drawn = []
    for number in thousands_result.values():
        dozens_drawn.append(number[2:])

    verification = [[], [], []]
    c = 0
    for number in final_choice:
        if number in dozens_drawn:
            verification[c] = 1
        c += 1

    hits = 0
    mistakes = [[], [], []]
    for number in verification:
        if number == 1:
            hits += 1

    if hits == 3:
        print("Congrats, You won!")
        print(f"You got al three numbers right → {final_choice[0]}, {final_choice[1]} and {final_choice[2]}!")
        print(f"Seu prêmio foi de R${int(bet * 3000)},00")
    elif hits == 2:
        print("Chegou perto...")
        print(f"Você não ganhou o prêmio, mas só errou uma dezena.\nBoa Sorte da próxima vez!")
    elif hits == 1:
        print("Não foi uma boa aposta...")
        print(f"Você só acertou uma dezena.\nBoa Sorte da próxima vez!")
    else:
        print("Você perdeu, nenhuma dezena que você escolheu estava nas milhares. \nBoa Sorte na próxima vez!")

elif options == 8:
    sleep(1)
    line("Regras")
    print(
        f"Cada grupo que você escolheu tem 4 dezenas, se uma dezena de cada grupo estiver em três \ndas cinco milhares, você ganha, seu prêmio será de 130x sua aposta: R${int(bet*130)},00")
    print()
    choice = int(input("""Número [1] Para escolher os grupo por número: 
Número [2] Para escolher os grupo por nome: 
Escolha: """))
    while choice not in range(1, 4):
        print()
        print("Por favor, escolha um número que representa uma das opções abaixo.")
        choice = int(input("""Número [1] Para escolher o grupo por número: 
Número [2] Para escolher o grupo por nome: 
Escolha: """))

    if choice == 1:
        final_choice = []
        while True:
            group1 = int(input("Qual é o número do 1º grupo? ").strip())
            while group1 not in range(1, 26):
                group1 = int(input("[ERROR] Escolha um número entre 1 e 25 representando o número de cada grupo."
                                   "\nQual é o número do 1º grupo? "))
            want_continue = str(input(f"O 1º grupo escolhido foi o do {groups[group1 - 1]['Name']}, quer continuar? [Y/N] ")).strip().upper()[0]
            while want_continue not in "YN":
                want_continue = str(input(f"O 1º grupo escolhido foi o do {groups[group1 - 1]['Name']}, quer continuar? [Y/N] ")).strip().upper()[0]
            if want_continue == "Y":
                final_choice.append(groups[group1 - 1])
                break
        while True:
            group2 = int(input("Qual é o número do 2º grupo? ").strip())
            while group2 not in range(1, 26):
                group2 = int(input("[ERROR] Escolha um número entre 1 e 25 representando o número de cada grupo."
                                   "\nQual é o número do 2º grupo? "))
            want_continue = str(input(f"O 2º grupo escolhido foi o do {groups[group2 - 1]['Name']}, quer continuar? [Y/N] ")).strip().upper()[0]
            while want_continue not in "YN":
                want_continue = str(input(f"O 2º grupo escolhido foi o do {groups[group2 - 1]['Name']}, quer continuar? [Y/N] ")).strip().upper()[0]
            if want_continue == "Y":
                final_choice.append(groups[group2 - 1])
                break
        while True:
            group3 = int(input("Qual é o número do 3º grupo? ").strip())
            while group3 not in range(1, 26):
                group3 = int(input("[ERROR] Escolha um número entre 1 e 25 representando o número de cada grupo."
                                   "\nQual é o número do 3º grupo? "))
            # while group3 == group2 or group3 == group1:
            #     print("Escolha um grupo diferente dos que você já escolheu")
            #     group3 = int(input("Qual é o número do 3º grupo? ").strip())
            want_continue = str(input(f"O 3º grupo escolhido foi o do {groups[group3 - 1]['Name']}, quer continuar? [Y/N] ")).strip().upper()[0]
            while want_continue not in "YN":
                want_continue = str(input(f"O 3º grupo escolhido foi o do {groups[group3 - 1]['Name']}, quer continuar? [Y/N] ")).strip().upper()[0]
            if want_continue == "Y":
                final_choice.append(groups[group3 - 1])
                break
        print()
        pprint(thousands_result)
        print()

        dozens_drawn = []
        for number in thousands_result.values():
            dozens_drawn.append(number[2:])

        verification = [[], [], []]
        for number in final_choice[0]['Numbers']:
            if number in dozens_drawn:
                verification[0] = 1

        for number in final_choice[1]['Numbers']:
            if number in dozens_drawn:
                verification[1] = 1

        for number in final_choice[2]['Numbers']:
            if number in dozens_drawn:
                verification[2] = 1

        if verification[0] == 1 and verification[1] == 1 and verification[2] == 1:
            print("Congrats, You won!\nYou hit at least a dozen of each group")
            print(f"Seu prêmio foi de R${int(bet*130)},00")
        elif verification[0] == 1 and verification[1] == 1 and verification[2] != 1:
            print("Chegou perto")
            print(f"Só faltou acertar uma dezena do grupo {groups[group3 - 1]['Name']}")
            print("Boa Sorte da próxima vez!")
        elif verification[0] == 1 and verification[1] != 1 and verification[2] == 1:
            print("Chegou perto")
            print(f"Só faltou acertar uma dezena do grupo {groups[group2 - 1]['Name']}")
            print("Boa Sorte da próxima vez!")
        elif verification[0] != 1 and verification[1] == 1 and verification[2] == 1:
            print("Chegou perto")
            print(f"Só faltou acertar uma dezena do grupo {groups[group1 - 1]['Name']}")
            print("Boa Sorte da próxima vez!")
        elif verification[0] == 1 and verification[1] != 1 and verification[2] != 1:
            print("Não foi uma boa aposta")
            print(f"você só acertou o grupo do(a) {groups[group1 - 1]['Name']}")
            print("Boa Sorte da próxima vez!")
        elif verification[0] != 1 and verification[1] == 1 and verification[2] != 1:
            print("Não foi uma boa aposta")
            print(f"você só acertou o grupo do(a) {groups[group2 - 1]['Name']}")
            print("Boa Sorte da próxima vez!")
        elif verification[0] != 1 and verification[1] != 1 and verification[2] == 1:
            print("Não foi uma boa aposta")
            print(f"você só acertou o grupo do(a) {groups[group3 - 1]['Name']}")
            print("Boa Sorte da próxima vez!")
        else:
            print("Você perdeu, nenhuma dezena dos grupos estavam nas milhares. \nBoa Sorte na próxima vez!")


# Posso tentar dar um pop() quando o número/grupo for escolhido, para evitar que a próxima escolha seja feita nele.