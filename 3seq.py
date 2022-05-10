numbers1 = str(input('Введите Первый список чисел через запятую. Для завершения - Enter: '))
numbers2 = str(input('Введите Второй список чисел через запятую. Для завершения - Enter: '))
numbers1 = numbers1.split(",")
numbers1 = set(numbers1)
numbers2 = numbers2.split(",")
numbers2 = set(numbers2)
numbers = numbers1 - numbers2
print(numbers)