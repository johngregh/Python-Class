# Crash Course in Python
# Author: Breanna McBean
# Important functions in Python
# May 28, 2019

##############################################
# Variables in Python
# Python has dynamic typing, so you do not have to declare what type of variable you are working with
myint = 1
myfloat = 1.23
mystring = "hello"
# You can define a string using either single or double quote

# Lists
# Lists in Python are like arrays.
mylist = [0, 1, 2]
print("mylist:", mylist)
print("mylist[0]:", mylist[0])  # You can access each element
# Note: Python is a zero-indexed language, i.e.
# 0 = mylist[0]
# 1 = mylist[1]
# 2 = mylist[2]

# You can create multi-dimensional lists
my2dlist = [[1, 2, 3], [4, 5, 6]]
print("my2dlist:", my2dlist)
print("my2dlist[0][0]:", my2dlist[0][0])
print("my2dlist[1][2]:", my2dlist[1][2])
# Note: These are not necessarily the most efficient to work with. Other methods will be shown in the future.

# You can reassign elements within arrays (Lists are a mutable data type.
fruits = ["apple", "banana", "strawberry"]
print("fruits:", fruits)
fruits[0] = "orange"
print("new fruits:", fruits)

# Note: This might not be something you come across, but just so you know...
a = [1, 2, 3]
print("a:", a)
b = a

b.append(4)  # append adds an item to the end of a list
print("new a:", a)
# Changing b also changes a. This is because Python variables are pointers. If you don't know what that means,
# it's not super important, but still be aware.

# Tuples
# Tuples in python are similar to lists, but they are immutable, meaning you cannot change their elements.
fruits_tuple = ("apple", "banana", "strawberry")
print("fruits tuple:", fruits_tuple)
# You can access the elements of tuples
print("fruits_tuple[0]:", fruits_tuple[0])
# You cannot change the elements in a tuple once it has been created (immutable)
# fruits_tuple[0] = "orange"
# I commented out the above line because it will give an error.

# You can check the type of your variable
print("myint type:", type(myint))
print("myfloat type:", type(myfloat))
print("mystring type:", type(mystring))

# Note: When you reassign a new value to a variable, the variable will change types.
myfloat = "changing"
print("new myfloat type:", type(myfloat))
# Now, myfloat is a string

# You can change the type of a variable manually
print(float(57))
print(int(102.8))
# Note: Dividing by two integers can yield a float!
# Example
print(5 / 2)  # This yields 2.5, rather than rounding to get an int.
print(int(5 / 2))  # This yields 2 by chopping at the decimal rather than rounding

print(str(12))  # This is especially helpful if you want to print a statement including a numerical value, as below
# Example
user = "Sammy"
lines = 50
print("Congratulations, " + user + "! You just wrote " + str(lines) + " lines of code.")
# This works because you can concatenate strings using +

# Making lists
print("tuple to list:", list((0, 1, 2)))
print("string to list:", list("Stats"))  # Makes a list with each of the letters in order
# Making tuples
print("list to tuple:", tuple([0, 1, 2]))
print("string to tuple:", tuple("Stats"))

##############################################
# Conditional Statements in Python

print("conditional statement 'if'")
# "if" statements
x = 2
y = 8
if x < y:
    print(str(x) + " is less than " + str(y))

# What if the statement doesn't meet the condition? We can add an "else" to catch those cases.
print("conditional statement 'if/else'")
x = 8
y = 2
if x < y:
    print(str(x) + " is less than " + str(y))
else:
    print(str(x) + " is greater than " + str(y))
# Note: The "else" does not get it's own condition. It catches anything that doesn't meet the first condition.

# What about the case when x=y? We can capture that with an "elif"(else-if) condition (an additional condition)
print("conditional statement 'if/elif/else'")
x = 8
y = 8
if x < y:
    print(str(x) + " is less than " + str(y))
elif x == y:  # Note: When comparing for equality, use double equals sign
    print(str(x) + " is equal to " + str(y))
else:
    print(str(x) + " is greater than " + str(y))
# Note: The elif gets a specific condition, while the else statement still serves as a catch-all for cases
# that don't meet the first two conditions.

# Note: Be careful about defining variables inside of each condition. If you define it in one and use it later,
# you should define it in all of them.
# Example:
# if x < y:
#     ans = "less than"
# print(ans)
# This example will cause an error if the condition is not met because the variable ans will not be defined if the
# condition is never entered.

# You can also have nested if statements
print("nested conditional statement")
x = 2
y = 12
z = 10
if x < y:
    if x < z:
        print(str(x) + " is less than " + str(y) + " and " + str(z) + ".")
    else:
        print(str(x) + " is less than " + str(y) + ", but greater than " + str(z) + ".")
