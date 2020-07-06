class Worker(object):
    def __init__(self, name, dic):
        self.name = name
        self.dic = dic
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
        flag=True
        for i in dic:
            if dic['Name'] == key:
                flag = False
        if flag==False:
            print("Працівник: ",dic['Name'],dic['Year'],dic['Dep'],dic['Post'],dic['Exp'])
    def addWorker():
        name = input("Ім'я: ")
        year = input("Рік народження: ")
        dep = input("Відділ: ")
        post = input("Посада: ")
        exp = input("Стаж роботи: ")
        dic = {'Name':name,'Year':year,'Dep':dep,'Post':post,'Exp':exp}
        return dic
    def delWorker(name,dic,dic1,dic2):
        if name in dic['Name']:
            del dic
            return print("Працівник", name," видалений")
        if name in dic1['Name']:
            del dic1
            return print(name," видалений")
        if name in dic2['Name']:
            del dic2
            return print(name,"видалений")
        return print("Такого працівника немає!")
    
d1 = {'Name': 'Симоненко Василь', 'Year': '1935', 'Dep': 'Письменництво', 'Post': 'Поет', 'Exp': 20}
d2 = {'Name': 'Микола Хвильовий', 'Year': '1893', 'Dep': 'Письменництво', 'Post': 'Прозаїк', 'Exp': 23}
print('''Виберіть, що бажаєте зробити:
* 1 - Добавити працівника
* 2 - Найти працівника по імені
* 3 - Найти працівника по відділу і посаді
* 4 - Переглянути всіх працівників
* 5 - Видалити працівника''')
while True:
    print("Введіть команду")
    command = input()
    if command == '1':
        d3=Worker.addWorker()
    elif command == '2':
        sname=input("Введіть ім'я: ")
        Worker.searchName(sname,d1)
        Worker.searchName(sname,d2)
        Worker.searchName(sname,d3)
    elif command == '3':
        sdep=input("Введіть відділ: ")
        spost=input("Введіть посаду: ")
        Worker.searchDic(sdep,spost,d1)
        Worker.searchDic(sdep,spost,d2)
        Worker.searchDic(sdep,spost,d3)
    elif command == '4':
        print("Працівник: ",d1['Name'],d1['Year'],d1['Dep'],d1['Post'],d1['Exp'])
        print("Працівник: ",d2['Name'],d2['Year'],d2['Dep'],d2['Post'],d2['Exp'])
        print("Працівник: ",d3['Name'],d3['Year'],d3['Dep'],d3['Post'],d3['Exp'])
    elif command == '5':
        delname=input("Введіть ім'я: ")
        Worker.delWorker(delname,d1,d2,d3)
        break
    else:
        print('Невідома команда')






        
