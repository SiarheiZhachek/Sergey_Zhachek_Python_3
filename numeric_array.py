def multiple_of_three():
    num = input('Enter the numbers separated by a space: ')
    num_list = list(num.split(' '))
    count = 0
    for digit in num_list:
        digit = int(digit)
        if digit % 3 == 0:
            count += 1
            print(f'Numbers multiples of three: {digit}', end=' ')
    if count == 0:
        print('No numbers multiples of three.')


multiple_of_three()
