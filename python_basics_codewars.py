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
