import sqlite3
# Клас для що описує працівників підприємства
class Worker():
 def __init__(self, **kwargs):
     self.name = kwargs.get('name')
     self.position = kwargs.get('position')
     self.work_from_date = kwargs.get('work_from_date')
     self.birth_date = kwargs.get('birth_date')
 def get_data(self):
     return self.name, self.position, self.work_from_date, self.birth_date

# створення екземпляра класу працівник з використанням
#непозиційних параметрів у конструкторі
w1 = Worker(name='Petrov Vadym', position='manager',
work_from_date='09-12-2019', birth_date='18-02-1990')
conn = sqlite3.connect("staff_db.db")
cursor = conn.cursor()
# Створення таблиці після першого запуску скрипта потрібно
#закоментувати
cursor.execute("""CREATE TABLE staff
 (name text, position text, work_from_date
text,
 birth_date text)
 """)
# Створення першого запису в таблиці "вручну"
cursor.execute("""INSERT INTO staff
 VALUES ('Ivanov Ivan', 'director', '07-10-
2019',
 '2-12-1980')"""
 )
# Створення першого запису в таблиці із екземпляра класу Worker
cursor.execute("""INSERT INTO staff
 VALUES (?,?,?,?)""", w1.get_data()
 )
# Зберігаємо зміни
conn.commit()
# Вставляємо список з трьох працівників
all_workers = [('Borysov Mykola', 'ingeneer', '23-11-1976',
'04-12-2019'),
 ('Pavlyik Inna', 'secretary', '12-09-1991',
'22-01-2020'),
 ('Kolodych Leonid', 'ingeneer', '16-08-1986',
'13-01-2020')]
cursor.executemany("INSERT INTO staff VALUES (?,?,?,?)",all_workers)
conn.commit()
# Виведення на екран всіх записів

# Вставляємо список з трьох працівників
all_workers1 = [('Borys Petro', 'ingeneer', '30-12-1976',
'04-12-2019'),
 ('Kholidiuk Anna', 'secretary', '13-02-1991',
'22-01-2020'),
 ('Petrov Leonid', 'ingeneer', '18-08-1986',
'13-01-2020')]
cursor.executemany("INSERT INTO staff VALUES (?,?,?,?)",all_workers1)
conn.commit()
# Виведення на екран всіх записів

print("Записи в таблиці бази даних у вигляі списка:")
sql = "SELECT * FROM staff"
cursor.execute(sql)
print(cursor.fetchall())
# Редагування запису для конкретного працівника
sql = """
UPDATE staff
SET position = 'main ingeneer'
WHERE name = 'Kolodych Leonid'
"""
cursor.execute(sql)
conn.commit()
# Виводимо список всіх інженерів
print("Список всіх ingeneer:")
sql = "SELECT * FROM staff WHERE position=?"
cursor.execute(sql, [("ingeneer")])
print(cursor.fetchall())
# Виведення на екран всіх записів
print("Список всіх записів в таблиці:")
for row in cursor.execute("SELECT rowid, * FROM staff ORDER BY name"):
 print(row)
