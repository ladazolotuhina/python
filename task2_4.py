#Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_str = input('Введите любое предложение: ')
get_str = user_str.split()
for number, word in enumerate(get_str):
    print(f'№ {number} - {word[0:10]}')
print('END')


