# classes = template
# object = instance of the class

# DRY pricipal - DO NOT REPEAT YOURSELF
# using classes saves time. money and efforts,repetability kam kerte he, code ko jada organise krte he,
# to restrict access of functions when required
# example given - get_no_of_films(srk) if a youtuber is passed as argument or some abnormal input
# like table is passed then function should not run it should only run for actors

class Student:
    pass
harry = Student() #class instance
larry = Student()

harry.name = 'jumma' #instance variables
harry.age = 34
larry.subjects = ['maths', 'geography']

print(harry, larry)
print(harry.age, larry.subjects)
