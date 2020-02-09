# List
# mutable, ordered sequence, allows duplicates

# define a list
l = ["cat", "dog"]

l2 = ["cat", "dog", 9000, False, 8.12]

# access list elements
# print(l2[-1])

# get the total number of elements of a list
# print(len(l2))


# range
# l3 = l2[:3]
# print(l3)


# check if an element exists in the list
# print("snake" in l2)


# loop through a list
# for x in l2[::2]:
#     print(x)


# Insert elements to a list
# l2.append("snake")
# l2.insert(2, "snake")
# print(l2)


# Combine two lists into one
# l3 = l + l2
l.extend(l2)
# print(l)

# Remove element from a list
# l.remove("dog")
l.pop(4)
# print(l)

# print(l2)


# Tuple

# immutable, ordered sequence, allows duplicates

# define a tuple
t1 = ("cat", "dog", 9000, False, 8.12)
t2 = ("cat",)
# print(t1, t2)

# access tuple element
# print(t1[3])

# range
# print(t1[2:])

# loop a tuple
# for t in t1:
#     print(t)

# length of a tuple
print(len(t1))