elif x == y:  # Note: When comparing for equality, use double equals sign
    print(str(x) + " is equal to " + str(y))
else:
    print(str(x) + " is greater than " + str(y))
# As an exercise, you can add the "x == z" condition within "x < y", and you can complete the nested statements for
# the "x == y" case and the "else" case.

# Using "and", "or", and negation in conditional statements

print("'and' in a conditional statement")
x = 2
y = 12
z = 10
if (x < y) & (x < z):
    print(str(x) + " is less than " + str(y) + " and " + str(z) + ".")
# This is like the first nested if statement above. We captured that same argument using a single condition and
# an "and". This will be true if both arguments are true. If one of the arguments is false, it will be false.

# We can also use "or"
print("using 'or' in a conditional statement")
x = 11
y = 12
z = 10
if (x > y) | (x > z):
    print(str(x) + " is not the smallest value.")

# We can also negate a condition
print("using negation in a conditional statement")
x = 2
y = 3

if x != y:
    print(str(x) + " is not equal to " + str(y))
# The "!" means "not"

##############################################
# Loops in Python

# For loops in Python
# For loops iterate through a specific, pre-determined range given by the programmer

# The "range" function in python allows you to create a range to iterate over
print("loops with range 1")
for x in range(5):
    print(x)
# This will print the numbers 0-4. The iterating will always stop one before the input value.

# You can also assign a starting point.
print("loops with range 2")
for x in range(10, 15):
    print(x)
# This will print the values 10-15.

# You are also able to give a step size for each iteration.
print("loops with range 3")
for x in range(0, 15, 3):
    print(x)
# This will print 0,3,6,9,12.

# Note: The Python package "itertools" has many useful functions for creating iterable lists for
# efficient looping

# Python also has a convenient way to iterate through lists and tuples.
print("loop through lists")
fruits = ["apples", "oranges", "bananas", "strawberries"]
for fruit in fruits:
    print(fruit)

# Above, "fruit" refers to the item in the list.

# Alternatively, you can still use the range function. Here "fruit" is an index.
print("loops with range 4")
for fruit in range(len(fruits)):
    print(fruits[fruit])

# You can use for loops to create a list
print("creating a list with loops")
integers = []
for i in range(10):
    integers.append(i)
print(integers)

# You can also iterate through strings
print("loop through strings")
word = "Statistics"
for letter in word:
    print(letter)

# Nested For Loops
# Nested for loops are good for iterating through two-dimensional arrays
print("nested for loops 1")
test = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
for i in range(3):
    for j in range(3):
        print(test[i][j])
# Above is the more "standard" way of indexing nested for loops. Below, you can find an example that uses the
# Python list indexing.
print("nested for loop 2")
for row in test:
    for item in row:
        print(item)

# While loops
# While loops continue running until a condition is met.
# Note: It is important to make sure you have an "updater" so that the condition will eventually be met
# and you do not end up in an infinite loop.
print("while loop")
i = 1
while i < 6:
    print(i)
    i += 1  # This is the "updater"

# The "+=" operator adds a value to the current i value (in this case, the value is one. You can also do -= ,
# *= , and /= to subtract by a value, multiply by a value, and divide by a value, respectively.

# You can also use a "break" statement to exit out of a loop for a given condition.
print("break statement 1")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# This will stop printing after 3

# The break statement will only take you out of the loop you are in. In the example below, the break statement will
# take you out of the for loop, but you will stay in the while loop.
i = 0
print("break statement 2")
while i < 5:
    print(i)
    for j in range(5):
        print(j)
        if i == j:
            break
    i += 1
    print("new i")

# There is also the "continue" statement to stop the current iteration but continue on to the next one.
print("continue statement")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# This will print 1, 2, 4, 5, 6. Three is skipped because of the continue statement.

##############################################
# User-Defined Functions in Python

# You start a a function in Python with the "def" keyword.

# Function to print hello
def greetings():
    print("Hello")


print("greetings function")
greetings()


# We can also have functions with input parameters
# Will greet a certain number of times
def greet_count(number):
    for k in range(number):
        print("Hello")


print("greet count function")
greet_count(3)


# The input parameter can be a list
def grocery_list(items):
    for thing in items:
        print(thing)


print("grocery_list function")
my_list = ["pasta", "eggs", "milk"]
grocery_list(my_list)


# You can have a function with a default value in case you don't input a parameter
def university(school="CSUF"):
    print("I go to " + school)


print("university function with input 1")
university("UCI")
print("university function with input 2")
university("CSULB")
print("university function default value")
university()


# You can also have functions with return values
def square(val):
    return val * val


print("function with a return value")
print(square(2))
