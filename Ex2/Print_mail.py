import re
regex1 = "^[A-Za-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
re_com = re.compile(regex1)
a = open("a.txt", "r")
# c=a.readlines()
b = a.read()
c = b.split("\n")
for d in c:
    obj = re_com.search(d)
    #obj = re.search(r'[\w.]+\@[\w.]+', d)
    if obj:
        print(d,"Valid Email")
    else:
        print(d,"Invalid Email")