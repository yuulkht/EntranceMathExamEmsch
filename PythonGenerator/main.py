import random
import pandas as pd
import openpyxl

variants_1 = []
variants_2 = []
for i in range(1000):
    variants_1.append(str(random.randint(1, 9)) + "1" + str(random.randint(100, 999)))
    variants_2.append(str(random.randint(1, 9)) + "2" + str(random.randint(100, 999)))
variants_1 = list(map(lambda x: int(x), variants_1))
variants_2 = list(map(lambda x: int(x), variants_2))

df = pd.DataFrame({"Первые варианты:": variants_1, "Вторые варианты:": variants_2})

df.to_excel('Номера вариантов вступы ЭМШ.xlsx')
