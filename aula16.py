# if / elif        / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"?')

if entrada == 'entrar':
    print('Você entrou no sistema')
    print('Bem vindo!')

elif entrada == 'emtrar':
    print('Você entrou no sistema')
    print('Bem vindo!')
    print('Você errou uma letra no "emtrar"')
elif entrada == 'sair': 
    print('Você saiu do sistema')

else:
    print('Você não digitou nem entrar e nem sair.')