import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.DataFrame([
	[0.1, 0.6],
	[0.15, 0.71],
	[0.24, 0.1],
	[0.3, 0.2],
    [0.08, 0.9],
    [0.16, 0.85],
    [0.2, 0.3],
    [0.25, 0.5]

])

model = KMeans(n_clusters = 2)
label = model.fit_predict(data)

centroids = model.cluster_centers_
c = ['red', 'blue','black']
print(centroids)
print(label)

plt.scatter(centroids[:,0] , centroids[:,1], color ='black')

for i in range(0, len(data[0])):
	plt.scatter(data[0][i], data[1][i], color=c[label[i]])
		
plt.show()
