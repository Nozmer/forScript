alfa = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# aqui armazena todas as possíveis combinações
store = []

# código que vai armazenar todas as combinações de acordo com 'alfa'
for c1 in range(len(alfa)):
    store += [alfa[c1]]

    for c2 in range(len(alfa)):
        store += [alfa[c1] + alfa[c2]]
        for c3 in range(len(alfa)):
            store += [alfa[c1] + alfa[c2] + alfa[c3]]
            for c4 in range(len(alfa)):
                store += [alfa[c1] + alfa[c2] + alfa[c3] + alfa[c4]]
            
print(store)
