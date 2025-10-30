# Importing essential libraries
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
# Importing Performance Metrics:
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import pickle
import warnings
warnings.filterwarnings('ignore')

# Loading the dataset
df = pd.read_csv('../dataset/Liver_data.csv')

# Filling NaN Values of "Albumin_and_Globulin_Ratio" feature with Median :
df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(df['Albumin_and_Globulin_Ratio'].median())

df['Gender'] = np.where(df['Gender']=='Male', 1, 0)

df = df.drop('Direct_Bilirubin', axis=1)

columns = ['Total_Bilirubin','Alkaline_Phosphotase','Alamine_Aminotransferase','Aspartate_Aminotransferase','Albumin_and_Globulin_Ratio']

for col in columns :
    # Lets compute the Interquantile range of feature to calculate the boundaries:
    IQR = df[col].quantile(0.75)-df[col].quantile(0.25)
    # Extreme outliers
    lower_bridge = df[col].quantile(0.25) - (IQR*3)
    upper_bridge = df[col].quantile(0.75) + (IQR*3)

    # if value greater than upper bridge, we replace that value with upper_bridge value:
    df.loc[df[col] >= upper_bridge, col] = upper_bridge

# Model Building
from sklearn.model_selection import train_test_split
X = df.drop(columns='Dataset')
y = df['Dataset']

# SMOTE Technique:
from imblearn.combine import SMOTETomek
smote = SMOTETomek()
X_smote, y_smote = smote.fit_resample(X,y)

# Train Test Split:
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_smote,y_smote, test_size=0.3, random_state=33)

# Creating model using best parameter of GridSearchCV:
classifier = RandomForestClassifier(criterion='entropy', n_estimators=1950, max_depth=150, max_features='log2', 
                                             min_samples_split=2, min_samples_leaf=1)
classifier = classifier.fit(X_train,y_train)

# Predictions:
y_pred = classifier.predict(X_test)

# Performance:
print('Accuracy:', accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

# Creating a pickle file for the classifier
filename = './liver-prediction-rfc-model.pkl'
pickle.dump(classifier, open(filename, 'wb'))