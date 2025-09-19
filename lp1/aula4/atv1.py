# Ex.: 1
def count(n: int) -> None:
    i: int = 1
    while i <= n:
        print(i)
        i += 1


# Ex.: 2
correct_data: dict[str, str] = {"user": "eu", "pw": "admin"}


def play():
    while True:
        user: str = input("Usuário: ")
        pw: str = input("Senha: ")

        if user == correct_data["user"] and pw == correct_data["pw"]:
            print("Acesso permitido!")
            break

        print("Senha/Usuário incorretos. Tente novamente")
        print()


# Ex.: 3
def sum_nums() -> int:
    sum: int = 0
    while True:
        n: int = int(input("Digite um número (0 para sair): "))
        if not n:
            break
        sum += n
        print()
    return sum


# print(sum_nums())
