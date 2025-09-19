# Ex.: 1 -- N vou fazer, trivial


# Ex.: 2
def print_table(n: int) -> None:
    for i in range(1, 10 + 1):
        print(f"{n} x {i} = {n * i}")


# n: int = int(input("Número: "))
#
# print_table(n)


# Ex.: 3
def evens(min: int, max: int) -> list[int]:
    return [i for i in range(min if min % 2 == 0 else min + 1, max + 1, 2)]
