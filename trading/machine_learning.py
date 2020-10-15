import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score


final_cotations = pd.read_csv("converted_cotations.csv", sep=",")



X = final_cotations[["0", "1", "2", "3", "4", "5", "6", "7", "8"]]
y = final_cotations[["9"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

model = LinearSVC()

model.fit(X_train, y_train)
predictions = model.predict(X_test)

acuracia = accuracy_score(y_test, predictions) * 100
print("A acurácia foi %.2f%%" % acuracia)