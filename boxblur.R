############################################
# BRUTE FORCE FINDING AVERAGES -- BOX BLUR #
############################################

library(raster) 
myJPG <- stack("rgb_eg.png")  
plotRGB(myJPG) 

r_mat <- matrix(nrow = 1, ncol = 3)
g_mat <- matrix(nrow = 1, ncol = 3)
b_mat <- matrix(nrow = 1, ncol = 3)

for (i in 1:3){
  for (j in 1:1){
    r_stack <- c()
    g_stack <- c()
    b_stack <- c()
    
    for (k in i:4*i){
      for (l in j:4*j){
        r_stack <- append(r_stack, myJPG$rgb_eg.1[k,l])
        g_stack <- append(g_stack, myJPG$colour.2[k,l])
        b_stack <- append(b_stack, myJPG$colour.3[k,l])
      }
    }
    avg_r <- sqrt(mean(r_stack^2))
    avg_g <- sqrt(mean(g_stack^2))
    avg_b <- sqrt(mean(b_stack^2))
    
    r_mat[i,j] <- avg_r
    g_mat[i,j] <- avg_g
    b_mat[i,j] <- avg_b
  }
}

rrast <- raster(r_mat)
grast <- raster(g_mat)
brast <- raster(b_mat)

stacky <- stack(rrast,grast,brast)
plotRGB(stacky)

####################
# SOME NAIVE THING #
####################

############################################
# BRUTE FORCE FINDING AVERAGES -- BOX BLUR #
############################################

library(raster) 
myJPG <- stack("rgb_eg.png")  
plotRGB(myJPG) 

r_mat <- matrix(nrow = 1, ncol = 6)
g_mat <- matrix(nrow = 1, ncol = 6)
b_mat <- matrix(nrow = 1, ncol = 6)

# manual

r_stack <- c()
g_stack <- c()
b_stack <- c()

for (k in 1:4){
  for (l in 1:2){
    r_stack <- append(r_stack, myJPG$rgb_eg.1[k,l])
    g_stack <- append(g_stack, myJPG$rgb_eg.2[k,l])
    b_stack <- append(b_stack, myJPG$rgb_eg.3[k,l])
  }
}

#avg_r <- sqrt(mean(r_stack^2))
#avg_g <- sqrt(mean(g_stack^2))
#avg_b <- sqrt(mean(b_stack^2))

avg_r <- mean(r_stack)
avg_g <- mean(g_stack)
avg_b <- mean(b_stack)

r_mat[1,1] <- avg_r
g_mat[1,1] <- avg_g
b_mat[1,1] <- avg_b

# second iteration

r_stack <- c()
g_stack <- c()
b_stack <- c()

for (k in 1:4){
  for (l in 3:4){
    r_stack <- append(r_stack, myJPG$rgb_eg.1[k,l])
    g_stack <- append(g_stack, myJPG$rgb_eg.2[k,l])
    b_stack <- append(b_stack, myJPG$rgb_eg.3[k,l])
  }
}

#avg_r <- sqrt(mean(r_stack^2))
#avg_g <- sqrt(mean(g_stack^2))
#avg_b <- sqrt(mean(b_stack^2))

avg_r <- mean(r_stack)
avg_g <- mean(g_stack)
avg_b <- mean(b_stack)

r_mat[1,2] <- avg_r
g_mat[1,2] <- avg_g
b_mat[1,2] <- avg_b

# third iteration

r_stack <- c()
g_stack <- c()
b_stack <- c()

for (k in 1:4){
  for (l in 5:6){
    r_stack <- append(r_stack, myJPG$rgb_eg.1[k,l])
    g_stack <- append(g_stack, myJPG$rgb_eg.2[k,l])
    b_stack <- append(b_stack, myJPG$rgb_eg.3[k,l])
  }
}

#avg_r <- sqrt(mean(r_stack^2))
#avg_g <- sqrt(mean(g_stack^2))
#avg_b <- sqrt(mean(b_stack^2))

avg_r <- mean(r_stack)
avg_g <- mean(g_stack)
avg_b <- mean(b_stack)

r_mat[1,3] <- avg_r
g_mat[1,3] <- avg_g
b_mat[1,3] <- avg_b


r_stack <- c()
g_stack <- c()
b_stack <- c()

for (k in 1:4){
  for (l in 7:8){
    r_stack <- append(r_stack, myJPG$rgb_eg.1[k,l])
    g_stack <- append(g_stack, myJPG$rgb_eg.2[k,l])
    b_stack <- append(b_stack, myJPG$rgb_eg.3[k,l])
  }
}

#avg_r <- sqrt(mean(r_stack^2))
#avg_g <- sqrt(mean(g_stack^2))
#avg_b <- sqrt(mean(b_stack^2))

avg_r <- mean(r_stack)
avg_g <- mean(g_stack)
avg_b <- mean(b_stack)

r_mat[1,4] <- avg_r
g_mat[1,4] <- avg_g
b_mat[1,4] <- avg_b


r_stack <- c()
g_stack <- c()
b_stack <- c()

for (k in 1:4){
  for (l in 9:10){
    r_stack <- append(r_stack, myJPG$rgb_eg.1[k,l])
    g_stack <- append(g_stack, myJPG$rgb_eg.2[k,l])
    b_stack <- append(b_stack, myJPG$rgb_eg.3[k,l])
  }
}

#avg_r <- sqrt(mean(r_stack^2))
#avg_g <- sqrt(mean(g_stack^2))
#avg_b <- sqrt(mean(b_stack^2))

avg_r <- mean(r_stack)
avg_g <- mean(g_stack)
avg_b <- mean(b_stack)

r_mat[1,5] <- avg_r
g_mat[1,5] <- avg_g
b_mat[1,5] <- avg_b


r_stack <- c()
g_stack <- c()
b_stack <- c()

for (k in 1:4){
  for (l in 11:12){
    r_stack <- append(r_stack, myJPG$rgb_eg.1[k,l])
    g_stack <- append(g_stack, myJPG$rgb_eg.2[k,l])
    b_stack <- append(b_stack, myJPG$rgb_eg.3[k,l])
  }
}

#avg_r <- sqrt(mean(r_stack^2))
#avg_g <- sqrt(mean(g_stack^2))
#avg_b <- sqrt(mean(b_stack^2))

avg_r <- mean(r_stack)
avg_g <- mean(g_stack)
avg_b <- mean(b_stack)

r_mat[1,6] <- avg_r
g_mat[1,6] <- avg_g
b_mat[1,6] <- avg_b


# final stuff

rrast <- raster(r_mat)
grast <- raster(g_mat)
brast <- raster(b_mat)

stacky <- stack(rrast,grast,brast)
plotRGB(stacky)
