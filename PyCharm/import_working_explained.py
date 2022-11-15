# import pandas as pd
# print(pd.__version__)

##note - MODULE KESE IMPORT HOTA TO KNOW THIS THERE IS A MODULE - sys

import sys
# print(sys.path) #lists paths jahase python modules ko leke ayega

import  file2
print(file2.a)
file2.printjoke('hello')

# from file2 import a #this way is not recommended,
# # import file and use items in it, as agar file 3 mebi a var he toh usme ambiguity create hoga
# if we use this way
# print(a)

##-- lesson learnt: DO NOT USE KEYWORDS AND MODULE NAMES, RESERVED WORDS TO NAME FILES IN PYTHON.
# THIS WILL LEAD TO ERROR, IF WE USE MODULE NAME AS NAME OF FILE, as we seen PYTHON WILL TRY TO
# SEARCH IN SPECIFIC DIRECTORIES AND IT LL GET CONFUSED. N THROW ERROR