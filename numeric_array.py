def multiple_of_three():
    num = input('Enter the numbers separated by a space: ')
    num_list = list(num.split(' '))
    for digit in num_list:
        digit = int(digit)
        if digit % 3 == 0:
            print(digit, end=' ')


multiple_of_three()
