# print("hello")
import pandas as pd
from sklearn import linear_model
import pickle

df=pd.read_csv("G:\covid detector\covid\detector\data.csv")

x=df[['fever','bodyPain','age','runnyNose','diffBreath']]
y=df['infectionProb']


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test =train_test_split(x,y,train_size=0.9)


model=linear_model.LinearRegression()
model.fit(X_train,y_train)

file=open('model.pkl','wb')
pickle.dump(model,file)

file.close()
