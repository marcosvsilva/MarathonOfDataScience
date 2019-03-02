import pandas as pd
import numpy as np
import string

number_exercise = 1


def print_exercice(arg: object = None):
    global number_exercise

    if arg is not None:
        print('exercice {}: {}'.format(number_exercise, arg))
        print('\n')

    number_exercise += 1


# Exercice 1 - Easy
# Importe Pandas e printe a versão
print_exercice(pd.__version__)

# Exercice 2 - Easy
# Crie uma série panda de cada um dos ítens abaixo: uma lista, numpy e um dicionário
list_alphabet = pd.Series([string.ascii_lowercase])
list_arange = pd.Series(range(26))s
test = list_alphabet.combine(list_alphabet, lambda x1, x2: {x1: x2})
print(test)
test = [list_arange.to_dict(),
        list_alphabet.to_dict()]
print_exercice(test)

# Exercice 3 - Easy
# Converta a série "ser" em um dataframe com seu índice como outra coluna no dataframe.
mylist = pd.Series([string.ascii_lowercase])
myarr = pd.Series(range(26))
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

# Exercice 4 - Easy
# Combine 'ser1' e 'ser2' para formar um dataframe
ser1 = pd.Series([string.ascii_lowercase])
ser2 = pd.Series(np.arange(26))

# Exercice 5 - Easy
#  Atribua um nome a série "ser" chamando-a de 'alfabeto'.
ser = pd.Series([string.ascii_lowercase])

# Exercice 1 - Medium
# Da variável 'ser', remova os ítens presentes em 'ser2'
ser1 = pd.Series(range(1, 6))
ser2 = pd.Series(range(4, 9))

# Exercice 2 - Medium
# Obtenha todos os ítens de 'ser1' e 'ser2' não comum a ambos.
ser1 = pd.Series(range(1, 6))
ser2 = pd.Series(range(4, 9))

# Exercice 3 - Medium
# Calcule o mínimo, 25º percentil, mediana, 75º e o máximo de 'ser':
ser = pd.Series(np.random.normal(10, 5, 25))

# Exercice 4 - Medium
# Da variável 'ser', matenha os 2 ítens mais frequentes como estão e substitua tod-o o resto por 'Outro'.
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

# Exercice 5 - Medium
# Coloque a série ‘ser’ em 10 decílios(decile) iguais e substitua os valores pelo nome da bandeja(bin)
ser = pd.Series(np.random.random(20))

# Exercice 1 - Hard
# Da variável 'ser' extraia palavras que contenham 2 vogais ou mais:
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])

# Exercice 2 - Hard
# Extraia emails válidos da série 'emails'. O padrão de regex para emails válidos é fornecido em 'padrao'.
emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])
padrao ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'

# Exercice 3 - Hard
# Obtenha as posições de picos(valores cercados por valores menores em ambos lados) da variável 'ser'.
ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])