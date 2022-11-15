import doctest
import re


def print_mail(path):
    """
    Get a file with addresses and check if they are valid email addresses.
    >>> print_mail("prefix_mail_test.txt")
    valid email:  ['a@gmail.com', 'a-a@gmail.com', 'adf34@gmail.com', 'a_a@gmail.com', 'gt5-56@gmail.com', 'Ahron@gmail.com', 'r.r@gmail.com', 'rtret_56@gmail.com']
    invalid email:  ['ad%f34@gmail.com', 'levi%@gmail.com', 'ghg-@gmail.com', 'levi%@gmail.com', 'fg..tr@gmail.com', 'fg_.tr@gmail.com']
    >>> print_mail("domain_mail_test.txt")
    valid email:  ['aryeh@gmail76.com', 'aryeh@re.re.re.re', 'aryeh@tr-tr.com', 'aryeh@gmail.com.il']
    invalid email:  ['aryeh@re', 'aryeh@re.87', 'aryeh@gmail..com', 'aryeh@-tr.com', 'aryeh@gma%il.com', 'aryeh@gmail.c']
    >>> print_mail("official_test.txt")
    valid email:  ['abc-d@mail.com', 'abc.def@mail.com', 'abc@mail.com', 'abc_def@mail.com', 'abc.def@mail.cc', 'abc.def@mail-archive.com', 'abc.def@mail.org', 'abc.def@mail.com']
    invalid email:  ['abc-@mail.com', 'abc..def@mail.com', '.abc@mail.com', 'abc#def@mail.com', 'abc.def@mail.c', 'abc.def@mail#archive.com', 'abc.def@mail', 'abc.def@mail..com']
    """
    # regular expression for valid email adress
    reg = re.compile(r'^[A-Za-z0-9]+([._-]?[A-Za-z0-9]+)*@([A-Za-z0-9]+[.-])+[A-Za-z]{2,}$')
    # open file for read
    with open(path, "r") as file:
        splited = re.split(r'[\n\t\r ]+', file.read())
        valid = []
        inValid = []

        for adress in splited:
            # if adress match to regular expression
            mail = reg.search(adress)
            if mail:
                valid.append(adress)
            else:
                inValid.append(adress)
        print("valid email: ", valid)
        print("invalid email: ", inValid)


if __name__ == '__main__':
     doctest.testmod()