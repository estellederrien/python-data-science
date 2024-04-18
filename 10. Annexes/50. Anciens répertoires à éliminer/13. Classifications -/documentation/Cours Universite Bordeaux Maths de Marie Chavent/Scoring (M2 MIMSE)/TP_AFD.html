
source("AFD_procedures.R")

insectes<-read.table("insectes.txt")
head(insectes)

colnames(insectes)<-c(paste("X",1:6,sep=""),"type") #change le nom des colonnes

#ou 
load("insectes.rda")
head(insectes)
X <- insectes[,1:6]
y <- insectes[,7]
class(y)

res <- AFD(X,y)

#----Question 1--------------
levels(y) #3 groupes donc au plus deux axes discriminants

#----Question 2--------------
n <-nrow(X) #nombre total d'insectes
res$nk #nombre d'insectes dans chaque groupes

#----Question 3----------------
res$g #centre de gravite de l'ensemble des donnees
res$gk

#----Question 4----------------
res$V
res$R

#----Question 5----------------
require(FactoMineR)

pca<-PCA(insectes,quali.sup=7,graph=FALSE) #ACP sur matrice des correlations
plot(pca,habillage=7)
plot(pca,choix="var")
plot(pca,invisible="ind")

#----Question 6----------------
res <- AFD(X,y)
res$eig

#----Question 7 et 8----------------
plotAFD(res)

#----Question 9----------------
#centre de gravite des donnees centrees
gA <- res$gk[[1]]-res$g
gB <- res$gk[[2]]-res$g
gC <- res$gk[[3]]-res$g


u1<-res$U[,1] #1er facteurs discriminants
t(gA)%*%u1
t(gB)%*%u1
t(gC)%*%u1

S1 <- res$S[,1] #1ere variable discriminante
Sk <- split(S1,y)
lapply(Sk,mean)

plotAFD(res,dim=1)

#----Question 10----------------

obs <- c(193,131,55,160,16,102)
g <- res$g#centre de gravite des donnees brutes (non centrees)
g <- res$g[,,drop=TRUE] #pour le transformer en vecteur
obs2 <- obs-g
obs2%*%u1

#-------Question 11 -------------------
smoy <- lapply(Sk,mean)
seuil1 <- (smoy$C+smoy$A)/2 #seuil entre C et A
seuil2 <- (smoy$A+smoy$B)/2 #seuil entre A et B

predict <- cut(S1,breaks=c(-2,seuil2,seuil1,2),labels=c("B","A","C"))
table(y,predict)
sum(y!=predict)/n


#-------Question 12 -------------------
n<-nrow(X)
index <- sample.int(n,50)
Xapp <- X[index,]
yapp <- y[index]
Xtest <- X[-index,]
ytest <- y[-index]

#construction de la règle sur l'ensemble d'apprentissage
res <- AFD(Xapp,yapp)
S <- res$S
Sk <- split(S,yapp)
smoy <- lapply(Sk,mean)
seuil1 <- (smoy$C+smoy$A)/2 #seuil entre C et A
seuil2 <- (smoy$A+smoy$B)/2 #seuil entre A et B


#application de la règle sur l'ensemble test

g <- res$g[,,drop=TRUE] #centre de gravité calculé sur Xapp
Xtest_centre <- sweep(Xtest,2,STATS=g,FUN="-") #centrage des données

Stest <- as.matrix(Xtest_centre)%*%u1 

predict <- cut(Stest,breaks=c(-2,seuil1,seuil2,2),labels=c("C","A","B"))
table(ytest,predict)
sum(ytest!=predict)/n

#-------Question 13 -------------------
res1 <- AFD(X,y, type="FR")
res2 <- AFD(X,y, type="GB")

lambda <- res1$eig
mu <- res2$eig

lambda/(1-lambda)
mu

head(res1$U) #même vecteur propre mais normé avec u'Vu=1
head(res2$U) #même vecteur propre mais normé avec u'Wu=1

head(res1$S) #donc même variable discriminante mais normé tq var(s)=1
head(res2$S) #donc même variable discriminante mais normé tq intra(s)=1

plotAFD(res1)
plotAFD(res2)

#-------Question 14 -------------------
require(MASS)
?lda


res3 <- lda(type~.,insectes)
res3$scaling #facteur discriminant
res2$U #identique celui de l'approche GB

pred <- predict(res3) #idem fonction predict.lda
?predict.lda
pred$x[1:5,] #variable discriminante (score de l'AFD)
res2$S[1:5,] #identique celui de l'approche GB




