import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

# data load
inputFolder = './data/'
df = pd.read_csv(inputFolder + 'iris.csv')
print(df.head())

X = df.loc[:, df.columns != 'variety']
y = df['variety']

# data split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.25)


# modeling
model = RandomForestClassifier()
model.fit(X_train, y_train)
# print score
print("Model score",model.score(X_train,y_train))

# predict X_test data
predictions = model.predict(X_test)

# scoring
print(accuracy_score(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

# saving model

pickle.dump(model, open('./output/randomforest_model.pkl', 'wb'))
