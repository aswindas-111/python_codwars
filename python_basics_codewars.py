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



# POWERS OF 2 UPTO N(0-N):
def powers_of_two(n):
    return [2**i for i in range(n+1)]

print(powers_of_two(1))



# WHEN PROVIDED WITH A LETTER, RETURN ITS POSITION IN THE ALPHABET.
def position(alphabet):
    return "Position of alphabet: %s" % ("abcdefghijklmnopqrstuvwxyz".find(alphabet) + 1)

print(position("v"))



# You get an array of numbers, return the sum of all of the positives ones.
def positive_sum(arr):
    sum_positive = 0
    for num in arr:
        if num > 0:
            sum_positive += num
    return sum_positive


# Calculate the multiplication and sum of two numbers
'''Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.'''
def mul_or_sum(a,b):
    if a*b < 1000:
        print(a*b)
    else:
        print(a+b)

mul_or_sum(30,20)



# Printing current and previous number and their sum in a range(a)
def problem(a):
    pre_num = 0
    for i in range(a+1):
        print(f"current number",i,"prev_number",pre_num,"sum: ",pre_num+i)
        pre_num=i
problem(10)


# given triangle od odd numbers , return sum of each row
def row_sum_odd_numbers(n):
    return n ** 3



# Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).
# Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).
def hello(name=None):
    if not name:
        return 'Hello, World!'
    elif name=='':
        return 'Hello, World!'
    elif name:
        name.lower()
        return f'Hello, {name.capitalize()}!' 
    return




# Define a function that removes duplicates from an array of non negative numbers and returns it as a result.
def distinct(seq):
    seen = set()
    result = []
    
    for element in seq:
        if element not in seen:
            result.append(element)
            seen.add(element)
    
    return result



# Your code will determine if the number passed is even (or not).
# The function needs to return either a true or false.
def is_even(n): 
    if n%2 == 0:
        return True
    else:
        return False
    


# Build a function that returns an array of integers from n to 1 where n>0.
def reverse_seq(n):
    return list(range(n, 0, -1)) 



# Converting binari number into decimal number.
def bin_to_decimal(inp):
    return int(inp, 2)


# Return the number (count) of vowels in the given string.
def get_count(sentence):
    return sum([sentence.count(vowels) for vowels in "aeiou"])