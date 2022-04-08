# Se os elementos da mesma linha começam com o visible = True, ta tudo certo, se por algum motivo, ao clicar em algum evento eu decido colocar esses botões DA MESMA LINHA com o visible = False, também ta tudo certo, mas se eu voltar eles para o True dps disso aparece um elemento em cada linha, doesn't make sense


from random import randint
from time import sleep

import PySimpleGUI as psg

psg.theme("DarkGrey13")

# groups = [
#     " Avestruz",
#     " Águia",
#     " Burro",
#     " Borboleta",
#     " Cachorro",
#     " Cabra",
#     " Carneiro",
#     " Camêlo",
#     " Cobra",
#     " Coelho",
#     " Cavalo",
#     " Elefante",
#     " Galo",
#     " Gato",
#     " Jacaré",
#     " Leão",
#     " Macaco",
#     " Porco",
#     " Pavão",
#     " Peru",
#     " Touro",
#     " Tigre",
#     " Urso",
#     " Veado",
#     " Vaca",
# ]

dozens = [
    "00", "01", "02", "03", "04", "05", "06", "08", "09", "10",
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
    "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
    "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
    "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
    "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
    "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
    "81", "82", "83", "84", "85", "86", "87", "88", "89", "90",
    "91", "92", "93", "94", "95", "96", "97", "98", "99"
]

dozens_beta = [
    "000", "001", "002", "003", "004", "005", "006", "008", "009", "010",
    "011", "012", "013", "014", "015", "016", "017", "018", "019", "020",
    "021", "022", "023", "024", "025", "026", "027", "028", "029", "030",
    "031", "032", "033", "034", "035", "036", "037", "038", "039", "040",
    "041", "042", "043", "044", "045", "046", "047", "048", "049", "050",
    "051", "052", "053", "054", "055", "056", "057", "058", "059", "060",
    "061", "062", "063", "064", "065", "066", "067", "068", "069", "070",
    "071", "072", "073", "074", "075", "076", "077", "078", "079", "080",
    "081", "082", "083", "084", "085", "086", "087", "088", "089", "090",
    "091", "092", "093", "094", "095", "096", "097", "098", "099"
]

centenas = dozens_beta + [c for c in range(100, 1000)]

thous_0 = []
thous_1 = []
thous_2 = []
thous_3 = []
thous_4 = []
thous_5 = []
thous_6 = []
thous_7 = []
thous_8 = []
thous_9 = []

for cent in centenas:
    thous_0.append(f"{'0'}{cent}")
    thous_1.append(f"{'1'}{cent}")
    thous_2.append(f"{'2'}{cent}")
    thous_3.append(f"{'3'}{cent}")
    thous_4.append(f"{'4'}{cent}")
    thous_5.append(f"{'5'}{cent}")
    thous_6.append(f"{'6'}{cent}")
    thous_7.append(f"{'7'}{cent}")
    thous_8.append(f"{'8'}{cent}")
    thous_9.append(f"{'9'}{cent}")

thousands = thous_0 + thous_1 + thous_2 + thous_3 + thous_4 + thous_5 + thous_6 + thous_7 + thous_8 + thous_9

