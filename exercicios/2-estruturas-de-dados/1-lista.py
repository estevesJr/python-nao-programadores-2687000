# Crie uma lista apenas com elementos numéricos
Lista_numeros = [1, 1, 2, 3, 5, 8, 13, 21]
print (Lista_numeros)
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
Lista_mista = [1, "string", 3.1417, "14-08-1981", True, "string2"]
print (Lista_mista)
# Imprima na tela apenas os 5 primeiros elementos da lista
print (Lista_mista[0:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
print (Lista_mista[0:5:2])
# Remova da lista o último item
Lista_mista.pop()

# Insira na lista um novo item
Lista_mista.append ("novo item")
print (Lista_mista)
# Remova da lista um item específico
Lista_mista.remove ("novo item")
print (Lista_mista)