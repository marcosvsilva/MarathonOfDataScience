import pandas as pd
import numpy as np
import string
from collections import OrderedDict, defaultdict

number_exercise = 1


def print_exercice(arg: object = None):
    global number_exercise

    if arg is not None:
        print('exercice {}: {}'.format(number_exercise, arg))
        print('\n')

    number_exercise += 1


def convert_to_ordinal(value):
    if value % 100 // 10 != 1:
        if value % 10 == 1:
            ordinal = u"%d%s" % (value, "st")
        elif value % 10 == 2:
            ordinal = u"%d%s" % (value, "nd")
        elif value % 10 == 3:
            ordinal = u"%d%s" % (value, "rd")
        else:
            ordinal = u"%d%s" % (value, "th")
    else:
        ordinal = u"%d%s" % (value, "th")

    return ordinal


# Exercice 1 - Easy
# Importe Pandas e printe a versão
print_exercice(pd.__version__)

# Exercice 2 - Easy
# Crie uma série panda de cada um dos ítens abaixo: uma lista, numpy e um dicionário
alphabet = pd.Series([str(char) for char in string.ascii_lowercase])
arange = pd.Series(range(26))
relationship = pd.concat([alphabet, arange], axis=1)
print_exercice(relationship)

# Exercice 3 - Easy
# Converta a série "ser" em um dataframe com seu índice como outra coluna no dataframe.
alphabet = list('abcedfghijklmnopqrstuvwxyz')
arange = np.arange(26)
dic = dict(zip(alphabet, arange))
serie = pd.Series(dic)
dataframe = serie.to_frame()
print_exercice(dataframe)

# Exercice 4 - Easy
# Combine 'ser1' e 'ser2' para formar um dataframe
alphabet = pd.Series([str(char) for char in string.ascii_lowercase])
arange = pd.Series(len(string.ascii_lowercase))
dataframe = pd.concat([alphabet, arange], axis=1)
print_exercice(dataframe)

# Exercice 5 - Easy
#  Atribua um nome a série "ser" chamando-a de 'alfabeto'.
alphabet = pd.Series([str(char) for char in string.ascii_lowercase], name='alphabet')
print_exercice(alphabet)

# Exercice 1 - Medium
# Da variável 'ser', remova os ítens presentes em 'ser2'
ser1 = pd.Series(range(1, 6))
ser2 = pd.Series(range(4, 9))
ser1_mask = ser1.apply(lambda x: x not in ser2.values)
ser1 = ser1[ser1_mask]
print_exercice(ser1)

# Exercice 2 - Medium
# Obtenha todos os ítens de 'ser1' e 'ser2' não comum a ambos.
ser1 = pd.Series(range(1, 6))
ser2 = pd.Series(range(4, 9))
ser1_mask = ser1.apply(lambda x: x not in ser2.values)
ser2_mask = ser2.apply(lambda x: x not in ser1.values)
ser_unsual = pd.concat([ser1[ser1_mask], ser2[ser2_mask]], axis=0, ignore_index=True)
print_exercice(ser_unsual)

# Exercice 3 - Medium
# Calcule o mínimo, 25º percentil, mediana, 75º e o máximo de 'ser':
ser = pd.Series(np.random.normal(10, 5, 25))
str_result = 'min = {} \n' \
             'percentile 25 = {} \n' \
             'median = {} \n' \
             'percentile 75 = {} \n' \
             'max = {}'.format(ser.min(), ser.quantile(0.25), ser.median(), ser.quantile(0.750), ser.max())
print_exercice(str_result)

# Exercice 4 - Medium
# Da variável 'ser', matenha os 2 ítens mais frequentes como estão e substitua tod-o o resto por 'Outro'.
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
max_repeat = ser.value_counts().idxmax()
ser = ser.apply(lambda x: x == max_repeat and x or -1)
print_exercice(ser)


# Exercice 5 - Medium
# Coloque a série 'ser' em 10 decílios(decile) iguais e substitua os valores pelo nome da bandeja(bin)
ser = pd.Series(np.random.random(20))
ordered = pd.Series(ser.sort_values(ascending=True).values)

positions = ''
for i in range(5):
    positions = positions + '{}, '.format(convert_to_ordinal(ser[ser == ordered[i]].index.values+1))
cut = len(positions)-2

print_exercice(positions[1:cut])


# Exercice 1 - Hard
# Da variável 'ser' extraia palavras que contenham 2 vogais ou mais:
vowel = pd.Series(['a', 'e', 'i', 'o', 'u'])
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])
for item in ser:
    for char in item:
        #print(char)
        #print(item)
        if lower(vowel) in vowel:
            print(item)



# Exercice 2 - Hard
# Extraia emails válidos da série 'emails'. O padrão de regex para emails válidos é fornecido em 'padrao'.
emails = pd.Series(['buying books at amazom.com',
                    'rameses@egypt.com',
                    'matt@t.co',
                    'narendra@modi.com'])
regex ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'

# Exercice 3 - Hard
# Obtenha as posições de picos(valores cercados por valores menores em ambos lados) da variável 'ser'.
ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])