full_groups = [
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

gameOptions = [
    "Aposta no Grupo",
    "Aposta na Dezena",
    "Aposta na Centena",
    "Aposta na Milhar",
    "Duque de Grupo",
    "Duque de Dezena",
    "Terno de Dezena",
    "Terno de Grupo"
]

# thousands_result = [[[randint(0, 9) for c in range(1, 5)] for c in range(6)]]
# thousands_result = {}
# for c in range(0, 6):
#     thousands_result[f'{c+1}º Thousand'] = f"{thousands[0][c][0]}{thousands[0][c][1]}{thousands[0][c][2]}{thousands[0][c][3]}"

thousands_result = {
    "1º Thousand": "9901",
    "2º Thousand": "3699",
    "3º Thousand": "1488",
    "4º Thousand": "1901",
    "5º Thousand": "9999",
    "6º Thousand": "9974",
}

def create_window1_groups():
    layout = [
        [psg.Text("Meet Animal Groups to play:"), psg.Button("Next", size=(7, 1))],
        [psg.Text("01:"), psg.Text("Avestruz", size=(7, 1)), psg.Text("Numbers:"), psg.Text("01-02-03-04")],
        [psg.Text("02:"), psg.Text("Águia", size=(7, 1)), psg.Text("Numbers:"), psg.Text("05-06-07-08")],
        [psg.Text("03:"), psg.Text("Burro", size=(7, 1)), psg.Text("Numbers:"), psg.Text("09-10-11-12")],
        [psg.Text("04:"), psg.Text("Borboleta", size=(7, 1)), psg.Text("Numbers:"), psg.Text("13-14-15-16")],
        [psg.Text("05:"), psg.Text("Cachorro", size=(7, 1)), psg.Text("Numbers:"), psg.Text("17-18-19-20")],
        [psg.Text("06:"), psg.Text("Cabra", size=(7, 1)), psg.Text("Numbers:"), psg.Text("21-22-23-24")],
        [psg.Text("07:"), psg.Text("Carneiro", size=(7, 1)), psg.Text("Numbers:"), psg.Text("25-26-27-28")],
        [psg.Text("08:"), psg.Text("Camêlo", size=(7, 1)), psg.Text("Numbers:"), psg.Text("29-30-31-32")],
        [psg.Text("09:"), psg.Text("Cobra", size=(7, 1)), psg.Text("Numbers:"), psg.Text("33-34-35-36")],
        [psg.Text("10:"), psg.Text("Coelho", size=(7, 1)), psg.Text("Numbers:"), psg.Text("37-38-39-40")],
        [psg.Text("11:"), psg.Text("Cavalo", size=(7, 1)), psg.Text("Numbers:"), psg.Text("41-42-43-44")],
        [psg.Text("12:"), psg.Text("Elefante", size=(7, 1)), psg.Text("Numbers:"), psg.Text("45-46-47-48")],
        [psg.Text("13:"), psg.Text("Galo", size=(7, 1)), psg.Text("Numbers:"), psg.Text("49-50-51-52")],
        [psg.Text("14:"), psg.Text("Gato", size=(7, 1)), psg.Text("Numbers:"), psg.Text("53-54-55-56")],
        [psg.Text("15:"), psg.Text("Jacaré", size=(7, 1)), psg.Text("Numbers:"), psg.Text("57-58-59-60")],
        [psg.Text("16:"), psg.Text("Leão", size=(7, 1)), psg.Text("Numbers:"), psg.Text("61-62-63-64")],
        [psg.Text("17:"), psg.Text("Macaco", size=(7, 1)), psg.Text("Numbers:"), psg.Text("65-66-67-68")],
        [psg.Text("18:"), psg.Text("Porco", size=(7, 1)), psg.Text("Numbers:"), psg.Text("69-70-71-72")],
        [psg.Text("19:"), psg.Text("Pavão", size=(7, 1)), psg.Text("Numbers:"), psg.Text("73-74-75-76")],
        [psg.Text("20:"), psg.Text("Peru", size=(7, 1)), psg.Text("Numbers:"), psg.Text("77-78-79-80")],
        [psg.Text("21:"), psg.Text("Touro", size=(7, 1)), psg.Text("Numbers:"), psg.Text("81-82-83-84")],
        [psg.Text("22:"), psg.Text("Tigre", size=(7, 1)), psg.Text("Numbers:"), psg.Text("85-86-87-88")],
        [psg.Text("23:"), psg.Text("Urso", size=(7, 1)), psg.Text("Numbers:"), psg.Text("89-90-91-92")],
        [psg.Text("24:"), psg.Text("Veado", size=(7, 1)), psg.Text("Numbers:"), psg.Text("93-94-95-96")],
        [psg.Text("25:"), psg.Text("Vaca", size=(7, 1)), psg.Text("Numbers:"), psg.Text("97-98-99-00")],
    ]
    return psg.Window("Animal Groups", layout, finalize=True)

def create_window2_game_options():
    bet = [
        [
            psg.Text("Aposta  R$"),
            psg.Input(size=(9, 1), key="bet"), psg.Button("Back", size=(7, 1), key="fefes")
        ],
    ]

    choose_game_option = [
        [
            psg.Combo(values=gameOptions, key="game_option", size=(19, 1), default_value="Aposta no Grupo"),
            psg.Button("Confirm", key="confirm_1_w2", size=(10, 1)),
            psg.Button("Cancel", key="cancel_1_w2", size=(7, 1), disabled=True),
        ],

    ]

    rules = [
        [psg.Button("See Rules", key="rules_w2", size=(39, 1))],
        [psg.Output(size=(42, 9))],
        [psg.Button("Send Options", size=(39, 1), key="send_options_w2", disabled=True)]
    ]

    layout = [
        [psg.Frame("Bet", bet)],
        [psg.Frame("Choose Game Option", choose_game_option)],
        [psg.Frame("Rules", rules)]
    ]

    return psg.Window("Game Options", layout, finalize=True)

def create_window_option1():
    bet = [
        [
            psg.Text(gmop, key="chosen_game"),
            psg.Text(f"Your bet was R${value['bet']},00"),
            psg.Button("Back", size=(6, 1))
        ],
    ]

    choose_group = [
        [
            psg.Combo(values=[c['Name'] for c in full_groups], key="choose_1gp", size=(19, 1), default_value="Avestruz"),
            psg.Button("Confirm", key="confirm_1_w3", size=(10, 1), disabled=False),
            psg.Button("Cancel", key="cancel_1_w3", size=(6, 1), disabled=True)
        ],

    ]

    award = [
        [
            psg.Radio("Apostar somente na 1º Milhar: ", group_id="choose_bet", key="choose_bet1", size=(23, 1), default=True),
            psg.Button(f"R${int(value['bet']) * 18},00", size=(10, 1), key="award_1")
        ],

        [
            psg.Radio("Apostar em todas as Milhares: ", group_id="choose_bet", key="choose_bet2", size=(23, 1)),
            psg.Button(f"R${int(value['bet']) * 3.6}0", size=(10, 1), key="award_2")
        ],
    ]

    left_column = [
        [psg.Text("1º Thousand:"), psg.Text("****", key="result_t1")],
        [psg.Text("2º Thousand:"), psg.Text("****", key="result_t2")],
        [psg.Text("3º Thousand:"), psg.Text("****", key="result_t3")],
        [psg.Text("4º Thousand:"), psg.Text("****", key="result_t4")],
        [psg.Text("5º Thousand:"), psg.Text("****", key="result_t5")],
        [psg.Text("6º Thousand:"), psg.Text("****", key="result_t6")],
    ]

    right_column = [
        [psg.Output(size=(19, 9))]
    ]

    draw_thousands = [
        [psg.Button("Draw Thousands", size=(38, 1), key="draw_1", disabled=True)],
        [psg.Column(left_column), psg.Column(right_column)],
    ]

    layout = [
        [psg.Frame("Bet", bet)],
        [psg.Frame("Choose Group", choose_group)],
        [psg.Frame("Award", award)],
        [psg.Frame("Draw Thousands", draw_thousands)],
    ]

    return psg.Window("Game Result", layout, finalize=True)

def create_window_option2():
    bet = [
        [
            psg.Text(gmop, key="chosen_game"),
            psg.Text(f"Your bet was R${value['bet']},00", key="testado"),
            psg.Button("Back", size=(6, 1))
        ],
    ]

    choose_dozen = [
        [
            psg.Combo(values=dozens, key="choose_1dz", size=(19, 1), default_value="00"),
            psg.Button("Confirm", key="confirm_2_w3", size=(10, 1), disabled=False),
            psg.Button("Cancel", key="cancel_2_w3", size=(7, 1), disabled=True),
        ],
    ]

    award = [
        [
            psg.Radio("Apostar somente na 1º Milhar: ", group_id="choose_bet", key="choose_bet1", size=(22, 1), default=True),
            psg.Button(f"R${int(value['bet']) * 60},00", size=(11, 1), key="award_3")
        ],

        [
            psg.Radio("Apostar em todas as Milhares: ", group_id="choose_bet", key="choose_bet2", size=(22, 1)),
            psg.Button(f"R${int(value['bet']) * 12},00", size=(11, 1), key="award_4")
        ],
    ]

    left_column = [
        [psg.Text("1º Thousand:"), psg.Text("****", key="result_t1")],
        [psg.Text("2º Thousand:"), psg.Text("****", key="result_t2")],
        [psg.Text("3º Thousand:"), psg.Text("****", key="result_t3")],
        [psg.Text("4º Thousand:"), psg.Text("****", key="result_t4")],
        [psg.Text("5º Thousand:"), psg.Text("****", key="result_t5")],
        [psg.Text("6º Thousand:"), psg.Text("****", key="result_t6")],
    ]

    right_column = [
        [psg.Output(size=(19, 9))]
    ]

    draw_thousands = [
        [psg.Button("Draw Thousands", size=(37, 1), key="draw_2", disabled=True)],
        [psg.Column(left_column), psg.Column(right_column)],
    ]

    layout = [
        [psg.Frame("Bet", bet)],
        [psg.Frame("Choose Dozen", choose_dozen)],
        [psg.Frame("Award", award)],
        [psg.Frame("Draw Thousands", draw_thousands)],
    ]

    return psg.Window("Game Result", layout, finalize=True)

def create_window_option3():
    bet = [
        [
            psg.Text(gmop, key="chosen_game"),
            psg.Text(f"Your bet was R${value['bet']},00", key="testado"),
            psg.Button("Back", size=(6, 1))
        ],
    ]

    choose_centena = [
        [
            psg.Combo(values=centenas, key="choose_1hund", size=(19, 1), default_value="000"),
            psg.Button("Confirm", key="confirm_3_w3", size=(10, 1), disabled=False),
            psg.Button("Cancel", key="cancel_3_w3", size=(7, 1), disabled=True),
        ],
    ]

    award = [
        [
            psg.Radio("Apostar somente na 1º Milhar: ", group_id="choose_bet", key="choose_bet1", size=(22, 1), default=True),
            psg.Button(f"R${int(value['bet']) * 600},00", size=(11, 1), key="award_5")
        ],

        [
            psg.Radio("Apostar em todas as Milhares: ", group_id="choose_bet", key="choose_bet2", size=(22, 1)),
            psg.Button(f"R${int(value['bet']) * 120},00", size=(11, 1), key="award_6")
        ],
    ]

    left_column = [
        [psg.Text("1º Thousand:"), psg.Text("****", key="result_t1")],
        [psg.Text("2º Thousand:"), psg.Text("****", key="result_t2")],
        [psg.Text("3º Thousand:"), psg.Text("****", key="result_t3")],
        [psg.Text("4º Thousand:"), psg.Text("****", key="result_t4")],
        [psg.Text("5º Thousand:"), psg.Text("****", key="result_t5")],
        [psg.Text("6º Thousand:"), psg.Text("****", key="result_t6")],
    ]

    right_column = [
        [psg.Output(size=(19, 9))]
    ]

    draw_thousands = [
        [psg.Button("Draw Thousands", size=(37, 1), key="draw_3", disabled=True)],
        [psg.Column(left_column), psg.Column(right_column)],
    ]

    layout = [
        [psg.Frame("Bet", bet)],
        [psg.Frame("Choose Centena", choose_centena)],
        [psg.Frame("Award", award)],
        [psg.Frame("Draw Thousands", draw_thousands)],
    ]

    return psg.Window("Game Result", layout, finalize=True)

def create_window_option4():
    bet = [
        [
            psg.Text(gmop, key="chosen_game"),
            psg.Text(f"Your bet was R${value['bet']},00", key="testado"),
            psg.Button("Back", size=(6, 1))
        ],
    ]

    choose_thousand = [
        [
            psg.Combo(values=thousands, key="choose_1thous", size=(19, 1), default_value="0000"),
            psg.Button("Confirm", key="confirm_4_w3", size=(10, 1), disabled=False),
            psg.Button("Cancel", key="cancel_4_w3", size=(7, 1), disabled=True),
        ],
    ]

    award = [
        [
            psg.Radio("Apostar somente na 1º Milhar: ", group_id="choose_bet", key="choose_bet1", size=(22, 1), default=True),
            psg.Button(f"R${int(value['bet']) * 4000},00", size=(11, 1), key="award_7")
        ],

        [
            psg.Radio("Apostar em todas as Milhares: ", group_id="choose_bet", key="choose_bet2", size=(22, 1)),
            psg.Button(f"R${int(value['bet']) * 800},00", size=(11, 1), key="award_8")
        ],
    ]

    left_column = [
        [psg.Text("1º Thousand:"), psg.Text("****", key="result_t1")],
        [psg.Text("2º Thousand:"), psg.Text("****", key="result_t2")],
        [psg.Text("3º Thousand:"), psg.Text("****", key="result_t3")],
        [psg.Text("4º Thousand:"), psg.Text("****", key="result_t4")],
        [psg.Text("5º Thousand:"), psg.Text("****", key="result_t5")],
        [psg.Text("6º Thousand:"), psg.Text("****", key="result_t6")],
    ]

    right_column = [
        [psg.Output(size=(19, 9))]
    ]

    draw_thousands = [
        [psg.Button("Draw Thousands", size=(37, 1), key="draw_4", disabled=True)],
        [psg.Column(left_column), psg.Column(right_column)],
    ]

    layout = [
        [psg.Frame("Bet", bet)],
        [psg.Frame("Choose Thousand", choose_thousand)],
        [psg.Frame("Award", award)],
        [psg.Frame("Draw Thousands", draw_thousands)],
    ]

    return psg.Window("Game Result", layout, finalize=True)

def create_window_option5():
    bet = [
        [
            psg.Text(gmop, key="chosen_game"),
            psg.Text(f"Your bet was R${value['bet']},00", key="saS"),
            psg.Button("Back", size=(6, 1))
        ],
    ]

    choose_groups = [
        [
            psg.Combo(values=[c['Name'] for c in full_groups], key="choose_2gps_1", size=(19, 1), default_value="Avestruz"),
            psg.Button("Confirm", key="confirm_5_w3", size=(10, 1), disabled=False),
            psg.Button("Cancel", key="cancel_5_w3", size=(7, 1), disabled=True),
        ],

        [
            psg.Combo(values=[c['Name'] for c in full_groups], key="choose_2gps_2", size=(19, 1), default_value="Avestruz", disabled=True),
            psg.Button("Confirm", key="confirm_6_w3", size=(10, 1), disabled=True),
            psg.Button("Cancel", key="cancel_6_w3", size=(7, 1), disabled=True),
        ],
    ]

    left_column = [
        [psg.Text("1º Thousand:"), psg.Text("****", key="result_t1")],
        [psg.Text("2º Thousand:"), psg.Text("****", key="result_t2")],
        [psg.Text("3º Thousand:"), psg.Text("****", key="result_t3")],
        [psg.Text("4º Thousand:"), psg.Text("****", key="result_t4")],
        [psg.Text("5º Thousand:"), psg.Text("****", key="result_t5")],
        [psg.Text("6º Thousand:"), psg.Text("****", key="result_t6")],
    ]

    right_column = [
        [psg.Output(size=(19, 9))]
    ]

    draw_thousands = [
        [psg.Button("Draw Thousands", size=(37, 1), key="draw_5", disabled=True)],
        [psg.Column(left_column), psg.Column(right_column)],
    ]

    layout = [
        [psg.Frame("Bet", bet)],
        [psg.Frame("Choose Groups", choose_groups)],
        [psg.Frame("Draw Thousands", draw_thousands)],
    ]

    return psg.Window("Game Result", layout, finalize=True)

def create_window_option6():
    bet = [
        [
            psg.Text(gmop, key="chosen_game"),
            psg.Text(f"Your bet was R${value['bet']},00", key="qwerty"),
            psg.Button("Back", size=(6, 1))
        ],
    ]

    choose_dozens = [
        [
            psg.Combo(values=dozens, key="choose_2dzs_1", size=(19, 1), default_value="00"),
            psg.Button("Confirm", key="confirm_7_w3", size=(10, 1)),
            psg.Button("Cancel", key="cancel_7_w3", size=(7, 1), disabled=True),
        ],

        [
            psg.Combo(values=dozens, key="choose_2dzs_2", size=(19, 1), default_value="00", disabled=True),
            psg.Button("Confirm", key="confirm_8_w3", size=(10, 1), disabled=True),
            psg.Button("Cancel", key="cancel_8_w3", size=(7, 1), disabled=True),
        ],
    ]

    left_column = [
        [psg.Text("1º Thousand:"), psg.Text("****", key="result_t1")],
        [psg.Text("2º Thousand:"), psg.Text("****", key="result_t2")],
        [psg.Text("3º Thousand:"), psg.Text("****", key="result_t3")],
        [psg.Text("4º Thousand:"), psg.Text("****", key="result_t4")],
        [psg.Text("5º Thousand:"), psg.Text("****", key="result_t5")],
        [psg.Text("6º Thousand:"), psg.Text("****", key="result_t6")],
    ]

    right_column = [
        [psg.Output(size=(19, 9))]
    ]

    draw_thousands = [
        [psg.Button("Draw Thousands", size=(37, 1), key="draw_6", disabled=True)],
        [psg.Column(left_column), psg.Column(right_column)],
    ]

    layout = [
        [psg.Frame("Bet", bet)],
        [psg.Frame("Choose Dozens", choose_dozens)],
        [psg.Frame("Draw Thousands", draw_thousands)],
    ]

    return psg.Window("Game Result", layout, finalize=True)

def create_window_option7():
    bet = [
        [
            psg.Text(gmop, key="chosen_game"),
            psg.Text(f"Your bet was R${value['bet']},00", key="asdfg"),
            psg.Button("Back", size=(6, 1))
        ],
    ]

    choose_dozens = [
        [
            psg.Combo(values=dozens, key="choose_3dzs_1", size=(19, 1), default_value="00"),
            psg.Button("Confirm", key="confirm_9_w3", size=(10, 1)),
            psg.Button("Cancel", key="cancel_9_w3", size=(7, 1), disabled=True),
        ],

        [
            psg.Combo(values=dozens, key="choose_3dzs_2", size=(19, 1), default_value="00", disabled=True),
            psg.Button("Confirm", key="confirm_10_w3", size=(10, 1), disabled=True),
            psg.Button("Cancel", key="cancel_10_w3", size=(7, 1), disabled=True),
        ],

        [
            psg.Combo(values=dozens, key="choose_3dzs_3", size=(19, 1), default_value="00", disabled=True),
            psg.Button("Confirm", key="confirm_11_w3", size=(10, 1), disabled=True),
            psg.Button("Cancel", key="cancel_11_w3", size=(7, 1), disabled=True),
        ],
    ]

    left_column = [
        [psg.Text("1º Thousand:"), psg.Text("****", key="result_t1")],
        [psg.Text("2º Thousand:"), psg.Text("****", key="result_t2")],
        [psg.Text("3º Thousand:"), psg.Text("****", key="result_t3")],
        [psg.Text("4º Thousand:"), psg.Text("****", key="result_t4")],
        [psg.Text("5º Thousand:"), psg.Text("****", key="result_t5")],
        [psg.Text("6º Thousand:"), psg.Text("****", key="result_t6")],
    ]

    right_column = [
        [psg.Output(size=(19, 9))]
    ]

    draw_thousands = [
        [psg.Button("Draw Thousands", size=(37, 1), key="draw_7", disabled=True)],
        [psg.Column(left_column), psg.Column(right_column)],
    ]

    layout = [
        [psg.Frame("Bet", bet)],
        [psg.Frame("Choose Dozens", choose_dozens)],
        [psg.Frame("Draw Thousands", draw_thousands)],
    ]

    return psg.Window("Game Result", layout, finalize=True)

def create_window_option8():
    bet = [
        [
            psg.Text(gmop, key="chosen_game"),
            psg.Text(f"Your bet was R${value['bet']},00", key="zxcvb"),
            psg.Button("Back", size=(6, 1))
        ],
    ]

    choose_groups = [
        [
            psg.Combo(values=[c['Name'] for c in full_groups], key="choose_3gps_1", size=(19, 1), default_value="Avestruz"),
            psg.Button("Confirm", key="confirm_12_w3", size=(10, 1)),
            psg.Button("Cancel", key="cancel_12_w3", size=(7, 1), disabled=True),
        ],

        [
            psg.Combo(values=[c['Name'] for c in full_groups], key="choose_3gps_2", size=(19, 1), default_value="Avestruz", disabled=True),
            psg.Button("Confirm", key="confirm_13_w3", size=(10, 1), disabled=True),
            psg.Button("Cancel", key="cancel_13_w3", size=(7, 1), disabled=True),
        ],

        [
            psg.Combo(values=[c['Name'] for c in full_groups], key="choose_3gps_3", size=(19, 1), default_value="Avestruz", disabled=True),
            psg.Button("Confirm", key="confirm_14_w3", size=(10, 1), disabled=True),
            psg.Button("Cancel", key="cancel_14_w3", size=(7, 1), disabled=True),
        ],
    ]

    left_column = [
        [psg.Text("1º Thousand:"), psg.Text("****", key="result_t1")],
        [psg.Text("2º Thousand:"), psg.Text("****", key="result_t2")],
        [psg.Text("3º Thousand:"), psg.Text("****", key="result_t3")],
        [psg.Text("4º Thousand:"), psg.Text("****", key="result_t4")],
        [psg.Text("5º Thousand:"), psg.Text("****", key="result_t5")],
        [psg.Text("6º Thousand:"), psg.Text("****", key="result_t6")],
    ]

    right_column = [
        [psg.Output(size=(19, 9))]
    ]

    draw_thousands = [
        [psg.Button("Draw Thousands", size=(37, 1), key="draw_8", disabled=True)],
        [psg.Column(left_column), psg.Column(right_column)],
    ]

    layout = [
        [psg.Frame("Bet", bet)],
        [psg.Frame("Choose Groups", choose_groups)],
        [psg.Frame("Draw Thousands", draw_thousands)],
    ]

    return psg.Window("Game Result", layout, finalize=True)


window1, window2, window3 = create_window1_groups(), None, None

gmop = ""

while True:
    window, event, value = psg.read_all_windows()

    if window == window1:
        if event in (psg.WIN_CLOSED, "Exit"):
            window.close()
            break

        if event == "Next":
            window1.hide()
            window2 = create_window2_game_options()

    if window == window2:

        if event in (psg.WIN_CLOSED, "Exit"):
            window.close()
            break


        if event == "Back":
            window2.hide()
            window1.un_hide()

        if event == "confirm_1_w2":
            if str(value['game_option']).strip().upper() not in [c.upper() for c in gameOptions]:
                var = [psg.popup_auto_close(f"O modo \"{value['game_option']}\" não existe.\nPor Favor escolha outro", title="Modo Inválido", auto_close=True, auto_close_duration=2.5)]
            else:
                window['game_option'].update(disabled=True)
                window['confirm_1_w2'].update(disabled=True)
                window['cancel_1_w2'].update(disabled=False)

        if event == "rules_w2":
            if str(value['game_option']).strip().upper() not in [c.upper() for c in gameOptions]:
                var = [psg.popup_auto_close(f"O modo \"{value['game_option']}\" não existe.\nPor Favor escolha outro", title="Modo Inválido", auto_close=True, auto_close_duration=2.5)]



            # Validar se começa/termina/tem 2 vírgulas
            if value['bet']:
                validation = 0
                for ch in str(value['bet']).replace(',', '.'):
                    if ch == ".":
                        validation += 1
                    if validation > 1:
                        print("não pode ter vários")
                        break
                    if ch[0] == ".":
                        var = [
                            psg.popup_auto_close(f"Não pode começar com , ou .", title="Modo Inválido", auto_close=True, auto_close_duration=2.5)]
                        break
                    if ch[-1] == ",":
                        var = [
                            psg.popup_auto_close(f"Não pode terminar com , ou .", title="Modo Inválido", auto_close=True, auto_close_duration=2.5)]
                        break
                    else:
                        if float(str(value['bet']).replace(',', '.')) <= 0:
                            print("Pfv escolha um número maior que 0 para apostar")

                        else:
                            if str(value['game_option']).strip().upper() == "APOSTA NO GRUPO":
                                print("----------------- Regras Aposta no Grupo -----------------")
                                print(
                                    f"\nApostando na 1º milhar, caso você ganhe, seu \nprêmio será de 18x sua aposta: R${float(str(value['bet']).replace(',', '.'))*18:.2f} \n\nApostando da 1º à 6º Milhar, caso você ganhe,\nseu prêmio será de 3,6x sua aposta: R${float(str(value['bet']).replace(',', '.'))*3.6:.1f}0\n")

                            elif str(value['game_option']).strip().upper() == "APOSTA NA DEZENA":
                                print("---------------- Regras Aposta na Dezena ----------------")
                                print(
                                    f"\nApostando na 1º milhar, caso você ganhe, seu \nprêmio será de 60x sua aposta: R${float(str(value['bet']).replace(',', '.'))*60:.2f} \n\nApostando da 1ª à 6ª Milhar, caso você ganhe,\nseu prêmio será de 12x sua aposta: R${float(str(value['bet']).replace(',', '.'))*12:.1f}0\n")

                            elif str(value['game_option']).strip().upper() == "APOSTA NA CENTENA":
                                print("---------------- Regras Aposta na Centena ----------------")
                                print(
                                    f"Apostando na 1º milhar, caso você ganhe, seu \nprêmio será de 600x sua aposta: R${float(str(value['bet']).replace(',', '.'))*600:.2f} \n\nApostando da 1º à 6º Milhar caso você ganhe, \nseu prêmio será de 120x sua aposta: R${float(str(value['bet']).replace(',', '.'))*120:.1f}0\n")

                            elif str(value['game_option']).strip().upper() == "APOSTA NA MILHAR":
                                print("------------------ Regras Aposta na Milhar -----------------")
                                print(
                                    f"\nApostando na 1º Milhar, caso você ganhe, seu \nprêmio será de 4000x sua aposta: R${float(str(value['bet']).replace(',', '.'))*4020} \n\nApostando da 1ª à 6ª Milhar, caso você ganhe, \nseu prêmio será de 800,x sua aposta: R${float(str(value['bet']).replace(',', '.'))*800}0\n")

                            elif str(value['game_option']).strip().upper() == "DUQUE DE GRUPO":
                                print("------------------ Regras Duque de Grupo ------------------")
                                print(
                                    f"\nCada grupo que você escolher terá 4 dezenas.\nSe uma dezena de cada grupo estiver no final de \nduas das cinco milhares, você ganha.\n\nCaso você ganhe, seu prêmio será de \n18,5x sua aposta: R${float(str(value['bet']).replace(',', '.'))*18.5:.2f}\n")

                            elif str(value['game_option']).strip().upper() == "DUQUE DE DEZENA":
                                print("----------------- Regras Duque de Dezena -----------------")
                                print(
                                    f"\nPara esse tipo de aposta você precisa escolher \nduas dezenas, se as duas dezenas escolhidas \nestiverem presentes no final de duas das \n5 milhares você ganha. \n\nCaso você ganhe, seu prêmio será de \n300x sua aposta: R${float(str(value['bet']).replace(',', '.'))*300:.2f}\n")

                            elif str(value['game_option']).strip().upper() == "TERNO DE DEZENA":
                                print("----------------- Regras Terno de Dezena ------------------")
                                print(
                                    f"\nPara esse tipo de aposta você precisa escolher \ntrês dezenas, se as três dezenas escolhidas \nestiverem presentes no final de três das \n6 milhares você ganha.\n\nCaso você ganhe, seu prêmio será de \n300x sua aposta: R${float(str(value['bet']).replace(',', '.'))*3000:.2f}\n")

                            elif str(value['game_option']).strip().upper() == "TERNO DE GRUPO":
                                print("------------------- Regras Terno de Grupo -------------------")
                                print(
                                    f"\nCada grupo que você escolheu tem 4 dezenas,\nse uma dezena de cada grupo estiver em três \ndas cinco milhares, você ganha.\n\nCaso você ganhe, seu prêmio será de \n130x sua aposta: R${float(str(value['bet']).replace(',', '.'))*130:.2f}\n")

            else:
                print("Choose bet amount")

        # if event == "confirm_1_w2":
        #     if value['game_option'] in gameOptions:
        #         window['game_option'].update(disabled=True)
        #         window['cancel_1_w2'].update(disabled=False)
        #         window['send_options_w2'].update(disabled=False)
        #
        # if event == "cancel_1_w2":
        #     window['cancel_1_w2'].update(disabled=True)
        #     window['confirm_1_w2'].update(disabled=False)
        #     window['game_option'].update(disabled=False)
        #     window['send_options_w2'].update(disabled=True)
        #
        # if event == "send_options_w2":
        #
        #     if value['bet']:
        #
        #         if int(value['bet']) <= 0:
        #             print("Pfv escolha um número maior que 0 para apostar")
        #         else:
        #             window2.hide()
        #             gmop = value['game_option']
        #             if value['game_option'][1:] == "Aposta no Grupo":
        #                 window3 = create_window_option1()
        #             elif value['game_option'][1:] == "Aposta na Dezena":
        #                 window3 = create_window_option2()
        #             elif value['game_option'][1:] == "Aposta na Centena":
        #                 window3 = create_window_option3()
        #             elif value['game_option'][1:] == "Aposta na Milhar":
        #                 window3 = create_window_option4()
        #             elif value['game_option'][1:] == "Duque de Grupo":
        #                 window3 = create_window_option5()
        #             elif value['game_option'][1:] == "Duque de Dezena":
        #                 window3 = create_window_option6()
        #             elif value['game_option'][1:] == "Terno de Dezena":
        #                 window3 = create_window_option7()
        #             elif value['game_option'][1:] == "Terno de Grupo":
        #                 window3 = create_window_option8()
        #
        #     else:
        #         print("Please, put how much you will bet")

    if window == window3:

        if event in (psg.WIN_CLOSED, "Exit"):
            window.close()
            break

        if event == "Back":
            window3.hide()
            window2 = create_window2_game_options()

        # Aposta no grupo
        if event == "confirm_1_w3":
            if str(value['choose_1gp']).strip().upper() not in [c['Name'].upper() for c in full_groups]:
                var = [psg.popup_auto_close(f"O grupo \"{value['choose_1gp']}\" não existe.\nPor Favor escolha outro", auto_close=True, auto_close_duration=2.5)]
            else:
                window['choose_1gp'].update(disabled=True)
                window['confirm_1_w3'].update(disabled=True)
                window['cancel_1_w3'].update(disabled=False)
                window['draw_1'].update(disabled=False)

        if event == "cancel_1_w3":
            window['choose_1gp'].update(disabled=False)
            window['confirm_1_w3'].update(disabled=False)
            window['cancel_1_w3'].update(disabled=True)
            window['draw_1'].update(disabled=True)

        # Aposta na Dezena
        if event == "confirm_2_w3":
            if value['choose_1dz'] not in dozens:
                var = [psg.popup_auto_close(f"A dezena \"{value['choose_1dz']}\" não existe.\nPor Favor escolha outra.\n\nDezenas entre 00-99", auto_close=True, auto_close_duration=2.5)]
            else:
                window['choose_1dz'].update(disabled=True)
                window['confirm_2_w3'].update(disabled=True)
                window['cancel_2_w3'].update(disabled=False)
                window['draw_2'].update(disabled=False)

        if event == "cancel_2_w3":
            window['choose_1dz'].update(disabled=False)
            window['confirm_2_w3'].update(disabled=False)
            window['cancel_2_w3'].update(disabled=True)
            window['draw_2'].update(disabled=True)

        # Aposta na Centena
        if event == "confirm_3_w3":
            if value['choose_1hund'] not in centenas:
                var = [psg.popup_auto_close(f"A centena \"{value['choose_1hund']}\" não existe.\nPor Favor escolha outra.\n\nCentenas entre 000-999", auto_close=True, auto_close_duration=2.5)]
            else:
                window['choose_1hund'].update(disabled=True)
                window['confirm_3_w3'].update(disabled=True)
                window['cancel_3_w3'].update(disabled=False)
                window['draw_3'].update(disabled=False)

        if event == "cancel_3_w3":
            window['choose_1hund'].update(disabled=False)
            window['confirm_3_w3'].update(disabled=False)
            window['cancel_3_w3'].update(disabled=True)
            window['draw_3'].update(disabled=True)

        # Aposta na Milhar
        if event == "confirm_4_w3":
            if value['choose_1thous'] not in thousands:
                var = [psg.popup_auto_close(f"A centena \"{value['choose_1thous']}\" não existe.\nPor Favor escolha outra.\n\nThousands entre 0000-9999", auto_close=True, auto_close_duration=2.5)]
            else:
                window['choose_1thous'].update(disabled=True)
                window['confirm_4_w3'].update(disabled=True)
                window['cancel_4_w3'].update(disabled=False)
                window['draw_4'].update(disabled=False)

        if event == "cancel_4_w3":
            window['choose_1thous'].update(disabled=False)
            window['confirm_4_w3'].update(disabled=False)
            window['cancel_4_w3'].update(disabled=True)
            window['draw_4'].update(disabled=True)

        # Duque de Grupo
        if event == "confirm_5_w3":
            if str(value['choose_2gps_1']).strip().upper() not in [c['Name'].upper() for c in full_groups]:
                var = [psg.popup_auto_close(f"A centena \"{value['choose_2_gps_1']}\" não existe.\nPor Favor escolha outro.", auto_close=True, auto_close_duration=2.5)]
            else:
                window['choose_2gps_1'].update(disabled=True)
                window['confirm_5_w3'].update(disabled=True)
                window['cancel_5_w3'].update(disabled=False)
                window['choose_2gps_2'].update(disabled=False)
                window['confirm_6_w3'].update(disabled=False)

        if event == "cancel_5_w3":
            window['choose_2gps_1'].update(disabled=False)
            window['confirm_5_w3'].update(disabled=False)
            window['cancel_5_w3'].update(disabled=True)
            window['choose_2gps_2'].update(disabled=True)
            window['confirm_6_w3'].update(disabled=True)
            window['cancel_6_w3'].update(disabled=True)
            window['draw_5'].update(disabled=True)

        if event == "confirm_6_w3":
            if str(value['choose_2gps_2']).strip().upper() not in [c['Name'].upper() for c in full_groups]:
                var = [psg.popup_auto_close(f"A centena \"{value['choose_2_gps_2']}\" não existe.\nPor Favor escolha outro.", auto_close=True, auto_close_duration=2.5)]
            elif value['choose_2gps_2'] == value['choose_2gps_1']:
                var = [psg.popup_auto_close("O 2º grupo é igual o grupo anterior.\nPor favor escolha outro")]
            else:
                window['choose_2gps_2'].update(disabled=True)
                # window['cancel_5_w3'].update(disabled=True)
                window['confirm_6_w3'].update(disabled=True)
                window['cancel_6_w3'].update(disabled=False)
                window['draw_5'].update(disabled=False)

        if event == "cancel_6_w3":
            window['choose_2gps_2'].update(disabled=False)
            window['cancel_5_w3'].update(disabled=False)
            window['confirm_6_w3'].update(disabled=False)
            window['cancel_6_w3'].update(disabled=True)
            window['draw_5'].update(disabled=True)

        # Duque de Dezena
        if event == "confirm_7_w3":
            if value['choose_2dzs_1'] not in dozens:
                var = [psg.popup_auto_close(f"A centena \"{value['choose_2dzs_1']}\" não existe.\nPor Favor escolha outro.", auto_close=True, auto_close_duration=2.5)]
            else:
                window['choose_2dzs_1'].update(disabled=True)
                window['confirm_7_w3'].update(disabled=True)
                window['cancel_7_w3'].update(disabled=False)
                window['choose_2dzs_2'].update(disabled=False)
                window['confirm_8_w3'].update(disabled=False)

        if event == "cancel_7_w3":
            window['choose_2dzs_1'].update(disabled=False)
            window['confirm_7_w3'].update(disabled=False)
            window['cancel_7_w3'].update(disabled=True)
            window['choose_2dzs_2'].update(disabled=True)
            window['confirm_8_w3'].update(disabled=True)
            window['cancel_8_w3'].update(disabled=True)
            window['draw_6'].update(disabled=True)

        if event == "confirm_8_w3":
            if value['choose_2dzs_2'] not in dozens:
                var = [psg.popup_auto_close(f"A centena \"{value['choose_2_dzs_2']}\" não existe.\nPor Favor escolha outro.", auto_close=True, auto_close_duration=2.5)]
            elif value['choose_2dzs_2'] == value['choose_2dzs_1']:
                var = [psg.popup_auto_close("A 2º dezena é igual à anterior.\nPor favor escolha outra")]
            else:
                window['choose_2dzs_2'].update(disabled=True)
                window['confirm_8_w3'].update(disabled=True)
                window['cancel_8_w3'].update(disabled=False)
                window['draw_6'].update(disabled=False)

        if event == "cancel_8_w3":
            window['choose_2dzs_2'].update(disabled=False)
            window['cancel_7_w3'].update(disabled=False)
            window['confirm_8_w3'].update(disabled=False)
            window['cancel_8_w3'].update(disabled=True)
            window['draw_6'].update(disabled=True)

        # Terno de Dezena
        if event == "confirm_9_w3":
            if value['choose_3dzs_1'] not in dozens:
                var = [psg.popup_auto_close(f"A centena \"{value['choose_3dzs_1']}\" não existe.\nPor Favor escolha outro.", auto_close=True, auto_close_duration=2.5)]
            else:
                window['choose_3dzs_1'].update(disabled=True)
                window['confirm_9_w3'].update(disabled=True)
                window['cancel_9_w3'].update(disabled=False)
                window['choose_3dzs_2'].update(disabled=False)
                window['confirm_10_w3'].update(disabled=False)

        if event == "cancel_9_w3":
            window['choose_3dzs_1'].update(disabled=False)
            window['confirm_9_w3'].update(disabled=False)
            window['cancel_9_w3'].update(disabled=True)
            window['choose_3dzs_2'].update(disabled=True)
            window['confirm_10_w3'].update(disabled=True)
            window['cancel_10_w3'].update(disabled=True)
            window['choose_3dzs_2'].update(disabled=True)
            window['choose_3dzs_3'].update(disabled=True)
            window['confirm_11_w3'].update(disabled=True)
            window['cancel_11_w3'].update(disabled=True)
            window['draw_7'].update(disabled=True)

        if event == "confirm_10_w3":
            if value['choose_3dzs_2'] not in dozens:
                var = [psg.popup_auto_close(f"A centena \"{value['choose_3dzs_2']}\" não existe.\nPor Favor escolha outro.", auto_close=True, auto_close_duration=2.5)]
            elif value['choose_3dzs_2'] == value['choose_3dzs_1']:
                var = [psg.popup_auto_close("A 2º dezena é igual à anterior.\nPor favor escolha outra")]
            else:
                window['choose_3dzs_2'].update(disabled=True)
                window['confirm_10_w3'].update(disabled=True)
                window['cancel_10_w3'].update(disabled=False)
                window['choose_3dzs_3'].update(disabled=False)
                window['confirm_11_w3'].update(disabled=False)

        if event == "cancel_10_w3":
            window['choose_3dzs_2'].update(disabled=False)
            window['cancel_9_w3'].update(disabled=False)
            window['confirm_10_w3'].update(disabled=False)
            window['cancel_10_w3'].update(disabled=True)
            window['choose_3dzs_3'].update(disabled=True)
            window['confirm_11_w3'].update(disabled=True)
            window['cancel_11_w3'].update(disabled=True)
            window['draw_7'].update(disabled=True)

        if event == "confirm_11_w3":
            if value['choose_3dzs_3'] not in dozens:
                var = [psg.popup_auto_close(f"A centena \"{value['choose_3dzs_3']}\" não existe.\nPor Favor escolha outro.", auto_close=True, auto_close_duration=2.5)]
            elif value['choose_3dzs_3'] == value['choose_3dzs_2']:
                var = [psg.popup_auto_close("A 3º dezena é igual à 2º Dezena.\nPor favor escolha outra")]
            elif value['choose_3dzs_3'] == value['choose_3dzs_1']:
                var = [psg.popup_auto_close("A 3º dezena é igual à 1º Dezena.\nPor favor escolha outra")]
            else:
                window['choose_3dzs_3'].update(disabled=True)
                window['confirm_11_w3'].update(disabled=True)
                window['cancel_11_w3'].update(disabled=False)
                window['draw_7'].update(disabled=False)

        if event == "cancel_11_w3":
            window['choose_3dzs_3'].update(disabled=False)
            window['confirm_11_w3'].update(disabled=False)
            window['cancel_11_w3'].update(disabled=True)
            window['draw_7'].update(disabled=True)

        # Terno de Grupo
        if event == "confirm_12_w3":
            if str(value['choose_3gps_1']).strip().upper() not in [c['Name'].upper() for c in full_groups]:
                var = [psg.popup_auto_close(f"O grupo \"{value['choose_3gps_1']}\" não existe.\nPor Favor escolha outro.", auto_close=True, auto_close_duration=2.5)]
            else:
                window['choose_3gps_1'].update(disabled=True)
                window['confirm_12_w3'].update(disabled=True)
                window['cancel_12_w3'].update(disabled=False)
                window['choose_3gps_2'].update(disabled=False)
                window['confirm_13_w3'].update(disabled=False)

        if event == "cancel_12_w3":
            window['choose_3gps_1'].update(disabled=False)
            window['confirm_12_w3'].update(disabled=False)
            window['cancel_12_w3'].update(disabled=True)
            window['choose_3gps_2'].update(disabled=True)
            window['confirm_13_w3'].update(disabled=True)
            window['cancel_13_w3'].update(disabled=True)
            window['choose_3gps_3'].update(disabled=True)
            window['confirm_14_w3'].update(disabled=True)
            window['cancel_14_w3'].update(disabled=True)
            window['draw_8'].update(disabled=True)

        if event == "confirm_13_w3":
            if str(value['choose_3gps_2']).strip().upper() not in [c['Name'].upper() for c in full_groups]:
                var = [psg.popup_auto_close(f"O Grupo \"{value['choose_3gps_2']}\" não existe.\nPor Favor escolha outro.", auto_close=True, auto_close_duration=2.5)]
            elif value['choose_3gps_2'] == value['choose_3gps_1']:
                var = [psg.popup_auto_close("Esse grupo é igual ao 1º Grupo.\nPor favor escolha outro")]
            else:
                window['choose_3gps_2'].update(disabled=True)
                window['confirm_13_w3'].update(disabled=True)
                window['cancel_13_w3'].update(disabled=False)
                window['choose_3gps_3'].update(disabled=False)
                window['confirm_14_w3'].update(disabled=False)

        if event == "cancel_13_w3":
            window['choose_3gps_2'].update(disabled=False)
            window['confirm_13_w3'].update(disabled=False)
            window['cancel_13_w3'].update(disabled=True)
            window['choose_3gps_3'].update(disabled=True)
            window['confirm_14_w3'].update(disabled=True)
            window['cancel_14_w3'].update(disabled=True)
            window['draw_8'].update(disabled=True)

        if event == "confirm_14_w3":
            if str(value['choose_3gps_3']).strip().upper() not in [c['Name'].upper() for c in full_groups]:
                var = [psg.popup_auto_close(f"O Grupo \"{value['choose_3gps_3']}\" não existe.\nPor Favor escolha outro.", auto_close=True, auto_close_duration=2.5)]
            elif value['choose_3gps_3'] == value['choose_3gps_1']:
                var = [psg.popup_auto_close("Esse grupo é igual ao 1º Grupo.\nPor favor escolha outro")]
            elif value['choose_3gps_3'] == value['choose_3gps_2']:
                var = [psg.popup_auto_close("Esse grupo é igual ao 2º Grupo.\nPor favor escolha outro")]
            else:
                window['choose_3gps_3'].update(disabled=True)
                window['confirm_14_w3'].update(disabled=True)
                window['cancel_14_w3'].update(disabled=False)
                window['draw_8'].update(disabled=False)

        if event == "cancel_14_w3":
            window['choose_3gps_3'].update(disabled=False)
            window['confirm_14_w3'].update(disabled=False)
            window['cancel_14_w3'].update(disabled=True)
            window['draw_8'].update(disabled=True)


        if event == "draw_1" or event == "draw_2" or event == "draw_3" or event == "draw_4" or event == "draw_5" or event == "draw_6" or event == "draw_7" or event == "draw_8":
            window['result_t1'].update(thousands_result['1º Thousand'])
            window['result_t2'].update(thousands_result['2º Thousand'])
            window['result_t3'].update(thousands_result['3º Thousand'])
            window['result_t4'].update(thousands_result['4º Thousand'])
            window['result_t5'].update(thousands_result['5º Thousand'])
            window['result_t6'].update(thousands_result['6º Thousand'])

            t1 = thousands_result['1º Thousand']
            t2 = thousands_result['2º Thousand']
            t3 = thousands_result['3º Thousand']
            t4 = thousands_result['4º Thousand']
            t5 = thousands_result['5º Thousand']
            t6 = thousands_result['6º Thousand']

            all_thousands = [t1, t2, t3, t4, t5, t6]

            if event == "draw_1":
                window['Back'].update(disabled=True)
                window['cancel_1_w3'].update(disabled=True)
                window['choose_bet1'].update(disabled=True)
                window['award_1'].update(disabled=True)
                window['choose_bet2'].update(disabled=True)
                window['award_2'].update(disabled=True)
                window['draw_1'].update(disabled=True)

                final_choice = []

                for c in full_groups:
                    if c['Name'] == value['choose_1gp'][1:]:
                        final_choice.append(c['Numbers'])

                if value['choose_bet1']:
                    tries = 0
                    for number in final_choice[0]:
                        if number == t1[2:]:
                            print("-=-= Parabéns!!! =-=-")
                            sleep(1.5)
                            print("→ Deu na Cabeça")
                            sleep(2)
                            print()
                            print(f"Nº \"{number}\" na 1º Milhar")
                            sleep(1)
                            print(f"Prêmio: {window['award_1'].get_text()}")
                            print()
                            sleep(1)
                            print("Até a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                            window[f'result_t1'].update(text_color="green")
                            break
                        else:
                            tries += 1

                    if tries == 4:
                        print(" -=-= Resultado =-=-=-")
                        print("Você não acertou \nna 1º Milhar")
                        for number in final_choice[0]:
                            for t in all_thousands:
                                if number == t[2:]:
                                    sleep(2)
                                    print()
                                    print(f"Se tivesse apostado \nem todas as milhares,\nvocê teria acertado \nna {all_thousands.index(t)+1}º Milhar")
                                    window[f'result_t{all_thousands.index(t)+1}'].update(text_color="red")
                        print("\nBoa sorte da Próxima.\n-=-=-=-=-=-=-=-=-=-=-")

                elif value['choose_bet2']:
                    win_1 = False
                    tries = 0
                    for number in final_choice[0]:
                        if number == t1[2:]:
                            print("-=-= Parabéns!!! =-=-")
                            sleep(1)
                            print("→ Você ganhou...")
                            sleep(1.5)
                            print("Mas eu tenho duas\nnotícias pra você...")
                            sleep(2)
                            print()
                            print(f"A boa é que você\nganhou {window['award_2'].get_text()}")
                            sleep(2)
                            print()
                            print("A ruim é que seu\nresultado saiu na\n1º Milhar...")
                            sleep(2)
                            print()
                            print(f"Se tivesse apostado \nsó nela teria \nganhado {window['award_1'].get_text()}")
                            sleep(2)
                            print()
                            print("Mas Parabéns!\nFoi uma boa aposta.\n-=-=-=-=-=-=-=-=-=-=-")

                            window[f'result_t{all_thousands.index(t1)+1}'].update(text_color="green")

                            win_1 = True
                            break

                    if not win_1:
                        win = False
                        for t in all_thousands:
                            if not win:
                                for number in final_choice[0]:
                                    if number == t[2:]:
                                        print(f" -=-= Parabéns!!! =-=-")
                                        sleep(2)
                                        print(f"O número \"{t[2:]}\" saiu\nna {all_thousands.index(t)+1}º Milhar.\n\nSeu prêmio:{window['award_2'].get_text()}\n-=-=-=-=-=-=-=-=-=-=-")

                                        window[f'result_t{all_thousands.index(t)+1}'].update(text_color="green")
                                        win = True
                                        break
                                    else:
                                        tries += 1
                        if tries == 24:
                            print("-=-= Você Perdeu =-=-\nQue pena...\nVocê não acertou \nnenhuma dezena.\n\nBoa sorte da \npróxima vez...\n-=-=-=-=-=-=-=-=-=-=-")

            if event == "draw_2":
                window['Back'].update(disabled=True)
                window['cancel_2_w3'].update(disabled=True)
                window['choose_bet1'].update(disabled=True)
                window['award_3'].update(disabled=True)
                window['choose_bet2'].update(disabled=True)
                window['award_4'].update(disabled=True)
                window['draw_2'].update(disabled=True)

                if value['choose_bet1']:
                    if value['choose_1dz'] == t1[2:]:
                        print("-=-= Parabéns!!! =-=-")
                        sleep(1.5)
                        print("→ Deu na Cabeça")
                        sleep(2)
                        print()
                        print(f"Nº \"{value['choose_1dz']}\" na 1º Milhar")
                        sleep(1)
                        print(f"Prêmio: {window['award_3'].get_text()}")
                        print()
                        sleep(1)
                        print("Até a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                        window[f'result_t1'].update(text_color="green")

                    else:
                        print(" -=-= Resultado =-=-=-")
                        print("Você não acertou \nna 1º Milhar")
                        for t in all_thousands:
                            if value['choose_1dz'] == t[2:]:
                                sleep(2)
                                print()
                                print(f"Se tivesse apostado \nem todas as milhares,\nvocê teria acertado \nna {all_thousands.index(t) + 1}º Milhar")
                                window[f'result_t{all_thousands.index(t) + 1}'].update(text_color="red")
                        print("\nBoa sorte da Próxima.\n-=-=-=-=-=-=-=-=-=-=-")

                elif value['choose_bet2']:
                    if value['choose_1dz'] == t1[2:]:
                        print("-=-= Parabéns!!! =-=-")
                        sleep(1)
                        print("→ Você ganhou...")
                        sleep(1.5)
                        print("Mas eu tenho duas\nnotícias pra você...")
                        sleep(2)
                        print()
                        print(f"A boa é que você\nganhou {window['award_4'].get_text()}")
                        sleep(2)
                        print()
                        print("A ruim é que seu\nresultado saiu na\n1º Milhar...")
                        sleep(2)
                        print()
                        print(f"Se tivesse apostado \nsó nela teria \nganhado {window['award_3'].get_text()}")
                        sleep(2)
                        print()
                        print("Mas Parabéns!\nFoi uma boa aposta.\n-=-=-=-=-=-=-=-=-=-=-")

                        window[f'result_t{all_thousands.index(t1) + 1}'].update(text_color="green")

                    else:
                        win = False
                        tries = 0
                        for t in all_thousands:
                            if not win:
                                if value['choose_1dz'] == t[2:]:
                                    print(f" -=-= Parabéns!!! =-=-")
                                    sleep(2)
                                    print(f"O número \"{t[2:]}\" saiu\nna {all_thousands.index(t) + 1}º Milhar.\n\nSeu prêmio:{window['award_4'].get_text()}\n-=-=-=-=-=-=-=-=-=-=-")

                                    window[f'result_t{all_thousands.index(t) + 1}'].update(text_color="green")
                                    break
                                else:
                                    tries += 1
                        if tries == 6:
                            print("-=-= Você Perdeu =-=-")
                            sleep(1.5)
                            print("Que pena...")
                            sleep(1)
                            print("Você não acertou \nnenhuma dezena.")
                            sleep(1.5)
                            print()
                            print("Boa sorte da \npróxima vez...\n-=-=-=-=-=-=-=-=-=-=-")

            if event == "draw_3":
                window['Back'].update(disabled=True)
                window['cancel_3_w3'].update(disabled=True)
                window['choose_bet1'].update(disabled=True)
                window['award_5'].update(disabled=True)
                window['choose_bet2'].update(disabled=True)
                window['award_6'].update(disabled=True)
                window['draw_3'].update(disabled=True)

                if value['choose_bet1']:
                    if value['choose_1hund'] == int(t1[1:]):
                        print("-=-= Parabéns!!! =-=-")
                        sleep(1.5)
                        print("→ Deu na Cabeça")
                        sleep(2)
                        print()
                        print(f"Nº \"{value['choose_1hund']}\" na 1º Milhar")
                        sleep(1)
                        print(f"Prêmio: {window['award_5'].get_text()}")
                        print()
                        sleep(1)
                        print("Até a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                        window[f'result_t1'].update(text_color="green")

                    else:
                        print(" -=-= Resultado =-=-=-")
                        print("Você não acertou \nna 1º Milhar")
                        for t in all_thousands:
                            if value['choose_1hund'] == int(t[1:]):
                                sleep(2)
                                print()
                                print(f"Se tivesse apostado \nem todas as milhares,\nvocê teria acertado \nna {all_thousands.index(t) + 1}º Milhar")
                                window[f'result_t{all_thousands.index(t) + 1}'].update(text_color="red")
                        print("\nBoa sorte da Próxima.\n-=-=-=-=-=-=-=-=-=-=-")

                elif value['choose_bet2']:
                    if value['choose_1hund'] == int(t1[1:]):
                        print("-=-= Parabéns!!! =-=-")
                        sleep(1)
                        print("→ Você ganhou...")
                        sleep(1.5)
                        print("Mas eu tenho duas\nnotícias pra você...")
                        sleep(2)
                        print()
                        print(f"A boa é que você\nganhou {window['award_6'].get_text()}")
                        sleep(2)
                        print()
                        print("A ruim é que seu\nresultado saiu na\n1º Milhar...")
                        sleep(2)
                        print()
                        print(f"Se tivesse apostado \nsó nela teria \nganhado {window['award_5'].get_text()}")
                        sleep(2)
                        print()
                        print("Mas Parabéns!\nFoi uma boa aposta.\n-=-=-=-=-=-=-=-=-=-=-")

                        window[f'result_t{all_thousands.index(t1) + 1}'].update(text_color="green")

                    else:
                        win = False
                        tries = 0
                        for t in all_thousands:
                            if not win:
                                if value['choose_1hund'] == int(t[1:]):
                                    print(f" -=-= Parabéns!!! =-=-")
                                    sleep(2)
                                    print(f"O número \"{t[1:]}\" saiu\nna {all_thousands.index(t) + 1}º Milhar.\n\nSeu prêmio:{window['award_6'].get_text()}\n-=-=-=-=-=-=-=-=-=-=-")

                                    window[f'result_t{all_thousands.index(t) + 1}'].update(text_color="green")
                                    break
                                else:
                                    tries += 1
                        if tries == 6:
                            print("-=-= Você Perdeu =-=-")
                            sleep(1.5)
                            print("Que pena...")
                            sleep(1)
                            print("Você não acertou \na centena.")
                            sleep(1.5)
                            print()
                            print("Boa sorte da \npróxima vez...\n-=-=-=-=-=-=-=-=-=-=-")

            if event == "draw_4":
                window['Back'].update(disabled=True)
                window['cancel_4_w3'].update(disabled=True)
                window['choose_bet1'].update(disabled=True)
                window['award_7'].update(disabled=True)
                window['choose_bet2'].update(disabled=True)
                window['award_8'].update(disabled=True)
                window['draw_4'].update(disabled=True)

                if value['choose_bet1']:
                    if value['choose_1thous'] == t1:
                        print("-=-= Parabéns!!! =-=-")
                        sleep(1.5)
                        print("→ Deu na Cabeça")
                        sleep(2)
                        print()
                        print(f"Nº \"{value['choose_1thous']}\" na 1º Milhar")
                        sleep(1)
                        print(f"Prêmio: {window['award_7'].get_text()}")
                        print()
                        sleep(1)
                        print("Até a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                        window[f'result_t1'].update(text_color="green")

                    else:
                        print(" -=-= Resultado =-=-=-")
                        print("Você não acertou \nna 1º Milhar")
                        for t in all_thousands:
                            if value['choose_1thous'] == t:
                                sleep(2)
                                print()
                                print(f"Se tivesse apostado \nem todas as milhares,\nvocê teria acertado \nna {all_thousands.index(t) + 1}º Milhar")
                                window[f'result_t{all_thousands.index(t) + 1}'].update(text_color="red")
                        print("\nBoa sorte da Próxima.\n-=-=-=-=-=-=-=-=-=-=-")

                elif value['choose_bet2']:
                    if value['choose_1thous'] == t1:
                        print("-=-= Parabéns!!! =-=-")
                        sleep(1)
                        print("→ Você ganhou...")
                        sleep(1.5)
                        print("Mas eu tenho duas\nnotícias pra você...")
                        sleep(2)
                        print()
                        print(f"A boa é que você\nganhou {window['award_8'].get_text()}")
                        sleep(2)
                        print()
                        print("A ruim é que seu\nresultado saiu na\n1º Milhar...")
                        sleep(2)
                        print()
                        print(f"Se tivesse apostado \nsó nela teria \nganhado {window['award_7'].get_text()}")
                        sleep(2)
                        print()
                        print("Mas Parabéns!\nFoi uma boa aposta.\n-=-=-=-=-=-=-=-=-=-=-")

                        window[f'result_t{all_thousands.index(t1) + 1}'].update(text_color="green")

                    else:
                        win = False
                        tries = 0
                        for t in all_thousands:
                            if not win:
                                if value['choose_1thous'] == t:
                                    print(f" -=-= Parabéns!!! =-=-")
                                    sleep(2)
                                    print(f"O número \"{t}\" saiu\nna {all_thousands.index(t) + 1}º Milhar.\n\nSeu prêmio:{window['award_8'].get_text()}\n-=-=-=-=-=-=-=-=-=-=-")

                                    window[f'result_t{all_thousands.index(t) + 1}'].update(text_color="green")
                                    break
                                else:
                                    tries += 1
                        if tries == 6:
                            print("-=-= Você Perdeu =-=-")
                            sleep(1.5)
                            print("Que pena...")
                            sleep(1)
                            print("Você não acertou \na Milhar.")
                            sleep(1.5)
                            print()
                            print("Boa sorte da \npróxima vez...\n-=-=-=-=-=-=-=-=-=-=-")

            if event == 'draw_5':
                window['Back'].update(disabled=True)
                window['cancel_5_w3'].update(disabled=True)
                window['cancel_6_w3'].update(disabled=True)
                window['draw_5'].update(disabled=True)

                final_choice = [[], []]
                verification_groups = [[], []]
                correct_numbers = [[], []]

                for g in full_groups:
                    if g['Name'] == value['choose_2gps_1'][1:]:
                        final_choice[0] = g['Numbers']
                    if g['Name'] == value['choose_2gps_2'][1:]:
                        final_choice[1] = g['Numbers']

                for i, choice in enumerate(final_choice):
                    for t in all_thousands:
                        for number in choice:
                            if number == t[2:]:
                                if not verification_groups[i]:
                                    verification_groups[i] = [1, all_thousands.index(t) + 1]
                                    correct_numbers[i] = number

                total = len(verification_groups[0]) + len(verification_groups[1])

                if total == 4:
                    print("-=-= Parabéns!!! =-=-")
                    sleep(1.5)
                    print(f"Você acertou uma\ndezena de cada grupo:")
                    print(f"\"{correct_numbers[0]}\" e \"{correct_numbers[1]}\"")
                    sleep(1)
                    print()
                    print(f"Prêmio: R${int(window['saS'].DisplayText[15:-3]) * 18.5}0")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                    window[f'result_t{verification_groups[0][1]}'].update(text_color="green")
                    window[f'result_t{verification_groups[1][1]}'].update(text_color="green")

                elif total == 2:
                    if len(verification_groups[1]) == 0:
                        print(" -=-= Resultado =-=-")
                        sleep(2)
                        print("Você Perdeu...")
                        sleep(1)
                        print()
                        print(f"Passou perto, mas\nfaltou acertar o grupo\ndo(a) \"{value['choose_2gps_2']}\"")
                        sleep(1)
                        print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                        window[f'result_t{verification_groups[0][1]}'].update(text_color="green")

                    elif len(verification_groups[0]) == 0:
                        print(" -=-= Resultado =-=-")
                        sleep(2)
                        print("Você Perdeu...")
                        sleep(1)
                        print()
                        print(f"Passou perto, mas\nfaltou acertar o grupo\ndo(a) \"{value['choose_2gps_1']}\"")
                        sleep(1)
                        print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                        window[f'result_t{verification_groups[1][1]}'].update(text_color="green")
                else:
                    print(" -=-= Resultado =-=-")
                    sleep(2)
                    print("Você Perdeu...")
                    sleep(1)
                    print()
                    print("Acabou não acertando\nnenhum grupo.")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

            if event == 'draw_6':
                window['Back'].update(disabled=True)
                window['cancel_7_w3'].update(disabled=True)
                window['cancel_8_w3'].update(disabled=True)
                window['draw_6'].update(disabled=True)

                final_choice = [[value['choose_2dzs_1']], [value['choose_2dzs_2']]]

                verification_1dz = [[], []]
                verification_2dz = [[], []]

                for t in all_thousands:
                    if t[2:] == final_choice[0][0]:
                        verification_1dz[0] = 1
                        verification_1dz[1] = all_thousands.index(t) + 1

                    if t[2:] == final_choice[1][0]:
                        verification_2dz[0] = 1
                        verification_2dz[1] = all_thousands.index(t) + 1

                if verification_1dz[0] == 1 and verification_2dz[0] == 1:
                    print("-=-= Parabéns!!! =-=-")
                    sleep(1.5)
                    print(f"Você acertou as duas\ndezenas: \"{final_choice[0][0]}\" e \"{final_choice[1][0]}\"")
                    sleep(1)
                    print()
                    print(f"Prêmio: R${int(window['qwerty'].DisplayText[15:-3])*300},00")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                    window[f'result_t{verification_1dz[1]}'].update(text_color="green")
                    window[f'result_t{verification_2dz[1]}'].update(text_color="green")

                elif verification_1dz[0] == 1 and verification_2dz[0] != 1:
                    print("-=-= Resultado =-=-")
                    sleep(1.5)
                    print("Você perdeu...")
                    sleep(1)
                    print()
                    print(f"Passou perto mas \nfaltou acertar a \ndezena \"{final_choice[1][0]}\"")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                    window[f'result_t{verification_1dz[1]}'].update(text_color="green")

                elif verification_1dz[0] != 1 and verification_2dz[0] == 1:
                    print("-=-= Resultado =-=-")
                    sleep(1.5)
                    print("Você perdeu...")
                    sleep(1)
                    print()
                    print(f"Passou perto mas \nfaltou acertar a \ndezena \"{final_choice[0][0]}\"")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                    window[f'result_t{verification_2dz[1]}'].update(text_color="green")

                else:
                    print(" -=-= Resultado =-=-")
                    sleep(2)
                    print("Você Perdeu...")
                    sleep(1)
                    print()
                    print("Acabou não acertando\nnenhuma dezena.")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

            if event == 'draw_7':
                window['Back'].update(disabled=True)
                window['cancel_9_w3'].update(disabled=True)
                window['cancel_10_w3'].update(disabled=True)
                window['cancel_11_w3'].update(disabled=True)
                window['draw_7'].update(disabled=True)

                final_choice = [[value['choose_3dzs_1']], [value['choose_3dzs_2']], [value['choose_3dzs_3']]]

                verification_1dz = [[], []]
                verification_2dz = [[], []]
                verification_3dz = [[], []]

                for t in all_thousands:
                    if t[2:] == final_choice[0][0]:
                        verification_1dz[0] = 1
                        verification_1dz[1] = all_thousands.index(t) + 1

                    if t[2:] == final_choice[1][0]:
                        verification_2dz[0] = 1
                        verification_2dz[1] = all_thousands.index(t) + 1

                    if t[2:] == final_choice[2][0]:
                        verification_3dz[0] = 1
                        verification_3dz[1] = all_thousands.index(t) + 1

                if verification_1dz[0] == 1 and verification_2dz[0] == 1 and verification_3dz[0] == 1:
                    print("-=-= Parabéns!!! =-=-")
                    sleep(1.5)
                    print(f"Você acertou as três\ndezenas: [{final_choice[0][0]}, {final_choice[1][0]}, {final_choice[2][0]}]")
                    sleep(1)
                    print()
                    print(f"Prêmio: R${int(window['asdfg'].DisplayText[15:-3]) * 3000},00")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                    window[f'result_t{verification_1dz[1]}'].update(text_color="green")
                    window[f'result_t{verification_2dz[1]}'].update(text_color="green")
                    window[f'result_t{verification_3dz[1]}'].update(text_color="green")

                elif verification_1dz[0] == 1 and verification_2dz[0] == 1 and verification_3dz[0] != 1:
                    print("-=-= Resultado =-=-")
                    sleep(1.5)
                    print("Passou Raspando...")
                    sleep(1)
                    print()
                    print(f"Se acertasse a \ndezena \"{final_choice[2][0]}\"\nvocê ganhava seu prêmio\nde R${int(window['asdfg'].DisplayText[15:-3]) * 3000},00")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                    window[f'result_t{verification_1dz[1]}'].update(text_color="green")
                    window[f'result_t{verification_2dz[1]}'].update(text_color="green")

                elif verification_1dz[0] == 1 and verification_2dz[0] != 1 and verification_3dz[0] == 1:
                    print("-=-= Resultado =-=-")
                    sleep(1.5)
                    print("Passou Raspando...")
                    sleep(1)
                    print()
                    print(f"Se acertasse a \ndezena \"{final_choice[1][0]}\"\nvocê ganhava seu prêmio\nde R${int(window['asdfg'].DisplayText[15:-3]) * 3000},00")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                    window[f'result_t{verification_1dz[1]}'].update(text_color="green")
                    window[f'result_t{verification_3dz[1]}'].update(text_color="green")

                elif verification_1dz[0] != 1 and verification_2dz[0] == 1 and verification_3dz[0] == 1:
                    print("-=-= Resultado =-=-")
                    sleep(1.5)
                    print("Passou Raspando...")
                    sleep(1)
                    print()
                    print(f"Se acertasse a \ndezena \"{final_choice[0][0]}\"\nvocê ganhava seu prêmio\nde R${int(window['asdfg'].DisplayText[15:-3]) * 3000},00")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                    window[f'result_t{verification_2dz[1]}'].update(text_color="green")
                    window[f'result_t{verification_3dz[1]}'].update(text_color="green")

                elif verification_1dz[0] == 1 and verification_2dz[0] != 1 and verification_3dz[0] != 1:
                    print("-=-= Resultado =-=-")
                    sleep(1.5)
                    print("Você perdeu...")
                    sleep(1)
                    print()
                    print(f"Passou longe.\nfaltou acertar a \ndezena \"{final_choice[1][0]}\" e \"{final_choice[2][0]}\"")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                    window[f'result_t{verification_1dz[1]}'].update(text_color="green")

                elif verification_1dz[0] != 1 and verification_2dz[0] == 1 and verification_3dz[0] != 1:
                    print("-=-= Resultado =-=-")
                    sleep(1.5)
                    print("Você perdeu...")
                    sleep(1)
                    print()
                    print(f"Passou longe.\nfaltou acertar a \ndezena \"{final_choice[0][0]}\" e \"{final_choice[2][0]}\"")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                    window[f'result_t{verification_2dz[1]}'].update(text_color="green")

                elif verification_1dz[0] != 1 and verification_2dz[0] != 1 and verification_3dz[0] == 1:
                    print("-=-= Resultado =-=-")
                    sleep(1.5)
                    print("Você perdeu...")
                    sleep(1)
                    print()
                    print(f"Passou longe.\nfaltou acertar a \ndezena \"{final_choice[0][0]}\" e \"{final_choice[1][0]}\"")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                    window[f'result_t{verification_3dz[1]}'].update(text_color="green")

                else:
                    print(" -=-= Resultado =-=-")
                    sleep(2)
                    print("Você Perdeu...")
                    sleep(1)
                    print()
                    print("Acabou não acertando\nnenhuma dezena.")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

            if event == "draw_8":
                window['Back'].update(disabled=True)
                window['cancel_12_w3'].update(disabled=True)
                window['cancel_13_w3'].update(disabled=True)
                window['cancel_14_w3'].update(disabled=True)
                window['draw_8'].update(disabled=True)

                final_choice = [[], [], []]
                verification_groups = [[], [], []]
                correct_numbers = [[], [], []]

                for g in full_groups:
                    if g['Name'] == value['choose_3gps_1'][1:]:
                        final_choice[0] = g['Numbers']
                    if g['Name'] == value['choose_3gps_2'][1:]:
                        final_choice[1] = g['Numbers']
                    if g['Name'] == value['choose_3gps_3'][1:]:
                        final_choice[2] = g['Numbers']

                for i, choice in enumerate(final_choice):
                    for t in all_thousands:
                        for number in choice:
                            if number == t[2:]:
                                if not verification_groups[i]:
                                    verification_groups[i] = [1, all_thousands.index(t) + 1]
                                    correct_numbers[i] = number

                total = len(verification_groups[0]) + len(verification_groups[1]) + len(verification_groups[2])

                if total == 6:
                    print("-=-= Parabéns!!! =-=-")
                    sleep(1.5)
                    print(f"Você acertou uma\ndezena de cada grupo:")
                    print(f"[\"{correct_numbers[0]}\", \"{correct_numbers[1]}\", \"{correct_numbers[2]}\"]")
                    sleep(1)
                    print()
                    print(f"Prêmio: R${int(window['zxcvb'].DisplayText[15:-3])*130},00")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                    window[f'result_t{verification_groups[0][1]}'].update(text_color="green")
                    window[f'result_t{verification_groups[1][1]}'].update(text_color="green")
                    window[f'result_t{verification_groups[2][1]}'].update(text_color="green")

                elif total == 4:
                    if len(verification_groups[0]) == 0:
                        print(" -=-= Resultado =-=-")
                        sleep(2)
                        print("Você Perdeu...")
                        sleep(1)
                        print()
                        print(f"Passou perto, só\nfaltou acertar o grupo\ndo(a) \"{value['choose_3gps_1']}\"")
                        sleep(1)
                        print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                        window[f'result_t{verification_groups[1][1]}'].update(text_color="green")
                        window[f'result_t{verification_groups[2][1]}'].update(text_color="green")

                    elif len(verification_groups[1]) == 0:
                        print(" -=-= Resultado =-=-")
                        sleep(2)
                        print("Você Perdeu...")
                        sleep(1)
                        print()
                        print(f"Passou perto, só\nfaltou acertar o grupo\ndo(a) \"{value['choose_3gps_2']}\"")
                        sleep(1)
                        print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                        window[f'result_t{verification_groups[0][1]}'].update(text_color="green")
                        window[f'result_t{verification_groups[2][1]}'].update(text_color="green")

                    elif len(verification_groups[2]) == 0:
                        print(" -=-= Resultado =-=-")
                        sleep(2)
                        print("Você Perdeu...")
                        sleep(1)
                        print()
                        print(f"Passou perto, só\nfaltou acertar o grupo\ndo(a) \"{value['choose_3gps_3']}\"")
                        sleep(1)
                        print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                        window[f'result_t{verification_groups[0][1]}'].update(text_color="green")
                        window[f'result_t{verification_groups[1][1]}'].update(text_color="green")

                elif total == 2:
                    if len(verification_groups[0]) == 2:
                        print(" -=-= Resultado =-=-")
                        sleep(2)
                        print("Passou Longe...")
                        sleep(1)
                        print()
                        print(f"Você só acertou\no grupo do(a) \"{value['choose_3gps_1']}\"")
                        sleep(1)
                        print("\nBoa Sorte da Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                        window[f'result_t{verification_groups[0][1]}'].update(text_color="green")

                    elif len(verification_groups[1]) == 2:
                        print(" -=-= Resultado =-=-")
                        sleep(2)
                        print("Passou Longe...")
                        sleep(1)
                        print()
                        print(f"Você só acertou\no grupo do(a) \"{value['choose_3gps_2']}\"")
                        sleep(1)
                        print("\nBoa Sorte da Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                        window[f'result_t{verification_groups[1][1]}'].update(text_color="green")

                    elif len(verification_groups[2]) == 2:
                        print(" -=-= Resultado =-=-")
                        sleep(2)
                        print("Passou Longe...")
                        sleep(1)
                        print()
                        print(f"Você só acertou\no grupo do(a) \"{value['choose_3gps_3']}\"")
                        sleep(1)
                        print("\nBoa Sorte da Próxima!\n-=-=-=-=-=-=-=-=-=-=-")

                        window[f'result_t{verification_groups[2][1]}'].update(text_color="green")

                else:
                    print(" -=-= Resultado =-=-")
                    sleep(2)
                    print("Você Perdeu...")
                    sleep(1)
                    print()
                    print("Acabou não acertando\nnenhum grupo.")
                    sleep(1)
                    print("\nAté a Próxima!\n-=-=-=-=-=-=-=-=-=-=-")