import matplotlib.pyplot as plt
a = float(input("valeur de A ?"))
b = float(input("valeur de B ?"))
pas = float(input("valeur du Pas ?"))
while a<=b:
	plt.scatter(a,a**2,s=100)
	a=a+pas
plt.show()	