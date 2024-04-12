try:
    print('Ola Mundo!')
except FileNotFoundError as e:
    print(f'Erro ao encontrar conquista:{e}')
except Exception as e:
    print(f'Ocorreu um erro inesperado:{e}')