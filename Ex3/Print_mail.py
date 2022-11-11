import re

# regex1 = "^[A-Za-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
regex1 = "^[A-Za-z0-9]+[\._]?\w+[@]\w+[.]\w{2,}$"
reg = re.compile(regex1)
with open("a.txt", "r") as a:
    b = a.read()
    c = re.split(r'[\n ]+', b)
    for d in c:
        obj = reg.search(d)
        # obj = re.search(r'[\w.]+\@[\w.]+', d)
        if obj:
            print(d, "Valid Email")
        else:
            print(d, "Invalid Email")
