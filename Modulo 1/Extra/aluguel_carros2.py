carros = (input("Qual foi o modelo do carro alugado?"))
dias = float(input("Por quantos dias o carro foi alugado?"))
km = float(input("Quantos km o carro rodou?"))
total_dias = (dias * 60)
total_km = (km * 0.15)
resultado = total_dias + total_km
print (f" Vc andou {km}km por {dias}, então o preço a pagar é {resultado}")
if carros == "civic":
    diaria = 550
elif carros == "mercedes":
    diaria = 899
if carros == "bmw":
    diaria = 600
resultado = total_dias * total_km * diaria