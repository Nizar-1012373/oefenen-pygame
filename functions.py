# parameters en arguments


# def hobby(voetbal, basketball):
#     count = 0
#     while count < basketball:
#         count += 1
#         print(basketball, voetbal)


# hobby("real", 7)

# # return statements in functies


# def print_statements(parameter):
#     i = 0
#     while i < len(parameter):
#         print(parameter)
#         i += 1

#     return print("iets", i)


# print_statements("ss")


def shouter(something, luid):
    for i in range(luid):
        if i < 10:
            print(something.upper())
        else:
            print("nothing")

    return print("done")


shouter("kaak ", 20)
