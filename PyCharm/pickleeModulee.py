import pickle
#NOTE- everything in python is object

#------------------------- pickling a python obj - serialising obj----------------------
# cars = ['Audi', 'BMW', "Maruti Suzuki", "Harryti Tuzuki"]
# file = "mycar.pkl"
# fileobj = open(file, "wb") #wb- write binary mode
# pickle.dump(cars, fileobj)
# fileobj.close()


#------------------------- Unpickling a python obj - deserialising----------------------
# file = 'mycar.pkl'
# fileobj = open(file, "rb") #read binary mode
# mycar = pickle.load(fileobj)
# print(mycar)
# print(type(mycar))


#------------------------DUMPS AND LOADS ----------------------------------------------
# initializing data to be stored in db
omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 'age' : 21, 'pay' : 40000}
jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak', 'age' : 50, 'pay' : 50000}

# database
db = {}
db['Omkar'] = omkar
db['Jagdish'] = jagdish

# For storing
b = pickle.dumps(db)	 # type(b) gives <class 'bytes'>
print(type(b))

# For loading
myEntry = pickle.loads(b)
print(myEntry)
print(type(myEntry))

