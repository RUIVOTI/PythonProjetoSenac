
iphone = 2980
samsung = 2540
tablet = 1950
ps5 = 2100
notebook = 2350

qtdiphone = int(input("digite a quantidade de iphone"))
qtdsamsung = int(input("digite a quantidade de samsung"))
qtdtablet = int(input("digite a quantidade de tablet"))
qtdps5 = int(input("digete a quantidede de ps5"))
qtdnotebook = int(input("digete a quantidade de notebook"))

valortotal = (qtdiphone*iphone)+(qtdsamsung*samsung)+(qtdtablet*tablet)+(qtdps5*ps5)+(qtdnotebook*notebook)
print(valortotal)

valordaparcela3x = (valortotal/3)
print(valordaparcela3x)

valordaparcela = (((valortotal * (5/100))+valortotal))/6
print(valordaparcela)

valordodesconto = (valortotal - (valortotal * (10/100)))
print(valordodesconto)
