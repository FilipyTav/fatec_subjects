# Ex.: 1
def get_sign(n: int) -> int:
    return 1 if n > 0 else -1 if n < 0 else 0


# n: int = int(input("Número: "))
# sign: int = get_sign(n)
# print(f"O número é {'positivo' if sign > 0 else 'negativo' if sign < 0 else 0}")


# Ex.: 2
def is_even(n: int) -> bool:
    return n % 2 == 0


# Ex.: 3
def is_adult(age: int) -> bool:
    return age >= 18


# Ex.: 4
def get_price(age: int) -> float:
    return 15.0 if (age < 12 or age >= 60) else 30.0


# Ex.: 5
def compare(a: float, b: float) -> int:
    return 1 if a > b else -1 if a < b else 0


# Ex.: 6
def determine_student_situation(grade: float) -> int:
    return 1 if grade >= 7 else 0 if grade >= 5 and grade <= 6.9 else -1


# Ex.: 7
def calculate_IMC(weight: float, height: float) -> float:
    return weight / (height * height)


def determine_IMC(imc: float) -> str:
    return (
        "Abaixo do peso"
        if imc < 18.5
        else (
            "Peso normal"
            if imc >= 18.5 and imc < 25
            else "Sobrepeso" if imc >= 25 and imc < 30 else "Obesidade"
        )
    )


# Ex.: 8
def is_valid_triangle(a: float, b: float, c: float) -> bool:
    return (a > 0 and b > 0 and c > 0) and (a + b > c and a + c > b and b + c > a)


def classify_triangle(a: float, b: float, c: float) -> str:
    if not is_valid_triangle(a, b, c):
        return "Inválido"
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"


# Ex.: 9
def get_bonus(salary: float) -> float:
    return (
        20.0
        if salary < 2000.0
        else 10.0 if salary >= 2000.0 and salary <= 5000.0 else 5.0
    )


# Ex.: 10
def is_leap_year(year: int):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


# Ex.: 11
import random

num = random.randint(1, 100)
# usern = int(input("Número: "))

# print(compare(num, usern))


# Ex.: 12
def classify_temp(c: float) -> int:
    return -1 if (c <= 15.0) else 0 if c > 15 and c < 26 else 1


# Ex.: 13
def get_delivery_fee(price: float) -> float:
    return 0 if price > 100 else 15


# Ex.: 14
def convert_grades(grade: float) -> str:
    if grade >= 9:
        return "A"
    if grade >= 7 and grade < 9:
        return "B"
    if grade >= 5 and grade < 7:
        return "C"
    if grade >= 3 and grade < 5:
        return "D"
    else:
        return "E"


# Ex.: 15
def calculate_bus_fee(age: int, has_student_card: bool) -> int:
    return -1 if age < 6 or age >= 65 else 0 if has_student_card else 1


# Ex.: 16
def calc_income_tex(salary: float) -> float:
    if salary < 1900:
        return 0
    elif salary >= 1900 and salary < 2800:
        return 7.5
    elif salary >= 2800 and salary < 3700:
        return 15
    elif salary >= 3700 and salary < 4600:
        return 22.5
    else:
        return 27.5


# Ex.: 17
def withdraw_money(value: float) -> dict[int, int]:
    amounts: dict[int, int] = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 1: 0}
    remainder: float = value
    for key in amounts:
        if not remainder:
            break
        amounts[key] = int(remainder // key)
        remainder -= amounts[key] * key

    return amounts


# Ex.: 18
correct_data: dict[str, str] = {"user": "eu", "pw": "admin"}
tries: int = 0
# while tries < 3:
#     user = input("Usuário: ")
#     senha = input("Senha: ")
#     if user == correct_data["user"] and senha == correct_data["pw"]:
#         print("Login bem-sucedido!")
#         break
#     else:
#         print("Usuário ou senha incorretos!")
#         tries += 1
#     print()


# Ex.: 19
def classify_athlete(age: int) -> str:
    if age < 12:
        return "Infantil"
    if age >= 12 and age < 18:
        return "Juvenil"
    if age >= 18 and age <= 40:
        return "Adulto"
    else:
        return "Veteranos"


# Ex.: 20
def queue_priority(age: int, pregnant: bool = False, deficient: bool = False) -> int:
    return 1 if age >= 60 or deficient else 0 if pregnant else -1
