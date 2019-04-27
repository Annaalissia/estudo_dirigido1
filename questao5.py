mercadoria = float(input("Qual o valor da mercadoria?: "))
desconto = float(input("Qual o valor de desconto?: "))

valordesconto = mercadoria * desconto/100

print("Seu desconto será de R$: ", valordesconto)
print("valor final da compra R$: ", mercadoria - valordesconto)
