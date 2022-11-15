# search for UCI ML repo and visit
# open most popular dataset iris
# check iris.data and iris.name - watch video for further details


import requests
import pickle

file = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
open("iris.data","wb").write(file.content) #this step is important
# print(file)
ls= []
with open("iris.data") as filehandle:
    f= filehandle.readlines()

# ls = f
# print(ls)
sepal = "sepal.pkl"
sepal_w = open("sepal.pkl", "wb")
pickle.dump(f,sepal_w)
sepal_w.close()

sepal_r = open("sepal.pkl", "rb")
iris = pickle.load(sepal_r)
print(iris)