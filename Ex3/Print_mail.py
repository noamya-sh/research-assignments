import re


def print_mail(path):
    reg = re.compile(r'^\w+([._-]\w+)?@(\w+[.-])+\w{2,}$')
    with open(path, "r") as file:
        splited = re.split(r'[\n\t\r ]+', file.read())
        valid = []
        inValid = []
        for adress in splited:
            mail = reg.search(adress)
            if mail:
                valid.append(adress)
            else:
                inValid.append(adress)
        print("valid email: ", valid)
        print("invalid email: ", inValid)


print_mail("a.txt")
