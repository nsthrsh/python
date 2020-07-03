word = input("Введіть слово: ")
print(list(filter(lambda x : word.count(x) > 1 , set(word)) ))
