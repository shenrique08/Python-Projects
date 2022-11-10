from random import randint
idioma = int(input(''
                   '[1] Portuguese\n'
                   '[2] English \n'
                   'Enter the language which you would like to play: '))
if idioma == 2:
    print('=' * 56)
    print("        Hello, Human! Let's play even or odd ?")
    print('The rule is simple. Who scores 3 times is the big winner.')
    print('=' * 56)
    sum_computer = 0
    sum_player = 0
    name = str(input('First, tell me your name: ')).upper()
    
    while True:
        even_or_odd = str(input('Even or odd? [E/O] ')).upper()
        player = int(input('Tell me a number: '))
        computer = randint(0, 10)
        if (player + computer) % 2 == 0:
            print(f'You played [{player}] and I played [{computer}]. The sum of them is [{player + computer}]')
            print("So it's EVEN")
            if even_or_odd == 'E':
                sum_player += 1
            elif even_or_odd == 'O':
                sum_computer += 1
        else:
            print(f'You played [{player}] and I played [{computer}]. The sum of them is [{player + computer}]')
            print("So it's ODD")
            if even_or_odd == 'E':
                sum_computer += 1
            elif even_or_odd == 'O':
                sum_player += 1
        if sum_player == 3:
            print(f'Congratulation, Human {name}. You are really good at this')
            print(f'FINAL SCORE: {name} [{sum_player}] X [{sum_computer}] COMPUTER')
            break
        elif sum_computer == 3:
            print(f'Sorry, Human {name}. You were not able to beat me. Try it another time!')
            print(f'SCORE: {name} [{sum_player}] X [{sum_computer}] COMPUTER')
            break
        print(f'FINAL SCORE: {name} [{sum_player}] X [{sum_computer}] COMPUTER')
    print('END')
elif idioma == 1:
    print('=' * 60)
    print("        Olá, Humano. Vamos jogar par ou ímpar ?")
    print('A regra é simples. Quem pontuar 3 vezes é o grande vencedor.')
    print('=' * 60)
    sum_computer = 0
    sum_player = 0
    name = str(input('Primeiro, diga-me seu nome: ')).upper()
    while True:
        even_or_odd = str(input('Par ou ímpar? [P/I] ')).upper()
        player = int(input('Me diz um valor: '))
        computer = randint(0, 10)
        if (player + computer) % 2 == 0:
            print(f'Você jogou [{player}] e eu joguei [{computer}]. A soma é [{player + computer}]')
            print("Então deu PAR")
            if even_or_odd == 'P':
                sum_player += 1
            elif even_or_odd == 'I':
                sum_computer += 1
        else:
            print(f'Você jogou [{player}] e eu joguei [{computer}]. A soma é [{player + computer}]')
            print("Então deu ÍMPAR")
            if even_or_odd == 'P':
                sum_computer += 1
            elif even_or_odd == 'I':
                sum_player += 1
        if sum_player == 3:
            print(f'Parabéns, Humano {name}. Você é muito bom nisso!')
            print(f'PLACAR FINAL: {name} [{sum_player}] X [{sum_computer}] COMPUTADOR')
            break
        elif sum_computer == 3:
            print(f'Desculpe, Humano {name}. Você não conseguiu ganhar de mim. Tente novamente!')
            print(f'SCORE: {name} [{sum_player}] X [{sum_computer}] COMPUTADOR')
            break
        print(f'PLACAR FINAL: {name} [{sum_player}] X [{sum_computer}] COMPUTADOR')
    print('FIM')
else:
    print('Please, type a valid option!')
    idioma = int(input(''
                       '[1] Portuguese\n'
                       '[2] English \n'
                       'Enter the language which you would like to play: '))
