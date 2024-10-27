import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.xlabel('Values', fontsize=14)
plt.ylabel('Square Values', fontsize=14)
plt.title('A Simple Line Graph', fontsize = 24)
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)
plt.axis([0,1100,0,1100000])
plt.show()