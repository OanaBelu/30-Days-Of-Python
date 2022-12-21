
# Incepem astazi quiz-ul.

# Python Challenge day 1:
lst_1 = [1, 2, 3, 4]
lst_2 = [1, 2, 3, 4]
print(lst_1 == lst_2, lst_1 is lst_2) # True False
# True True
# True False
# False True
# False False
# De ce ai facut aceasta alegere?

# Python Challenge day 2 :
# Se da variabila numere, care este o lista si variabila suma, care reprezinta un intreg
# Returneaza indicii oricaror doua numere din lista numere, care adunate, vor fi egale cu valoarea variabilei suma
# Ex:
numere = [1, 4, 7, 9]
suma = 5
# output: 0,1 pentru ca numere[0] + numere[1] = 1 + 4 = 5
#
# numere = [5, 6, 3 ,7]
# suma = 10
# output: 2,3



for _ in range (2,6):
    print("cdr")

friends =[ "Ana"" Rud "" Cld"]
print(",".join(friends))

while True:
    num = int(input("Number : "))

    if num < 100:
        break
names = ["ana", "fer", "kdfr"]

for counter, name in enumerate(names):
    print((f'{counter}. {name}'))

names = ["ana", "fer", "kdfr"]
pets = ["caine", "pisica", "cal"]
for name, pet in zip(names,pets):
    print((f'{name.title()} owns {pet}'))

# The repr() function returns a printable representational string of the given object.

def generate_prompt(animal):

    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(animal.capitalize())

generate_prompt("Cat")

# Normal function
def normal_test():
    return "Hello World"


# Generator function
def generator_test():
    yield "Hello World"


print(normal_test())  # call to normal function
print(generator_test())  # call to generator function

print(normal_test())
print(next(generator_test()))  # will output Hello World
print(list(generator_test()))


def even_numbers(n):
    for x in range(n):
        if (x % 2 == 0):
            yield x


num = even_numbers(10)
print(list(num))


def even_numbers(n):
    for x in range(n):
        if (x % 2 == 0):
            yield x


num = even_numbers(10)
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))


# print(next(num))

def getFibonnaciSeries(num):
    c1, c2 = 0, 1
    count = 0
    while count < num:
        yield c1
        c3 = c1 + c2
        c1 = c2
        c2 = c3
        count += 1


fin = getFibonnaciSeries(7)
print(list(fin))
for i in fin:
    print(i)
