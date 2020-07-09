import os.path # Модуль, який містить функції для роботи з
#шляхом у файловій системі
text = '''Hello!
I am a text file. And I had been written with a Python
script
before you opened me, so look up the docs and try to delete
me using Python, too.'''

def write_text_to_file(filename, text):
 """Функція для запису у файл filename рядка text"""
 f = open(filename, "w") # відкриття файла для запису
 f.write(text) # Запис рядка text у файл
 f.close() # Закриття файлу
if __name__ == '__main__':
    write_text_to_file(os.path.join('data','example01.txt'), text)
