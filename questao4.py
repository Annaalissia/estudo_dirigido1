salario = float(input("Qual o valor so salário?? "))
porcentagem = float(input("qual a porcentagem de correção salarial?: "))

total = salario * porcentagem/100
print(" Seu aumento foi de R$: ", total)
print("seu novo salário será R$: ", salario + total)
