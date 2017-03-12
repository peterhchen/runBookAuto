#!/usr/bin/python3

rand_string = "     This is a random string   "

rand_string = rand_string.lstrip()

rand_string = rand_string.rstrip()

rand_string = rand_string.strip()

print (rand_string.capitalize())

print (rand_string.upper())

print (rand_string.lower())

a_list = ["A", "bunch", "of", "random", "words"]
print (" ".join(a_list))

a_list_2 = rand_string.split()
for i in a_list_2:
    print (i)


print ("String: ", rand_string)
print ("Word \"is\" indexi count: ", rand_string.count("is"))
print ("Word \"string\" position index: ", rand_string.find ("string"))
print ("\"a\" replaced by \"a kind of\":", \
        rand_string.replace ("a ", "a kind of "))
