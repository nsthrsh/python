import os.path

def read_file(fname):
 """Функція для зчитування файла fname
 та виведення його вмісту на екран"""
 file = open(fname, 'r') # відкриття файлу для зчитування
 print('File ' + fname + ':') # виведення назви файлу
 # зчитування вмісту файла по рядках
 for line in file:
     print(line, end='') # виведення рядка s
 file.close() # закриття файлу
if __name__ == '__main__':
 # функція os.path.join з'єднує частини шляху у файловій системі
 # необхідним роздільником
 read_file(os.path.join('data', 'example01.txt'))
