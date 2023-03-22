# 2. Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные. Создать
# файл и записать в него первые 2 строки и закрыть файл. Затем открыть файл на
# редактирование и дозаписать оставшиеся 2 строки. В итогом файле должны быть 4
# строки, каждая из которых должна начинаться с новой строки.
# text_1 = "True\n"
# text_2 = "False\n"
# num_1 = "6\n"
# num_2 = "15\n"
#
# with open("my_text.txt", "w") as file:
#     file.write(text_1)
#     file.write(text_2)
#
# with open("my_text.txt", "a") as file:
#     file.write(num_1)
#     file.write(num_2)

# 3. Создать словарь в качестве ключа которого будет 6-ти значное число (id), а в
# качестве значений кортеж состоящий из 2-х элементов - имя(str), возраст(int).
# Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл.

dicti = {236509: ("Luke Skywalker", 25), 213476: ("Anakin Skywalker", 60), 932412: ("Han Solo", 34),
         324157: ("Leia Organa", 28), 380121: ("Obi-Wan Kenobi", 57)}
#
import json
#
with open("Star Wars.json", "w") as json_file:
    data = json.dump(dicti, json_file, indent= 4)

# 4. Прочитать сохранённый json-файл и записать данные на диск в сvs-файл, первой
# строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.

import csv
import random
with open("Star Wars.json") as json_file:
    json_dict = json.load(json_file)
    json_str = json.dumps(json_dict)
    json_list = json.loads(json_str)

list_ = ['id','name','age','телефон']
with open("Star Wars.csv", "w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(list_)
    for key in json_list:
        csv_data = []
        csv_data += [key] + json_list[key] + [random.randint(111111, 999999)]
        csv_writer.writerow(csv_data)






