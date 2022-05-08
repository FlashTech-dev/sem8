import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

data = pd.DataFrame([
    ["<21"	, "High"	, "Male"	, "Single"	, "No"],
	["<21"	, "High"	, "Male"	, "Marrid"	, "No"],
	["21-35", "High"	, "Male"	, "Single"	, "Yes"],
	[">35"	, "Medium"	, "Male"	, "Single"	, "Yes"],
	[">35"	, "Low"		, "Female"	, "Single"	, "Yes"],
    ["<21"	, "Low"		, "Female"	, "Married"	, "Yes"],
])

x = data.iloc[:,0:4]
y = data.iloc[:, -1]

x_encode = LabelEncoder()
y_encode = LabelEncoder()

x = x.apply(x_encode.fit_transform)
y = y_encode.fit_transform(y)

model = DecisionTreeClassifier()
model.fit(x,y)
y_pred = model.predict(x)

print("X:",x)
print("Y:",y)
print("Predicted Y is:",y_pred)
