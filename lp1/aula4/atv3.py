# Ex.: 1
def count(min: int, max: int) -> None:
    for i in range(min, max + 1):
        print(i)


# Ex.: 2
def multiples(n: int, min: int, max: int):
    return [
        i for i in range(min if min % n == 0 else (n + min) - (min % n), max + 1, n)
    ]


# print(multiples(5, 23, 32))


# Ex.: 3
def evens(min: int, max: int) -> list[int]:
    return [i for i in range(min if min % 2 == 0 else min + 1, max + 1, 2)]


# Ex.: 4
def withdraw_money(value: float) -> dict[int, int]:
    amounts: dict[int, int] = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    remainder: float = value
    for key in amounts:
        if not remainder:
            break
        amounts[key] = int(remainder // key)
        remainder -= amounts[key] * key

    return amounts


# Ex.: 5
def fatorial(n: int, acc: int = 1) -> int:
    if n < 0:
        return -1
    if n == 0:
        return acc
    return fatorial(n - 1, acc * n)
