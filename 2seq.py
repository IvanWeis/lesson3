# вводим данные в строку:
numbers = str(input('Введите числа через "," или "/" или ";". Для завершения - Enter: '))
# преобразуем строку в массив, используя разные разделители
numbers = numbers.replace("/", ",").replace(";", ",").split(",")
print(numbers)
numbers = set(numbers)  # формируем уникальный список (без повторений)
print(list(numbers))