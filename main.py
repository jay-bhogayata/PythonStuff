print("Hello, world")

# variable and assignment
a = 25
b = 56
c = a + b
print(c)

print(10 + 58)

"""
python code execute line by line.
syntax error in prog lang
this is doc string comment
"""

print("avg", (10+20+30)/3)

n1 = 10
n1 = 20
n1 += 50
print(n1)

# + , - , * , %
# python use snack_case naming for var

s1 = 'jay'
s2 = "jay"

n2 = 10
n3 = -10

f1 = 10.56
f2 = -10.6

is_login = True
is_coder = False


# f string
name = "jay"
print(f"My name is {name}")

# None type variable
empty = None
print(type(empty))

# "None" and None is different

# python is dynamic type language


first_name = "Jay "
last_name = "Bhogayata"
full_name = first_name + last_name
print(f"full name is {full_name}")

l1, l2 = "Python", "Go"

# function


def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result


ans = area_of_circle(50)
print(ans)


def sum(a, b):
    return a + b


print(sum(1, 2))


def to_celsius(f):
    return round((5/9) * (f - 32), 3)


print(to_celsius(10))


def hour_to_sec(h):
    print(h * 60 * 60)


hour_to_sec(10)

# args vs params in function
# function vs methods

# When no return value is specified in a function.
# it will automatically return None


def Test():
    print("A")

# multiple return


def get_user_info():
    return "Jay", 21, "jayj33303@gmail.com"


name, age, email = get_user_info()
print(name, age, email)

# parameter when defining the function and arg when calling

# default value


def print_info(name, country="INDIA"):
    print(f"{name} is from {country}")


print_info("Jay")
print_info("John", "USA")

# 50% of 899 is 899 * 0.5

# in python variable is function scoped
# wired example


def print_nums():
    nums = [1, 2, 3, 4, 5]
    for i in nums:
        print(i)
    print(i)  # this will print 5


print_nums()

# The pass keyword is a way to tell Python to do nothing.

# Computing
print(10+2)
print(10-2)
print(10*3)
print(10/3)
print(10//3)
print(10 % 3)
print(2**3)

# += , -= , *= , /= , //= , %=  , **=
# Numerics : Integers and floats

print(10e3)

# we can use _ for readability
t = 10_000
print(t)


# logical and or not
print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(not True)

# binary numbers 0bxxxx
print(0b1101)


# bitwise & and |
print(5 & 7)
# 0101 & 0111
print(5 | 7)
# 0101 | 0111

# str to bin a = int( s1 , 2 )

# comparision operators (<,>,<=,>=,==,!=)
print(5 > 4)
print(10 <= 2)

age = 21
if age > 18:
    print("you are adult")
else:
    print("you are not adult")

# if elif elif ... else

num = 2
if num < 2:
    print("less then 2")
elif num < 5:
    print("less then 5")
else:
    print("gt or el to 5")


# do if else ex of ch7


# loops
for i in range(0, 10):
    print(i)

for i in range(0, 11, 2):
    print(i)

# countdown using range
for i in range(10, 0, -1):
    print(i)

for i in range(1, 4):
    print(f"{i} square = {i * i}")


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


print(is_prime(7))

# Lists(array in some language)

my_fav_proglang = ["Python", "Go", "Javascript", "c"]

user_names = [
    "jay",
    "kishan",
    "john"
]
print(my_fav_proglang)
print(user_names)

# index start with 0
print("index 0", my_fav_proglang[0])
print("index 1", my_fav_proglang[-1])
print("index 2", my_fav_proglang[-2])

print("total programming language i love", len(my_fav_proglang))

my_fav_proglang[-1] = "c++"
print("My new List of fav prog lang", my_fav_proglang)

my_fav_proglang.append("Java")

print("My new List of fav prog lang", my_fav_proglang)

print("pop from list")

remove_lang = my_fav_proglang.pop()

print("My new List of fav prog lang", my_fav_proglang,
      f"now {remove_lang} is removed")

nums = [1, 2, 3, 4, 5]
# if we do not need index
for num in nums:
    print(num)

for num in nums:
    if num == 1:
        print("Found 1")

print(float('-inf'))
print(float('+inf'))


def get_odd_numbers(num):
    odd_numbers = []
    for i in range(0, num):
        if i % 2 == 1:
            odd_numbers.append(i)
    return odd_numbers


print(get_odd_numbers(10))

# slicing
nums = [10, 20, 30, 40, 50, 60]
print(nums[1:4:2])
print(nums[1::2])
print(nums[::2])
print(nums[1:])
print(nums[:2])
print(nums[-5:])

l1 = ["a", "b"]
l2 = ["c", "d"]
print(l1+l2)

prog_lang = ["c", "c++", "java", "python", "c#", "go", "ruby"]

# reverse the list
print(prog_lang[::-1])

print("rust" in prog_lang)
del prog_lang[-1]
print(prog_lang)
del prog_lang[:1]  # remove c from list
print(prog_lang)
del prog_lang[:]  # del whole list
print(prog_lang)


# Tuples are collections of data that are ordered and unchangeable
my_tuple = ("a", 34, False, 12.34)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])

# tuple with 1 item , watch for traling ,
t1 = (1,)

# Dictionaries
user = {
    "name" : "jay",
    "email" : "jay@gmail.com",
}
print(user)
print(user['name'])

for k , v in user.items():
    print(k,v)

# Because dictionaries rely on unique keys, you can't have two of the same key in the same dictionary. If you try to use the same key twice, the first value will simply be overwritten.

names = ["jay b" , "john doe"]
name_dict = {}

for name in names:
    name_last = name.split()
    name_dict[name_last[0]] = name_last[1]

print(name_dict)

del name_dict["jay"]

print(name_dict)

name_dict["jay"] = "b"

print(name_dict)

# deleting key that not exits errors out

user = {
    "name" : "jay",
    "email" : "jay@gmail.com",
}

print("name" in user)
print("phone" in user)

d1 = {
    "name" : "jay",
    "country": "IND"
}

d2 = {
    "age" : 21
}

users_info = {**d1,**d2}
print(users_info)
