# matplotlib is used to visualize the data according to the need of user by using given data.
import matplotlib.pyplot as plt

x = [1,2,3,4,5,5,5];
y = [23,32,43,32,2,43,33];
plt.plot(x,y, color = 'green', linewidth= 5, linestyle = 'dashed');
plt.xlabel('day');
plt.ylabel('tempreature');
plt.title('weather');
plt.show();


