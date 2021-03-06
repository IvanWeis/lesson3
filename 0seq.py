# 5 методов списка  (list), которые используются чаще всего :
# Частота использования методов зависит от класса решаемых задач.
# Поскольку я дальше буду применять Python для решения задач Mashine Learning,
# то я список буду скорее всего использовать как инструмент обработки числовых массивов.

# Поэтому для меня наиболее часто используемыми будут следующие функции:
# Определяем список (массив),
# содержаший объем добычи железной руды посуточно за 5 суток
iron_ore = [2000, 1700, 2100, 2200, 1900]

#   1.Индексы  (Объем добычи руды за вторые сутки)
print('За вторые сутки добыто руды: ', iron_ore[1], ' тонн')

#   2.Длина (Количество прошедших суток)
print('С начало месяца прошло ', len(iron_ore), ' суток')

#   3.Замена элемента с конкретным индексом (Исправляем объем во вторые сутки)
iron_ore[1] = 1500
print(iron_ore)

# И следующие методы:
#   1.Добавление в конец списка (Добавляем добытую руду за шестые сутки)
iron_ore.append(2300)
print('Руда, добытая посуточно в этом месяце : ', iron_ore)

#   2.Определение длины  списка (длины массива) и сохранение в переменной count
count = iron_ore.__len__()
print(count)

#   3.Удаление по индексу (Удаляем ошибочно введенные шестые сутки)
iron_ore.pop(5)
print(iron_ore)

#   4.Вставка пропущенного элемента по индексу (Вставляем пропущенные 3-и сутки)
iron_ore.insert(2, 1800)
print(iron_ore)

#   5.Очищение списка
iron_ore.clear()
print(iron_ore)

# Для строк  (str) наиболее важными методами, являются:
# friend.upper()  -  перевод в верхний регистр
# friend.lover()  -  перевод в нижний регистр
# friend.title()  -  перевод в верхний регистр первой буквы каждого слова
# friend.replace("Попов", "Иванов")  -  замена подстроки строкой
# friend.split(" ")  -  разбиение строки через разделитель (в данном случае - пробел)
# info = f'имя : {name}, возраст : {age}'  -  форматированный вывод

# Для словарей  (dict) наиболее важными методами, являются:
# friend['has_wife']= False   добавить ключь или изменить значение ключа
# del friend['has_wife']      удалить ключь
# friend.keys()     получить ключи
# friend.values()   получить значения
# friend.items      получить пары: ключь-значение (кортежи)

# Множество (set) - набор уникальных элементов
office = {'max', 'kate', 'john'}
print(office)
# Для множеств наиболее важными методами, являются:

office.add('leo') # добавление элементов
print(office)

# set(friend) приведение списка к уникальности (исключение повторяющихся элементов)

# office|freelance объединение множеств (везде)
# office&freelance пересечение множеств (одновременно и там и там)
# office - freelance исключение (только в офисе)
