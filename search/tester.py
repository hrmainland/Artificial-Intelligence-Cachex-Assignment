def recurse(number):
    print(number)
    if number >= 5:
        return number
    recurse(number + 1)

print(recurse(1))