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
        newi= i+1
        newj= j+1
        if newi < newj:
            num = 2**(newi+newj)
            matriz[i].append(num)
        if newi >= newj:
            num = newi * newj
            matriz[i].append(num)

mostrarMatriz(matriz)




