# https://stackoverflow.com/questions/59582648/turning-bars-to-a-normal-distribution

# Import des librairies
import matplotlib.pyplot as plt
import statistics
import seaborn as sns

# Loi de probabilité discrète :
"""   
On a un vecteur de % d'acheteurs et un vecteur de taille de vêtements.
"""

# Pourcentage d'acheteurs en %
h =[1,1,3,5,9,13,16,16,14,10,5,4,2,1,0]

# Taille de vêtements
x =  [34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]

# Calcul de probabilités ( On peut faire une fonction, pas le temps) :
# P(X=40) La probabilité que les acheteurs achètent du 40 est de 16 %
# P(37 <= X <= 40) La probabilité que les acheteurs achètent entre 37 et 40 est de 5+9+13+16 = 43 %

# On calcule moyenne et écart type
moyenne = statistics.mean(h)
ecartType = statistics.stdev(h)

print ("Moyenne du pourcentage d'acheteurs : ", moyenne)
print ("ecartType du pourcentage d'acteurs: ", ecartType)

# On trace le graphique en barres
plt.ylabel('buyers % ')
plt.xlabel('size')
plt.bar(x, height = h)
plt.grid(True)
plt.show()

# Ensuite, on trace la loi normale par dessus ...
data = []
for i in range(len(x)): data += [x[i]]*h[i] 
sns.set()
plt.figure(figsize=(10,5),dpi=100)
sns.distplot(data, fit=norm, kde=False)
plt.show()

# Si on transforme les barres de  l'histogramme en une fonction continue f de densité.
 # Alors,  P(37 <= X <= 40) = aire de l'intégrale sous f() entre l'Intervalle x[37,40]



