# mytuple = "Max", 28, "Boston"
# # or mytuple = ("Max", 28, "Boston")
# # if you want a tuple with one element mytuple = ("Max",)


# # can be created from a list
# mytuple = tuple(["Max", 28, "Boston"])

# print(type(mytuple))
# print(mytuple)

# item = mytuple[-1]

# # tuple is immutable
# # mytuple[0] = "pong"  # brings error
# print(mytuple[0])

# # for i in mytuple:
# #     print(i)


# if "Max" in mytuple:
#     print("yes")
# else:
#     print("no")

# print(mytuple.count("tim"))

# print(mytuple.index("Max"))
# # print(mytuple.index("Tim")) # raises error is not found

# #####

# mytuple2 = ("a", "p", "p", "l", "e")
# print(mytuple2.count("p"))
# print(mytuple2.count("o"))

# my_list = list(mytuple2)
# print(my_list)

# mytuple2 = tuple(my_list)
# print(mytuple2)

# #####
# # tuple slicing
# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# b = a[2:5]
# print(b)

# #####
# # unpacking

# mytuple = ("Max", 28, "Boston")

# name, age, city = mytuple
# print(name)
# print(age)
# print(city)

# mytuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# i1, *i2, i3 = mytuple

# print(i1)
# print(i2)
# print(i3)


# #####
# # tuple takes less space in memory and it's more efficient to iterate over it
# import sys

# my_list = [0, 1, 2, "hello", "world", 3.14]
# mytuple = (0, 1, 2, "hello", "world", 3.14)
# print(sys.getsizeof(my_list))
# print(sys.getsizeof(mytuple))


# ### times to iterate over a tuple and listp
# import timeit


# print(timeit.timeit(stmt='[0, 1, 2, "hello", "world", 3.14]', number=1000000))
# print(timeit.timeit(stmt='(0, 1, 2, "hello", "world", 3.14)', number=1000000))


#######################################################################
### Dictionary: key-value pairs, unordered, mutable

# from faker import Faker

# faker = Faker()

# mydict = {
#     "name": faker.name(),
#     "age": faker.random_int(min=1, max=90),
#     "city": faker.city(),
# }
# print(mydict)

# mydict2 = dict(
#     name=faker.name(), age=faker.random_int(min=1, max=90), city=faker.city()
# )
# print(mydict2)

# value = mydict.get("name")
# value = mydict["age"]

# mydict["email"] = faker.email()
# mydict["email"] = faker.email()
# mydict["email"] = faker.email()

# del mydict["email"]
# mydict.pop("age")
# mydict.popitem()


# if "age" in mydict:
#     print("yes")

# try:
#     print(mydict["iceage"])
# except:
#     print("error")


# for value in mydict.values():
#     print(value)

# for key in mydict.keys():
#     print(key)

# for key, value in mydict.items():
#     print(key, value)

# # when creating a copy of a dictionary, make sure use the copy() method
# mydict3 = mydict.copy()

# mydict3["email"] = faker.email()
# print(mydict3)
# print(mydict)

# # another way to create a copy of a dictionary is to use the dict(dict_to_copy) method

# # to merge two dictionaries
# mydict.update(mydict3)  # it merges and overwrites

# # we can  use tuples as keys, but not list
# mytuple = (8, 7)
# mydict = {mytuple: 15}
# mydict


# #######################################################################
# ##### Sets: unordered, mutable, unique
# myset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10}
# print(myset)

# myset = set([2, 4, 6, 8, 10])
# print(myset)

# # empty set
# myset = set()

# myset.add(2)
# myset.add(4)
# myset.add(6)

# print(myset)

# # remove
# myset.discard(0)
# myset.discard(2)

# # to empty a set
# myset.clear()

# odds = set([1, 3, 5, 7, 9])
# evens = set([2, 4, 6, 8, 10])
# primes = set([2, 3, 5, 7])

# u = odds.union(evens)

# i = odds.intersection(evens)
# i

# i = odds.intersection(primes)
# i

# i = evens.intersection([2, 3, 4, 4, 5, 6, 7, 8, 9, 10])
# i

# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# setB = {1, 2, 3, 10, 11, 12, 13, 14, 15, 16}

# diff = setA.difference(setB)
# diff

# diff = setA.symmetric_difference(setB)
# diff

# setA.update(setB)  # changes/updates setA with the missing from setB

# setA.intersection_update(setB)  # updates with common elements

# setA.difference_update(setB)  # updates with elements in setA but not in setB

# setA.symmetric_difference_update(
#     setB
# )  # updates with elements in setA or setB but not both


# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# setB = {1, 2, 3}

# setB.issubset(setA)

# setA.issuperset(setB)

# setA.isdisjoint(setB)  # check if there are no common elements


# setB = setA.copy()  # make a copy of setA
# setB = set(setA)  # make a copy of setA

# # frozen set: immutable set

# a = frozenset([1, 2, 3, 4, 5])
# a.add(6)

################################
### String


import pandas as pd

# using dask delayed to take my custom function below, but run it in parallel
from dask import delayed
from dask.distributed import Client, progress

# here you can define number of workers to be made for parallel processing (each worker will handle one file/process)
# like this: `client = Client(n_workers=100, threads_per_worker=1)`
# I am leaving it empty to have workers equal to the number of cores on my machine
client = Client()
# having a look at dask dashboard which shows progress of parallel tasks (see dask documentation on it and a photo below)
client


import duckdb

cursor = duckdb.connect(
    database="/code/adv_python_training/data/13f_filings.duckdb", read_only=False
)


# cursor.execute(
#     "CREATE TABLE main AS SELECT * FROM \
#         read_csv_auto('/code/adv_python_training/data/filings_13f_main.csv', \
#         NULLSTR=NULL, NULLSTR='', dateformat='%Y/%m/%d')"
# )

# cursor.execute(
#     "CREATE TABLE main AS SELECT * FROM \
#         read_csv_auto('/code/adv_python_training/data/filings_13f_xml_flag.csv', \
#         NULLSTR=NULL, NULLSTR='', dateformat='%Y/%m/%d')"
# )

cursor.execute("DROP TABLE IF EXISTS duckdb_xml_flag")

cursor.execute(
    "CREATE OR REPLACE TABLE duckdb_xml_flag \
        (accessionNumber VARCHAR PRIMARY KEY, \
        cikManager VARCHAR, \
        managerName VARCHAR, \
        submissionType VARCHAR, \
        filedAsOfDate DATE, \
        periodOfReport DATE, \
        report_Quarter VARCHAR, \
        report_Year VARCHAR, \
        xml_flag VARCHAR, \
        created_at TIMESTAMP)"
)

cursor.execute(
    "COPY duckdb_xml_flag FROM \
    '/code/adv_python_training/data/filings_13f_xml_flag.csv' ( AUTO_DETECT TRUE )"
)


#     AS SELECT * FROM \
#         read_csv_auto('/code/adv_python_training/data/filings_13f_xml_flag.csv')"
# )


cursor.execute("SELECT * FROM duckdb_xml_flag").fetchone()
print(cursor.description)

# filedAsOfDate=DATE,\
# report_Year=INTEGER,\
# report_Quarter=INTEGER,\
# cikManager=INTEGER,\


# cursor.execute(
#     "COPY (SELECT * FROM read_csv_auto('/code/adv_python_training/data/filings_13f_main.csv', NULLSTR='NULL', ALL_VARCHAR=1)) \
#                 TO 'main.parquet'"
# )


cursor.commit()
cursor.close()
# PRAGMA memory_limit='20GB';
# PRAGMA threads=10;
