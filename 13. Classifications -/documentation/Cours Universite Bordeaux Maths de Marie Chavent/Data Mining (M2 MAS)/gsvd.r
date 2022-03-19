#--------------Fonction SVD avec metriques ------------------

### Generalized SVD with diagonal metrics

gsvd <- function(Z,w,c)
{
  #-----input---------------
  # Z real matrix of dimension (n,p) and rank r
  # w weights of the rows N=diag(w)
  # c weights of the columns M=diag(c)
  #-----output---------------
  # d vector of size r of the singular values 
  # U matrix of dimension (n,r) of the eigenvectors of ZMZ'N
  # V matrix of dimension (p,r) of the eigenvectors of Z'NZM
  #----------------------------
  
  r <- qr(Z)$rank
  colnames<-colnames(Z)
  rownames<-rownames(Z)
  Z <- as.matrix(Z)
  Ztilde <- diag(sqrt(w)) %*% Z %*% diag(sqrt(c))
  e <- svd(Ztilde)
  U <-diag(1/sqrt(w))%*%e$u[,1:r] 
  V <-diag(1/sqrt(c))%*%e$v[,1:r] 
  d <- e$d[1:r] 
  rownames(U) <- rownames
  rownames(V) <- colnames
  if (length(d)>1)
    colnames(U) <- colnames (V) <- paste("dim", 1:r, sep = "")
  return(list(U=U,V=V,d=d))
}