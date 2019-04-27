import math

metros_pintar = int (input("qual o espaço a ser pintado?"))

litros = (metros_pintar / 6)

#questão a)
latas = math.ceil(litros / 18)
preco_latas = latas * 80

print ("serão utilizadas:", latas, "latas")
print ("que custarão:", preco_latas, "reais")

print("==*==" * 10)

#questão b)
galoes = math.ceil(litros / 3.6)
preco_galoes = galoes * 25

print ("serão utilizadas:", galoes, "galões")
print ("que custarão:", preco_galoes, "reais")

print("==*==" * 10)

#questão c)
latas1 = int (litros / 18)
faltou = litros % 18
galoes1 = math.ceil (faltou / 3.6)
preco_galoes1 = galoes1 * 25
preco_latas1 = latas1 * 80

print ("serão necessários:", latas1, "lata(s)")
print ( "e", galoes1, "galões")
print ("será gasto:", preco_galoes1 + preco_latas1, "reais")
