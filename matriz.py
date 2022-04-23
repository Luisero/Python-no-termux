#mostrar uma matriz
def mostrarMatriz(mat):
    print('-'*20)
    for i in range(0,len(mat)):
        print(mat[i])
    print('-'*20)

matriz=[]
ordem = input('Digite a ordem da matriz(ex:3x2): ').split('x')
linhas =int( ordem[0])
colunas =int( ordem[1])
#declarar os numeros da matriz
for i in range(0,linhas):
    matriz.append(list())
    for j in range(0,colunas):
        num = float(input(f'Digite o elemento a {i+1},{1+j}:'))
        matriz[i].append(num)

mostrarMatriz(matriz)


matriz_transpo= []
#criar matriz transposta
for i in range(0,colunas):
    matriz_transpo.append(list())
    for j in range(0,linhas):
        matriz_transpo[i].append(matriz[j][i])
print('Matriz transposta:')
mostrarMatriz(matriz_transpo)



