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
