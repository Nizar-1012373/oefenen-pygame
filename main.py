import math


iets = input("wat is je naam:")
nog_iets = input("wat is je leeftijd:")
niks = f"{iets}"
print(f"je naam is: {niks} met de leeftijd van: {nog_iets}")


# integers
print("iets".upper())
print(abs(-1))
print(max(2, 3, 5, 2, 4, 6, 8, 66, 43, 34))
print(min(2, 2, 2, 3, 4, 4, 456, 545, 3, 4654, 34, 4, 3))


def triangle(x, y):
    z = math.sqrt(pow(x, 2) + pow(y, 2))
    return z


side_1 = input("wortel ")
side_2 = input("wortel 2")

print(triangle(int(side_1), int(side_2)))
