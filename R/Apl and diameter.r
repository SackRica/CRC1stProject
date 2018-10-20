library (igraph)
library(poweRlaw)
library(data.table)

f <- read.table(file="../fb_edgeList.txt")
edges <- c()
edges <- as.vector(t(f[,1:2]))
for (e in 1:dim(f)[1]){
  edges <- append(edges, c(f[e, 1], f[e, 2]))
}
g <- graph(edges, directed = FALSE)

#APL
path1 <- average.path.length(g, unconnected=TRUE)
#Diameter
diametro <- diameter(graph, directed = TRUE, unconnected = TRUE, weights = NULL)
