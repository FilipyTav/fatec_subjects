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
    return 15.0 if (age < 12 or age > 60) else 30.0


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
