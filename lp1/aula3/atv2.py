def has_benefits(age: int, salary: float) -> bool:
    if age > 60 or (age > 18 and salary <= 2000):
        return True

    return False


age: int = int(input("Idade: "))
salary: float = float(input("Salário: "))

print(f"Você{'' if has_benefits(age, salary) else ' não'} tem direito aos benefícios")
