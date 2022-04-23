nome = input('Digite seu nome')

while True:
    
    try:
        nome = int(nome)
        nome= input('Nome inválido! Tente novamente: ')

    except:
        print('Nome válido')
        break

print('Seu nome é: '+nome)


