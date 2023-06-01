def name():
    while True:
        input_name = input('Enter name: ')
        if input_name != 'Вячеслав':
            print('Нет такого имени')
        else:
            print('Привет, Вячеслав')
            break


name()
