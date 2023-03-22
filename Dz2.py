
def my_friends(name):
    friends = {'Egor', 'Liza', 'Vanya', 'Yana'}
    if name in friends:
        return "У меня есть друг " + name
    else:
        return "У меня нет друга с именем " + name

print(my_friends('Liza'))
print(my_friends('Georg'))