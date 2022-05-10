count = int(input("Введите количество элементов списка: "))

numbers_list = []  # определяем пустой список (массив)
i = 1
while i <= count:  # в цикле добавляем элементы в массив
    element = int(input("Введите " + str(i) + " элемент: "))
    numbers_list.append(element)
    i = i + 1

numbers_list.sort() # сортируем массив по возрастанию
print("Вывод: ", numbers_list) # выводим отсортированный массив
