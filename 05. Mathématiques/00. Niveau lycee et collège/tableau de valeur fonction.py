a = float(input("valeur de A ?"))
b = float(input("valeur de B ?"))
pas = float(input("valeur du Pas ?"))
x = a
y = x**2
while x<=b:
	y=x**2
	print(x," a pour image",y)
	x=x+pas