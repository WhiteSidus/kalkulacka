x = int(input("Zadejte první čislo: "))
y = int(input("Zadejte druhe čislo: "))

print("Pro sčítání zadejte +")
print("Pro odčítání zadejte -")
print("Pro násobení zadejte *")
print("Pro dělení zadejte /")
print("Pro mocnění zadejte **")
print("Pro odmocnění zadejte /*")

znamenko = input("Zvolte si operator: ")
if znamenko == "+":
    print(x + y)

elif znamenko == "-":
    print(x - y)

elif znamenko == "*":
    print(x * y)

elif znamenko == "/":
    if y != 0:
        print(x / y)
    else:
        print("Chyba! Chyba! Chyba!")
elif znamenko == "**":
    print(x ** y)

elif znamenko == "/*":
    if y < 0:
        print ("Chyba!")
    else:
        print(x ** (1/y))
