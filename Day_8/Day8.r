file_name <- "Input.txt"
dims <- 99
data <- as.matrix(read.fwf(file_name,width=rep(1L,dims)))
f <- function(x) {(x > cummax(c(-1L,x[-dims]))) | (rev(x[dims:1] > cummax(c(-1L,x[dims:2])))) }
see <- function(x) { 
    sapply(seq_along(x), \(k) Position(\(y) y >= x[k],x[-(1:k)],nomatch = dims -k ))
}

#print(data)
print(sum(t(apply(data, 1, f )) | apply(data, 2,  f )))

print(max(t(apply(data, 1, \(x) see(x)*rev(see(rev(x))))) * apply(data, 2, \(x) see(x)*rev(see(rev(x))))))
#print(cummax(c(-1L,data[-dims])))

#print(data[dims:2])