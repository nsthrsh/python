class Product:
    def __init__(self, price, model, year):
        self.price = price
        self.model = model
        self.year = year
    def print(self):
        print(self.__class__.__name__)
        print('Модель:', self.model)
        print('Ціна: ', self.price)
        print('Рік:', self.year)
    def search(arr, key):
        flag=True
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == key:
                    k=i
                    flag = False
                    for m in range(len(arr[i])):
                        print(arr[k][m],end=' ')
                    print()
        print()
        print()        

class TV(Product):
    def __init__(self, price, model, year, diag, matrix):
        Product.__init__(self, price, model, year)
        self.diag = diag
        self.matrix = matrix
    def print(self):
        super().print()
        print('Діагональ екрана: ',self.diag)
        print('Тип матриці: ',self.matrix)
        print()
 
class Phone(Product):
     def __init__(self, price, model, year, os, camera):
        Product.__init__(self, price, model, year)
        self.os = os
        self.camera = camera
     def print(self):
        super().print()
        print('Операційна система: ',self.os)
        print('Кількість камер: ',self.camera)
        print()
    
class Laptop(Product):
     def __init__(self, price, model, year, diag, proc):
        Product.__init__(self, price, model, year)
        self.diag = diag
        self.proc = proc
     def print(self):
        super().print()
        print('Діагональ екрана: ',self.diag)
        print('Тип процесора: ',self.proc)
        print()

tv1=TV(25599,'R356FH',2019,32,'LED')
tv2=TV(31099,'KH3922',2020,30,'LED')
tv3=TV(31990,'MI4252',2018,32,'TN')
arrTV=[[tv1.model,tv1.price,tv1.year,tv1.diag,tv1.matrix],
       [tv2.model,tv2.price,tv2.year,tv2.diag,tv2.matrix],
       [tv3.model,tv3.price,tv3.year,tv3.diag,tv3.matrix]]
phone1=Phone(27099,'Iphone11',2019,'IOS',2)
phone2=Phone(10099,'SAMSUNG9',2020,'Android',1)
phone3=Phone(20190,'IphoneX',2018,'IOS',2)
arrPhone=[[phone1.model,phone1.price,phone1.year,phone1.os,phone1.camera],
          [phone2.model,phone2.price,phone2.year,phone2.os,phone2.camera],
          [phone3.model,phone3.price,phone3.year,phone3.os,phone3.camera]]
laptop1=Laptop(27099,'LAT65FH',2019,32,'Intel')
laptop2=Laptop(35199,'KS3002L',2020,30,'AMD')
laptop3=Laptop(18990,'4252RXO',2018,32,'AMD')
arrLaptop=[[laptop1.model,laptop1.price,laptop1.year,laptop1.diag,laptop1.proc],
           [laptop2.model,laptop2.price,laptop2.year,laptop2.diag,laptop2.proc],
           [laptop3.model,laptop3.price,laptop3.year,laptop3.diag,laptop3.proc]]

print('''Виберіть, що бажаєте зробити:
* 1 - Вивести на екран всі телевізори
* 2 - Вивести на екран всі телефони
* 3 - Вивести на екран всі ноутбуки
* 4 - Найти телевізор по параметру
* 5 - Найти телефон по параметру
* 6 - Найти ноутбук по параметру
* 7 - Вийти''')
while True:
    print("Введіть команду")
    command = input()
    if command == '1':
        tv1.print()
        tv2.print()
        tv3.print()
    elif command == '2':
        phone1.print()
        phone2.print()
        phone3.print()
    elif command == '3':
        laptop1.print()
        laptop2.print()
        laptop3.print()
    elif command == '4':
        key1 = input("Введіть параметр для пошуку телевізора: ")
        Product.search(arrTV,key1)
    elif command == '5':
        key2 = input("Введіть параметр для пошуку телефора: ")
        Product.search(arrPhone,key2)
    elif command == '6':
        key3 = input("Введіть параметр для пошуку ноутбука: ")
        Product.search(arrLaptop,key3)
    elif command == '7':
        break
    else:
        print('Невідома команда')


