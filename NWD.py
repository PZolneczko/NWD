def nwd(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

x = int(input("podaj pierwszą liczbę: "))
y = int(input("podaj drugą liczbę: "))

print("największy wspólny dzielnik dla " + str(x) + " i " + str(y) + " to: " + str(nwd(x,y)) )
