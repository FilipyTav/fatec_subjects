salario: float = 100
idade: int = 200

operations: list[bool] = [
    salario > 1000 and idade > 18,
    salario != 2000 and idade <= 25,
    salario != 2000 and not idade <= 25,
    salario < 500 and idade > 18,
    salario >= 100 and idade < 30,
    salario == 100 and idade >= 20,
    salario != 50 and idade <= 25,
    salario > 50 and idade == 20,
    salario < 1000 or idade > 25,
    salario >= 200 or idade < 18,
    salario == 100 or idade >= 30,
    salario != 100 and idade < 21,
    salario > 200 and idade > 15,
    salario <= 100 and idade >= 20,
    salario < 500 or idade == 20,
    salario > 200 and not idade > 18,
    salario == 100 and not idade != 20,
    salario != 100 or idade > 30,
    not (salario > 1000 and idade > 18),
    not (salario == 100 and idade < 18),
    not (salario < 50 or idade > 40),
    not (salario >= 500 or idade <= 18),
    not (salario != 100 and idade == 20),
]

for i in range(len(operations)):
    print(f"{i + 1}: {operations[i]}")
