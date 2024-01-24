
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB


df1 = pd.read_csv(r'SampleData/banknote.csv')
print("DF1 :\n", df1)
print("DF1 Type: ", type(df1))

features = df1[['X1','X2','X3','X4']]
features = features.to_numpy()
print("\nFeatures:\n", features)
print("Features type: ", type(features))

label = df1[['S']]
label = label.to_numpy()
label = label.ravel()
print("\nLabel:\n", label)
print("\nLabel type: ", type(label))
print("\nLabel shape:\n", label.shape)

#Create a Gaussian Classifier
model = GaussianNB()
# Train the model using the training sets
model.fit(features,label)

#Predict Output
xp = [-2.54190,  -0.65804,   1.6842,  1.19520];
predicted= model.predict([xp])
print("\n\nPredicted Value: ", predicted)