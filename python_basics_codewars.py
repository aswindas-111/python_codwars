# ISOGRAM:
def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True

print(is_isogram("asdef"))



# MULTIPLICATION TABLE:
def table(n):
    for i in range(1,11):
        print(i,"*",n,"=",i*n)
num=int(input("enter the number : "))
table(num)


# SUM OF DIGITS:
def sum_digits(number):
    return sum(int(i) for i in str(number) if i.isdigit())

print(sum_digits(22))


# CONVERT_ALL_INTO_UPPERCASE:
def convert_all_into_uppercase(string):
    return string.upper()

print(convert_all_into_uppercase("Create a method to see whether the string is ALL CAPS."))



# CREATE A METHOD TO SEE WHETHER THE STRING IS ALL CAPS:
def is_uppercase(inp):
    return inp.upper()==inp


