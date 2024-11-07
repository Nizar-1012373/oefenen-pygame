# # classes leren en goed kijken wat ze echt gaan doen

# # basic class


# class TestClass:
#     # deze variable in een class is attribute van de class
#     mijn_var = "Mohamed"
#     new_var = "anas"

#     # je kan ook een functie maken in een class, dat noemen we een method
#     # in de functie kan je ook de class oproepen door self als argument te nemen
#     # self verwijst naar alle instances in de class
#     def test_class(self):
#         print(f"dit is mijn class{self.mijn_var}")
#         # dit is hetzelfde als test3.new_function("nizatr") alleen met een andere argument
#         self.new_function("dan")

#     def new_function(self, name):
#         print(name)


# # instance class

# test = TestClass()
# print(test.mijn_var)

# # kan ook een attribute van de class herschrijven
# test3 = TestClass()
# test3.new_var = "joost"
# # zo roep je de methode op
# print(test3.new_var, test3.test_class())
# # je kan een argument van een andere parameter naast self zo instanceren of in een andere functie in de class
# test3.new_function("nizatr")


# oefening class
class MonsterParent:

    def attack(self):
        print(f"attack{self.damage}")


class Monster(MonsterParent):
    def __init__(self, damage, health):

        self.damage = damage
        self.health = health


monster = Monster(3, 4)
print(monster.health)
monster.attack()
