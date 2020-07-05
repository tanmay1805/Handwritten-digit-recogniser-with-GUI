import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score


mnist = fetch_openml('mnist_784')
x , y = mnist['data'] , mnist['target']
x_train , x_test = x[:60000] , x[60000:]
y_train , y_test = y[:60000] , y[60000:]
shuffleindex = np.random.permutation(60000)
x_train , y_train = x_train[shuffleindex] , y_train[shuffleindex]
y_train = y_train.astype(np.int8)
y_test = y_test.astype(np.int8)
model = LogisticRegression()
model.fit(x_train,y_train)
model.predict([x[0]])
a = cross_val_score(model , x_train , y_train , cv=3 , scoring="accuracy")
a.mean()
pred = model.predict(x_test)
print(r2_score(y_test, pred).round(2))
file = open('model.pkl','wb')
pickle.dump(model,file)
file.close()