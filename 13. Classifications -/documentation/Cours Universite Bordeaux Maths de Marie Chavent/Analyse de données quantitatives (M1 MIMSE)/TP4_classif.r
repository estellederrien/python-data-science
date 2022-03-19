#-------------TP les algorithmes de classification--------------

#-------Exercice 1-------------

X <- matrix(NA,4,2)
X[1,] <- c(5,4)
X[2,] <- c(4,5)
X[3,] <- c(1,-2)
X[4,] <- c(0,-3)

rownames(X)  <- c("ind1","ind2","ind3","ind4")
colnames(X) <- c("var1","var2")
        
help(kmeans)

init<-X[1:2,] #
kmeans(X,centers=init)

#Pour calculer la somme des carres totaux:
apply(X,2,var)
3*sum(apply(X,2,var)) #inertie totale (avec poids egaux a 1)


#-------Exercice 2-------------

#dendrogramme du lien max
d <- dist(X) #matrice de distances euclidiennes

tree <- hclust(d) #lien max pas defaut
names()
tree$height
plot(tree)
cutree(tree,2)

#dendrogramme de ward
d^2 #distances au carre
tree  <- hclust(d^2,method="ward")
plot(tree)

g1 <- c(0.5,-2.5)
g2 <- c(4.5,4.5)

t(g1-g2)%*%(g1-g2) #carre de la distance euclidienne entre g1 et g2
tree$height  #indice de ward*2



