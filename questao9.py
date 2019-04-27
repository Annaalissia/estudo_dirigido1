qtdecigarros = int(input("Informe a quantidade de cigarros fumados por dia: "))
anos = int(input("Quanto anos fumando?: "))

calc1 = (anos * 365) * qtdecigarros 
calc2 = (calc1 * 10)/24

print("O tota de dias perdidos será de: ", calc2, "dias")

