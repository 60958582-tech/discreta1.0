# Programa: término n-ésimo de una progresión geométrica

a1 = float(input("Ingresa el primer término (a1): "))
r = float(input("Ingresa la razón (r): "))
n = int(input("Ingresa el número de término que quieres (n): "))
if r!=1:
    an = a1 * (r ** (n - 1))
else:
    print("el r debe ser diferente de 1")
print("El término número", n, "de la progresión geométrica es:", an)