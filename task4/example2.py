phonebook = {
'Олександр': '123-032-846',
'Анатолій': '432-917-333',
'Вадим': '345-120-422',
'Андрій': '111-890-532', # остання кома ігнорується
}
# len(d) – кількість елементів
print(phonebook, '\n', len(phonebook), 'entries found')

#d[key] – отримання значення з ключем key. Якщо ключ не
#існує, відображення реалізує спеціальний метод missing
#(self, key): якщо ключ не існує і метод missing не
#визначений, видається виняток KeyError
print(phonebook['Вадим']) # 345-120-422
print(phonebook['Олег']) # KeyError: 'Олег'

#d[key]=value – змінити значення або створити пару ключзначення,
#якщо ключ не існує
phonebook['Андрій'] = '222-890-532'
phonebook['Олег'] = '432-850-133'
print(phonebook, '\n', len(phonebook), 'entries found')

#key in d, key not in d – перевірка наявності ключа в
#відображенні
for person in ('Анатолій', 'Вадим', 'Микола'):
    if person in phonebook:
        print(person, 'is in the phonebook')
    else:
        print('No entry found for', person)
