# lambda fucntions

# lambda functions zijn gewoon normale functies maar kost ook veel minder typwerk


# voorbeeld van een normale function
def voorbeeld(dag):
    print(dag * 3)


voorbeeld("zaterdag ")
# output: zaterdag zaterdag zaterdag


# zelfde functie maar dan met lambda

voorbeeld_2 = lambda day: print(day * 3)

voorbeeld_2("zaterdag ")


# sommige funtions willen een function als argument
# sorted_list = [("Joe", 34), ("John", 22), ("omar", 25), ("Ali", 48)]
# obje = sorted(sorted_list)
# print(obje)
# output : [('Ali', 48), ('Joe', 34), ('John', 22), ('omar', 25)]

# hij sort nu op alfabetische volgorde maar stel je wilt op leeftijd hoe doe je dat?

sorted_list = [("Joe", 34), ("John", 22), ("omar", 25), ("Ali", 48)]
obje = sorted(sorted_list, key=lambda persoon: persoon[1])
# geeft van jongste naar oudste
print(obje)
# geeft van oudste naar jongste
print(obje[::-1])
