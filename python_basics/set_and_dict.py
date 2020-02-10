# Set 
# a collection of data, unordered, not allow duplicates, mutable

# create a set
s1 = {"cat", "dog", 1024, False, 3.5}
# print(type(s1))

# Add elements to a set
s1.add("snake")
# print(s1)

# Remove element from a set
s1.discard("snake")
# print(s1)

# Total elements in a set
# print(len(s1))

# Loop through a set
# for s in s1:
#     print(s)

# union
s2 = {"red", "Blue", "green", 3.5}

u = s1 | s2
# print(u)

# intersection
i = s1 & s2
# print(i)

# difference
d = s2 - s1
# print(d)

# subset
s3 = {"dog", False}
c = s1 >= s3

# print(c)

# Dictionary
# dict: stores a key-value pair, no duplicates for keys, unordered, mutable

# Create a dict
d1 = {
    "first_name": "John",
    "last_name": "Doe"
}

# print(type(d1))
# print(d1)

# Access dict value
# print(d1["last_name"])

# Add key-value pair to dict
d1["email"] = "john.doe@gmail.com"
# print(d1)

d1["sets"] = s1
# print(d1)

# Remove a key-value pair from dict
d1.pop("sets")
# print(d1)

d2 = {
    "home": "111-111-1111",
    "work": "222-222-2222",
    "mobile": "333-333-3333"
}

d1["contact"] = d2

# print(d1)

# pretty print dict
import pprint

# pprint.pprint(d1, sort_dicts=False, indent=2)

# Loop through a dict
# for key, value in d1.items():
#     print(key, value)

# for key in d1.keys():
#     print(key)

# for value in d1.values():
#     print(value)

# Check if key exists in dict
print("address" in d1)