# One-week-Python-Course
Getting through this Python learning course

Stings exercise complete

first = "Niko"
last = "Hulkenberg"

full_name=(first + " " + last)
print(full_name)

initials=(first[0] + " " + last[0])
print(initials)

initials_2=(first[0] + "." + last[0] + ".")
print(initials_2)

nickname=last[:4]
print(nickname)


-----------------------------------------------

Strings + Built-Ins + Functions Lesson

Arguments - fancy words for inputs

>>> burger(bun,secret_sauce,lettuce,tomato,bacon,cheese,well_done)

-----------------------------------------------

input() - Function requires you to enter some input, then it will convert it to a string and then it will return it. We can use this function to gather input in our programs.

>>>age=input('how old are you?')
how old are you?

>>>first_name=input("What is your name?")
print('Hi there' + ' ' + first_name + '!!!')

Result: Hi there NAME !!!

>>>

print('***WELCOME TO THE NAME APP***')

first_name=input('What is your first name?')
last_name=input('What is your last name?')

full_name=first_name + ' ' + last_name
print('Hey there ' + full_name)

-----------------------------------------------

AGE CALCULATOR EXCERCISE COMPLETE!!!

print('***WELCOME TO THE NAME APP***')

first_name=input('What is your first name?')
last_name=input('What is your last name?')

full_name=first_name + ' ' + last_name
print('Hey there ' + full_name)

age=input('How old are you?')

print('You are' + ' ' + str(int(age)*365) + ' ' + 'days old!')

print('Thank you so much, I appreciate that!')

-----------------------------------------------

SHOPPING CART EXERCISE

>>>My code

print('***WELCOME TO OUR USELESS STORE***')

item=input('What item are you purchasing? ')

price=input('What is a price of ' + item + "? ")

quantity=input('How many' + ' ' + item + ' ' + 'are you buying? ')

print('Added ' + quantity + ' ' + item + '(s)' + ' to shopping cart')
print('Subtotal:' + '$' + str(int(price)*int(quantity)))

>>>Supposed to be

print("WELCOME TO THE USELESS STORE")
print("*" * 30)

item=input("What item are you purchasing? ")

price=float(input(f"What is the price of {item}? "))

quantity=float(input(f"How many {item} are you buying? "))

print(f"Added {quantity} {item}(s) to a cart")
print(f"Subtotal: ${quantity*price}")

-----------------------------------------------
COMPLETE

-----------------------------------------------

Strip Methods

Strip Methods require a signature, provided in ([]). If no signature is provided, it goes with space by default.

EXAMPLE: "        hello    ".strip() - returns 'hello'

removes leading and trailing characters until it hits a non-space character (or other provided signature)

>>> "www.example.com".strip('cmowz.') will return 'example'

in description of a method, the siqnature goes in square brackets, and that means that you dont have to provide that (by defaulte the method will strip the string of all spaces

-----------------------------------------------

REPLACE METHODS

>>>str.replace(old,new,[count])

Replace method requires arguments

>>> freelance="agoodjob"
freelance.strip("good","bad")
abadjob

Use empty space as a replacement to delete a symbol

>>> prices="982379879$$$NJhsHGHG44$$$$$O&83O74287479879$$$"
prices.replace("$","")
"982379879NJhsHGHG44O&83O74287479879"

IMPORTANT

every signature in round brackets is required, every signature in square brackets is optional 

-----------------------------------------------

FIND AND INDEX METHOD

>>>str.find(req,[opt_start_from],[opt_end_at])

EXAMPLE: word="lickitylicklick"
word.find("l", 1)
8

will return -1 if nothing is found

-----------------------------------------------

REPLACE AND COUNT METHOD

>>> msg="Hot dog"
msg.replace("o","u")
Hut dug

>>> msg.replace("o","u", 1)
Hut dog

>>> msg.count("u")
0
msg.count("o")
2

The method will do what it tells - replace or count the specified signature as many times as you will tell it to

-----------------------------------------------

METHOD CHAINING

Methods can be chainde together to execute multiple actions at a time in a single line of code

>>> email="TOdd@gmail.com    "
print(email.lower().strip(" "))
todd@gmail.com

Not every method can be chained, only methods that return similar types of object

-----------------------------------------------

BOOLEANS

Booleans are another basic Python type. There are only two possible values: True and False. Notice the capitalization!!!

>>> True
>>> False

Decision making is broken down into a series of yes or no questions.

>>> isAlive = True
>>> isAlive = False

Comparison operator

> Greater then
< Lesser then
>= Greater Then or Equels To
<= Lesser Then or Equals To

a>b - a is greater then b

a<b - a is lesser then b

a>=b - a is greater or equals to b

a<=b - a is lesser or equals to b

>>> 3>10
False

>>> 30>10
True

>>> age=33
age>21
True

>>> age+33
age>=33
True

Booleans - kinda understand, need practice

More on booleans

== Equal To
!= Not Equal to

Notice: 4.0 == 4
True

Two data enteries are compared and the result is equal, no matter that one is integer and the other is a float.

Every value is inherently Truth-y or False-y in Python.

>>> False-y False, 0.0, 0, Empty strings, None, range(0), Empty data structures [](){} set()
>>> Truth-y everything else!

bool()
Just as we can use int(), float(), and str() to cast values, we can use bool()to cast a value to a Boolean

This is one way to determine wether Python considers a value to be Truth-y or False-y

>>> bool()

in Operator looks to see if an item is a member of a sequence

>>> "a" in "bat"
True

Comparing strings

>>> str1 = "ABC"
str2 = "AbC"
str3 = "ABc"

print(str1 > str2)
print(str2>str3)
print(str1>str3)

DECISIONS EXERCISE

COMPLETE!!!!

-----------------------------------------------

