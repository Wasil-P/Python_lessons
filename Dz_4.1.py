# 4*
# Ввести строку (считаем, что в начале и в конце строки нет пробелов,
# все слова в строке разделены одним пробелом). Для введенной строки
# изменить порядок символов в каждом слове в предложении,
# сохраняя при этом пробелы и первоначальный порядок слов.
# Примеры:
# "Hello World!" -> "olleH !dlroW"
# "Let's see, how it works" -> "s'teL ,ees woh ti skrow"

# 4.1
# string_user = input('Введите строку: ')
# words = list(string_user)
# n = len(words) - 1
# new_words = ""
# for letter in words:
#     if n >= 0:
#         new_words += words[n]
#         n = n - 1
# new_words2 = new_words.split()
# n = len(new_words2) - 1
# finish_words = ""
# for letter in new_words2:
#     if n >= 0:
#         finish_words += f'{new_words2[n]} '
#         n = n - 1
# print(finish_words)

# 4.2
string_user = input('Введите строку: ')
words = len(string_user)
new_words = string_user[words::-1]
print(new_words)
new_words2 = new_words.split()
words_new = len(new_words2)
finish_words = new_words2[words_new::-1]
print(' '.join(finish_words))
