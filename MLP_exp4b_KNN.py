from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, f1_score
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# True labels (ground truth)
y_true = np.array([0, 1, 1, 0, 1, 0, 0, 1, 0, 1])

# Predicted labels (model predictions)
y_pred = np.array([0, 1, 1, 1, 0, 0, 0, 1, 0, 1])

# Calculate the confusion matrix
conf_matrix = confusion_matrix(y_true, y_pred)

# Extract values from the confusion matrix
tn, fp, fn, tp = conf_matrix.ravel()
# Calculate Accuracy
accuracy = accuracy_score(y_true, y_pred)
# Calculate sensitivity and specificity
precision= tp / (tp + fp)
sensitivity = tp / (tp + fn)
specificity = tn / (tn + fp)

f1 = f1_score(y_true, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
print(f'Precision: {precision:.2f}')
print(f'Sensitivity: {sensitivity:.2f}')
print(f'Specificity: {specificity:.2f}')
print(f'F1-Score: {f1:.2f}')

# visualize the confusion matrix using a heatmap

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()
