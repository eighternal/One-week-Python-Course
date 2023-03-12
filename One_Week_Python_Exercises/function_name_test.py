# def laugh():
#     print("HA"*20)


# laugh()

# def laugh(intensity):
#     print("HA" * intensity)

# laugh(3)

# def division(a,b):
#     print (a/b)

# division(10,5)

def is_even(num):
    return num % 2 == 0

def slugify(phrase):
    return phrase.lower().strip().replace(" ","-")

def count_vowels(word):
    count = 0
    for char in word:
        if char in "aeiou":
            count+=1
    return count
