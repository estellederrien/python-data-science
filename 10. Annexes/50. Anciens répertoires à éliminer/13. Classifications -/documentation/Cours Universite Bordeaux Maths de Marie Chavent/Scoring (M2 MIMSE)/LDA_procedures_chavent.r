linear_func <- function(X,y,type="geom")
{
	X <- data.frame(X)
	n<-nrow(X)
	p <- ncol(X)
	K<-length(levels(factor(y)))
	nk<-as.vector(table(y))
	names(nk) <- levels(y)
	pk<-nk/n

	Xk <-list()
	Xk <- split(X,y)

	V<-var(X)*(n-1)/n
	g<-matrix(apply(X,2,mean),ncol=1)
	rownames(g) <- colnames(X)
	Vk<-list()
	gk<-list()
	for (k in 1:K){
		gk[[k]]<-matrix(apply(Xk[[k]],2,mean),ncol=1)
		rownames(gk[[k]]) <- colnames(X)
		Vk[[k]]<-var(Xk[[k]])*(nk[k]-1)/nk[k]
		}

	W<-matrix(0,nrow=p,ncol=p)
	for (k in 1:K){
		W<-W+pk[k]*Vk[[k]]
	}
	W <- W*n/(n-K)
  
	Lk <- matrix(NA,p+1,K)
	rownames(Lk) <- c("constant",colnames(X))
	colnames(Lk) <- levels(y)
	invW <- solve(W)
	for (l in 1:K)
	{
		Lk[1,l] <- -0.5* t(gk[[l]])%*% invW %*%gk[[l]]
		if (type=="prob") Lk[1,l] <-  Lk[1,l] +log(pk[l])
		Lk[2:(p+1),l] <- invW %*%gk[[l]]
	}
	S <- matrix(NA,n,K)
	for (l in 1:K)
	{
		S[,l] <- as.matrix(X) %*% Lk[2:(p+1),l] + Lk[1,l]
	}
 
	return(list(Lk=Lk,W=W,gk=gk, S=S))
		
}