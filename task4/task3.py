text = input("Введіть текст: ")
m=set()
for i in text:
    i.lower()
    if i in 'aeiouy':
        m.add(i)
n=list(m)
n.sort()
print(n)
