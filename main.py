alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# aqui armazena todas as possíveis combinações
store = []

# código que vai armazenar todas as combinações de acordo com 'alfa'
for c1 in range(len(alfa)):
    for c2 in range(len(alfa)):
        for c3 in range(len(alfa)):
            for c4 in range(len(alfa)):
                for c5 in range(len(alfa)):
                    for c6 in range(len(alfa)):
                        for c7 in range(len(alfa)):
                            for c8 in range(len(alfa)):
                                if c1 < 1 and c2 < 1 and c3 < 1 and c4 < 1 and c5 < 1 and c6 < 1 and c7 < 1:
                                    store += [alfa[c8]]
                                    print(alfa[c8])

                                elif c1 < 1 and c2 < 1 and c3 < 1 and c4 < 1 and c5 < 1 and c6 < 1:
                                    store += [alfa[c7] + alfa[c8]]
                                    print(alfa[c7] + alfa[c8])

                                elif c1 < 1 and c2 < 1 and c3 < 1 and c4 < 1 and c5 < 1:
                                    store += [alfa[c6] + alfa[c7] + alfa[c8]]
                                    print(alfa[c6] + alfa[c7] + alfa[c8])

                                elif c1 < 1 and c2 < 1 and c3 < 1 and c4 < 1:
                                    store += [alfa[c5] + alfa[c6] + alfa[c7] + alfa[c8]]
                                    print(alfa[c5] + alfa[c6] + alfa[c7] + alfa[c8])

                                elif c1 < 1 and c2 < 1 and c3 < 1:
                                    store += [alfa[c4] + alfa[c5] + alfa[c6] + alfa[c7] + alfa[c8]]
                                    print(alfa[c4] + alfa[c5] + alfa[c6] + alfa[c7] + alfa[c8])

                                elif c1 < 1 and c2 < 1:
                                    store += [alfa[c3] + alfa[c4] + alfa[c5] + alfa[c6] + alfa[c7] + alfa[c8]]
                                    print(alfa[c3] + alfa[c4] + alfa[c5] + alfa[c6] + alfa[c7] + alfa[c8])

                                elif c1 < 1:
                                    store += [alfa[c2] + alfa[c3] + alfa[c4] + alfa[c5] + alfa[c6] + alfa[c7] + alfa[c8]]
                                    print(alfa[c2] + alfa[c3] + alfa[c4] + alfa[c5] + alfa[c6] + alfa[c7] + alfa[c8])

                                else:
                                    store += [alfa[c1] + alfa[c2] + alfa[c3] + alfa[c4] + alfa[c5] + alfa[c6] + alfa[c7] + alfa[c8]]
                                    print(alfa[c1] + alfa[c2] + alfa[c3] + alfa[c4] + alfa[c5] + alfa[c6] + alfa[c7] + alfa[c8])
