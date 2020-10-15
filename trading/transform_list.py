import numpy as np

cotations = np.genfromtxt('cotations.txt', delimiter= ',')

print(cotations)

converted_cotations = np.zeros((len(cotations), 10))

for i in range(len(cotations)-9):
    for j in range(10):
        converted_cotations[i][j] = cotations[j + i][0]



print(converted_cotations)
# converted_cotations.to_csv("converted_cotations.csv")