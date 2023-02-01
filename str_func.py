#функция для всех больших букв
def big_alfabet():
    a = str(input())
    return print(f'{a.upper()}')

big_alfabet()

#функция для всех первых больших букв
def big_alfabet_first():
    a = str(input())
    return print(f'{a.title()}')

big_alfabet_first()