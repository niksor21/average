digits = []
how = int(input('Сколько чисел вы хотите ввести? \n'))
for i in range(how):
    digits.append(int(input('Введите число: ')))
print('Среднее арифметическое:', sum(digits) / len(digits))