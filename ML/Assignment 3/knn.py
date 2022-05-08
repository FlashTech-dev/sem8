import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

x = pd.DataFrame([[2, 4], [4, 2], [4, 4], [4, 6], [6, 2], [6, 4]])
y = pd.DataFrame(["square", "square", "circle", "square", "circle", "square"])

y_encode= LabelEncoder()
y=y_encode.fit_transform(y)

print(x)
print(y)

model= KNeighborsClassifier(n_neighbors=3)
model.fit(x,y)
y_pred = model.predict(pd.DataFrame([[6,6]]))
print(y_pred)

colors = ['red','blue']

for i in range (0 , len(x[0])):
    plt.scatter(x[0][i],x[1][i], color=colors[y[i]])

plt.scatter(6,6,color=colors[y_pred[0]])
plt.show()