# # 1
# list = [2, "Hello", 5.34, True, [5, 2, 4], {"name": "Ali", "age": 20}]
#
# for i in list:
#     i_type = type(i)
#     print(f"Элемент: {i}, Тип: {i_type}")


# # 2
# elem = input("Введите элементы списка через пробел: ").split()
#
# for i in range(0, len(elem) - 1, 2):
#     elem[i], elem[i + 1] = elem[i + 1], elem[i]
#
# print("Измененный список:", ' '.join(elem))


# # 3
# months = ["январь", "февраль", "март", "апрель", "май", "июнь",
#           "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
#
# seasons_dict = {
#     "зима": [1, 2, 12],
#     "весна": [3, 4, 5],
#     "лето": [6, 7, 8],
#     "осень": [9, 10, 11]
# }
#
# month_num = int(input("Введите номер месяца (от 1 до 12): "))
#
# for season, month_list in seasons_dict.items():
#     if month_num in month_list:
#         print(f"Месяц {months[month_num - 1]} сезон года {season}.")
#         break
# else:
#     print("Ошибка!")


# # 4
# string = input("Введите предложение: ")
#
# words = string.split()
#
# for i, word in enumerate(words, start=1):
#     s_word = word[:10] if len(word) > 10 else word
#     print(f"{i}: {s_word}")


# # 5
# list = [8, 7, 5, 4, 4, 2]
#
# new = float(input("Введите новый элемент: "))
#
# element = False
# for i in range(len(list)):
#     if new >= list[i]:
#         list.insert(i, new)
#         element = True
#         break
#
# if not element:
#     list.append(new)
#
# print("Обновленный рейтинг:", list)


# 6
products = []

while True:
    name = input("Введите название товара (или '1' для завершения ввода): ")
    if name.lower() == "1":
        break

    tovar = float(input("Введите цену: "))
    colvo = int(input("Введите количество: "))
    izmerenie = input("Введите ед. измерения: ")

    product = {
        "название": name,
        "цена": tovar,
        "количество": colvo,
        "ед": izmerenie
    }
    products.append((len(products) + 1, product))

analyz = {}
for product in products:
    for key, sena in product[1].items():
        if key not in analyz:
            analyz[key] = [sena]
        else:
            analyz[key].append(sena)

print("Аналитика о товарах:")
for key, sena in analyz.items():
    print(f"{key}: {list(set(sena))}")