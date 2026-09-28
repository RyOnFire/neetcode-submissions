def add_two_numbers() -> int:
    sum12 = input()
    ex = sum12.split(",")
    total = 0
    for i in ex:
        total = total + int(i)
    return total



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
