import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([[10], [9], [2], [15], [10], [16], [11], [16]])
y = np.array([[95], [80], [10], [50], [45], [98], [38], [93]])

model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)
a =int(input("Enter"))
print("y=%f*%f+%f" %(model.coef_,a,model.intercept_))
plt.scatter(x, y, color ='blue')
plt.plot(x, y_pred, color ='black')
plt.show()

