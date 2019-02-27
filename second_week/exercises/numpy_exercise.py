import numpy as np

number_exercise = 1


def print_exercice(arg: object = None):
    global number_exercise

    if arg is not None:
        print('exercice {}: {}'.format(number_exercise, arg))
        print('\n')

    number_exercise += 1


def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

# Exercice 1 - Easy
# Importe numpy como 'np' e imprima o número da versão.
print_exercice(np.version.version)

# Exercice 2 - Easy
# Crie uma matriz 1D com números de 0 a 9
arr = np.arange(10)
print_exercice(arr)

# Exercice 3 - Easy
# Crie uma matriz booleana numpy 3×3 com 'True'
arr = np.repeat(True, 3*3).reshape(3, -1)
print_exercice(arr)

# Exercice 4 - Easy
# Extraia todos os números ímpares de 'arr'
arr = np.arange(10)
arr_mask = arr % 2 > 0
print_exercice(arr[arr_mask])

# Exercice 5 - Easy
# Substitua todos os números ímpares arr por -1
arr = np.arange(10)
arr[arr_mask] = -1
print_exercice(arr)

# Exercice 1 - Medium
# Substitua todos os números ímpares em arr com -1 sem alterar arr
arr = np.arange(10)
print_exercice()

# Exercice 2 - Medium
# Converta uma matriz 1D para uma matriz 2D com 2 linhas
arr = np.arange(10)
arr = arr.reshape(2, -1)
print_exercice(arr)

# Exercice 3 - Medium
# Empilhe matrizes verticalmente
matrix_a = np.arange(10).reshape(2, -1)
matrix_b = np.repeat(1, 10).reshape(2, -1)
matrix_merge = np.append(matrix_a, matrix_b, axis=0)
print_exercice(matrix_merge)

# Exercice 4 - Medium
# Empilhe as matrizes horizontalmente
matrix_a = np.arange(10).reshape(2, -1)
matrix_b = np.repeat(1, 10).reshape(2, -1)
matrix_merge = np.append(matrix_a, matrix_b, axis=1)
print_exercice(matrix_merge)

# Exercice 5 - Medium
# Crie o seguinte padrão sem codificação, usando apenas funções numpy e a matriz de entrada abaixo 'a'.
arr = np.arange(1, 4, 1)
arr_out = arr.repeat(3)
for i in range(len(arr)):
    arr_out = np.append(arr_out, arr)
print_exercice(arr_out)


# Dataset para exercícios hard.
url = 'dataset/iris.csv'

# Exercice 1 - Hard
# Calcule a pontuação softmax de 'sepal length':
iris = np.genfromtxt(url, delimiter=',', usecols=[0, 1, 2, 3], skip_header=1)
print_exercice(softmax(iris[:, 1]))

# Exercice 2 - Hard
# Filtre as linhas de iris_2d que possuem petallength (coluna 3) > 1.5 e sepallength (coluna 1) < 5.0


# Exercice 3 - Hard
# Selecione as linhas de iris_2d que não têm nenhum valor 'nan'


# Exercice 1 - Hard
# Calcule as contagens de valores únicos na linha.
np.random.seed(100)
arr = np.random.randint(1, 11, size=(6, 10))


# Exercice 2 - Hard
# Encontre todos os picos em uma matriz 1D numpy 'a'. Picos são pontos cercados por valores menores em ambos os lados.
a = np.array([1, 3, 7, 1, 2, 6, 0, 1])


# Exercice 3 - Hard
# Calcule as codificações únicas (variáveis ​​binárias dummy para cada valor único na matriz)
np.random.seed(101)
arr = np.random.randint(1, 4, size=6)
