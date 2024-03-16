def number_sun(n):
    sum = 0
    for i in range(0,n+1):
        sum = sum + i
number_sun(3)

def find_min(nums):
    return min(nums)

l = [11,2,3,4,56]

print(find_min(l))

def remove_nonints(nums):
    l = []
    for i in nums:
        if type(i) == int:
            l.append(i)
    return l

def factorial(num):
    f = 1
    for i in range(1,num+1):
        f = f * i
    return f
print(factorial(5))

def fizzbuzz(start, end):
    for i in range(start,end):
        if (i % 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

def join_strings(strings):
    result = ''
    for i, string in enumerate(strings):
        result += string
        if i < len(strings) - 1:
            result += ','
    return result
