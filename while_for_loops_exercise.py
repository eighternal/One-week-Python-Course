word="supercalifragilisticexpialidocious"

for char in word:
    print(char)
print("*"*40)

idx = 0
while idx < len(word):
    print(word[idx])
    idx+=1
print("*"*40)

num=100
while num <= 140:
    print(num)
    num+=2
print("*"*40)

for num in range (100,142,2):
    print(num)
print("*"*40)

reply = input("Enter the passphrase: ")
while reply != "sillygoose":
    reply=input("Incorrect! Please enter the passphrase: ")
print("Thanks, quack!")