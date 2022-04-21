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

from faker import Faker

faker = Faker()

mydict = {
    "name": faker.name(),
    "age": faker.random_int(min=1, max=90),
    "city": faker.city(),
}
print(mydict)

mydict2 = dict(
    name=faker.name(), age=faker.random_int(min=1, max=90), city=faker.city()
)
print(mydict2)

value = mydict.get("name")
value = mydict["age"]

mydict["email"] = faker.email()
mydict["email"] = faker.email()
mydict["email"] = faker.email()

del mydict["email"]
mydict.pop("age")
mydict.popitem()


if "age" in mydict:
    print("yes")

try:
    print(mydict["iceage"])
except:
    print("error")
