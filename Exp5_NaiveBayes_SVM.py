import pandas as pd
from sklearn import svm
import numpy as np

df_1 = pd.read_csv( r'SampleData/banknote.csv')
print("\n\ndf1:\n", df_1)
print("\ndf1 type: ", type(df_1))

features = df_1[['X1', 'X2','X3','X4']] #double square brackets -> data frame for pandas
features = features.to_numpy()
print("\n\nFeatures:\n", features)
print("Features type: ", type(features))

label = df_1[['S']]
label = label.to_numpy()
label = label.ravel()
print("\nLabel:\n", label)
print("Label type: ", type(label))
print("Label shape: ", label.shape)

#creating classifiers:
model1 = svm.SVC()

#Training models w/ training sets
model1.fit(features,label)

#predict output:
xp = [-2.123131, 0.53523, 1.53353, 1.14141]
predicted1 = model1.predict([xp])
print("Predicted value - model.L1:  ", predicted1)