import os
fname='students.txt'
print('''Виберіть, що бажаєте зробити:
* 1 - Записати у файл
* 2 - Зчитати файл
* 3 - Дозаписати у файл
* 4 - Знайти файл у каталозі
* 5 - Знайти дані у файлі
* 6 - Посортувати дані у файлі
* 7 - Вийти''')
while True:
    print("\nВведіть команду")
    command = input()
    if command == '1':
        text=input("Введіть текст, який бажаєте записати у файл: ")
        f = open(fname, "w")
        f.write(text)
        f.close()
    elif command == '2':
        file = open(fname, 'r')
        print('File ' + fname + ':')
        for line in file:
            print(line, end='')
        file.close() 
    elif command == '3':
        text=input("Введіть текст, який бажаєте дозаписати у файл: ")
        f = open(fname, "a")
        f.write('\n')
        f.write(text)
        f.close() 
    elif command == '4':
        flag=False
        folder=input("Введіть шлях до каталогу, у якому бажаєте шукати файл: ")
        for d, dirs, files in os.walk(folder):
            for f in files:
                if f==fname:
                    flag=True
                    path = os.path.join(d,f)
        if flag == True:
            print("Файл є у каталозі "+path)
        else:
            print("Файлу у каталозі немає "+folder)
    elif command == '5':
        word=input("Введіть слово, що шукаєте: ")
        file = open(fname, 'r')
        for line in file:
            if word in line:
                print(line, end='')
    elif command == '6':
        f = open(fname,'r+')
        d=f.readlines()
        d.sort(key=lambda x: float(x.split(" - ")[1]),reverse = True)
        f.seek(0)
        f.write("".join(d))
        print("Файл посортовано.")
        f.close() 
    elif command == '7':
        break
    else:
        print('Невідома команда')
