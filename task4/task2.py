text=input("Введіть текст: ")
vow=0
cons=0
digit=0
for i in text:
    i.lower()
    if i in 'aeiouy':
        vow+=1
    elif i in '1234567890':
        digit+=1
    else:
        cons+=1
print("Голосні %i\nПриголосні %i\nЦифри %i" % (vow, cons,digit))
