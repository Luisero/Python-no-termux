carros = []
model_carro = {}
#O carro tera as seguintes chaves
#-Preco
#-Marca
#-Modelo
#-Para PCD? TRUE ou FALSE



def inputTrueFalse(texto, escolhas, erro):
    res = input(texto).lower()

    while res != escolhas[0] and res != escolhas[1]:
        print(erro)
        res = input(texto).lower()
    if res == escolhas[0]:
        return True
    else:
        return False

def printCarros(lista_carro):
    for modelo in lista_carro:
        print(f"Marca: {modelo['Marca']}")
        
    

add = True
while add:
    model_carro.clear()
    marca= input('Qual a marca do carro? ')
    modelo = input('Qual o modelo do carro? ')
    paraPCD = inputTrueFalse('Esse é para PCD? [s]sim [n]não ',['s','n'],'Valor inválido! Digite novamente. ')
    preco = float(input('Qual o preço do carro? '))

    model_carro['Marca'] = marca
    model_carro['Modelo'] = modelo
    model_carro['PCD?'] = paraPCD
    model_carro['Preco'] = preco
    carros.append(model_carro.copy())
    add = inputTrueFalse('Deseja adicionar mais carros? [s]sim [n] não', ['s','n'],'Valor inválido! Digite novamente')


printCarros(carros)




