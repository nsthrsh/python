f = open('file1.txt','r')
f1 = open('file2.txt','w')
d=f.readlines()
for i in d:
    if len(i)>30:
        print(i)
        f1.write(i)
f.close()
f1.close()
