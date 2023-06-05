orase = ["Chisinau", "Iasi", "Brasov", "Bucuresti"]
distante = [12, 150, 400, 600]

dictionar = {}
for i, item in enumerate(orase):
    dictionar[item] = distante[i]
print(dictionar)

dictionar = {}
for i, j in zip(orase, distante):
    dictionar[i] = j
print(dictionar)

dictionar = {}
for oras in orase:
    dictionar[oras] = 0

for i, k in enumerate(dictionar):
    dictionar[k] = distante[i]
print(dictionar)