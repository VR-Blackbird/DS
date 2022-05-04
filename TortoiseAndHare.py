# Find the duplicate number from a sequence on 1 to n+1

duplicate_list = [1, 3, 2, 4, 5, 5]


def find_duplicate(entry):
    if not entry:
        return None
    tortoise = entry[0]
    hare = entry[0]

    while True:
        tortoise = entry[tortoise]
        hare = entry[entry[hare]]
        if tortoise == hare:
            break

    tortoise = entry[0]

    while True:
        tortoise = entry[tortoise]
        hare = entry[hare]
        if tortoise == hare:
            print(tortoise)
            break


find_duplicate(duplicate_list)
