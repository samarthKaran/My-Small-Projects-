#r*r = 1 - (Square error of bestline(y)/Square error of mean(y))

from statistics import mean #to include mean from stats
import numpy as np
import matplotlib.pyplot as plt #to plot graph 

x = np.array([1,2,3,4,5,6] , dtype = np.float64) #converts list to array
y = np.array([4,1,6,2,6,1] , dtype = np.float64) 

def bestfitline (x,y):
    m = ( ((mean(x) * mean(y)) - mean(x*y))/
          ((mean(x) * mean(x)) - mean(x*x)) )

    c = mean(y) - m * mean(x)
    return m,c

m,b = bestfitline(x,y)

best_line = [(m*i)+b for i in x]
y_mean_line = [mean(y) for i in y]

def sqrd_err(y_orig,y_line):
    return sum((y_line-y_orig)**2)

def coe_of_det(y_orig,y_line):
    sqrd_err_best_line = sqrd_err(y_orig,y_line)


    y_mean_line = [mean(y_orig) for i in y_orig]
    sqrd_err_y_mean = sqrd_err(y_orig,y_mean_line)

    return 1 - (sqrd_err_best_line / sqrd_err_y_mean)

#future_X = 8
#future_Y = (m*future_X)+b

#future_Y = 8
#future_X = (future_Y - b)/m  

r_squared = coe_of_det(y,best_line)    
plt.plot(best_line,y_mean_line)
plt.scatter(x,y)
#plt.scatter(future_X,future_Y)
plt.plot(x,best_line)
plt.show() 
print(m,b)
#print(future_X)
print(r_squared)
#plt.show to display all plots

