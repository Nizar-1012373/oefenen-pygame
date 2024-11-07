# je hebt list comprehension (one line for loop )
# en je hebt one line if statements

# normale for loop

# list = []
# for i in range(0, 11, 1):
#     list.append(i)
# print(list)

# list comprehension
sec_list = [i for i in range(0, 11, 1)]
print(sec_list)

# output is precies hetzelfde!

# je kan ook een for loop in een for loop doen met list comprehension
for_loepie = [(i, j) for i in range(0, 11, 1) for j in ("a", "b", "c")]
print(for_loepie)
# is het zelfde als een normale for loop in een for loop
lala = []
for i in range(0, 11, 1):
    for j in ["a", "b"]:
        lala.append((i, j))
        print(lala)

# oefening
lijst = [0, 1, 2, 3, 4, 5]
letters = ["a", "b", "c", "d", "e"]
battle_ship = [(i, j) for i in lijst for j in letters if (i, j) != (3, "c")]
print(battle_ship)
