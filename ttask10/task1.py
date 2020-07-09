from sqlite3 import *

connection = connect('workers.db')
cursor = connection.cursor()

class Worker(object):
    def __init__(self, name, dic):
        self.name = name
        self.dic = dic
        
#def startDataBase():
 #   cursor.execute("CREATE TABLE workers (name text, year text, dep text, post text, exp text)")

def searchDic(key,key1,dic):
    flag=True
    for i in dic:
        if dic['Dep'] == key:
            for j in dic:
                if dic['Post']==key1:
                    flag = False
    if flag==False:
        print("Працівник: ",dic['Name'],dic['Year'],dic['Dep'],dic['Post'],dic['Exp'])
def searchName(key,dic):
    cursor.execute("SELECT * FROM workers WHERE name=?",[(key)])
    name = cursor.fetchall()
    print(name[0])
    flag=True
    for i in dic:
        if dic['Name'] == key:
            flag = False
    if flag==False:
        print("Працівник: ",dic['Name'],dic['Year'],dic['Dep'],dic['Post'],dic['Exp'])
def addWorker():
    connection.commit()
    name = input("Ім'я: ")
    year = input("Рік народження: ")
    dep = input("Відділ: ")
    post = input("Посада: ")
    exp = input("Стаж роботи: ")
    dic = {'Name':name,'Year':year,'Dep':dep,'Post':post,'Exp':exp}
    l =(name,year,dep,post,exp)
    cursor.execute("""INSERT INTO workers VALUES (?,?,?,?,?)""",l)
    connection.commit()
    return dic
def delWorker(name,dic,dic1):
    cursor.execute("DELETE FROM workers WHERE name=?",[(name)])
    connection.commit()
    if name in dic['Name']:
        del dic
        return print("Працівник", name," видалений")
    if name in dic1['Name']:
        del dic1
        return print(name," видалений")
    
d1 = {'Name': 'Симоненко Василь', 'Year': '1935', 'Dep': 'Письменництво', 'Post': 'Поет', 'Exp': 20}
d2 = {'Name': 'Микола Хвильовий', 'Year': '1893', 'Dep': 'Письменництво', 'Post': 'Прозаїк', 'Exp': 23}
print('''Виберіть, що бажаєте зробити:
* 1 - Добавити працівника
* 2 - Найти працівника по імені
* 3 - Найти працівника по відділу і посаді
* 4 - Переглянути всіх працівників
* 5 - Видалити працівника
* 6 - Переглянути базу даних
* 7 - Вийти''')
while True:
    #startDataBase()
    print("Введіть команду")
    command = input()
    if command == '1':
        d3=addWorker()
    elif command == '2':
        sname=input("Введіть ім'я: ")
        searchName(sname,d1)
    elif command == '3':
        sdep=input("Введіть відділ: ")
        spost=input("Введіть посаду: ")
        searchDic(sdep,spost,d1)
    elif command == '4':
        print("Працівник: ",d1['Name'],d1['Year'],d1['Dep'],d1['Post'],d1['Exp'])
        print("Працівник: ",d2['Name'],d2['Year'],d2['Dep'],d2['Post'],d2['Exp'])
    elif command == '5':
        delname=input("Введіть ім'я: ")
        delWorker(delname,d1,d2)
    elif command == '6':
        print("Список всіх записів в таблиці:")
        for row in cursor.execute("SELECT * FROM workers ORDER BY name"):
            print(row)
    elif command == '7':
        break
    else:
        print('Невідома команда')
