import matplotlib
print(matplotlib.__version__)      
import matplotlib.pyplot as plt
x=[1, 2, 3, 4,]
y=[10, 20, 25, 30]
plt.plot(x, y)
plt.show()
plt.plot(x, y, marker='o', linestyle='--', color='r')   
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Customizations')
plt.grid()
plt.show()

