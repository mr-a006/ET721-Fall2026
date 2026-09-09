"""
lab 3: introduction to Python Basics
Aqeel Hussain
Sep 9, 2026
"""
print("------- Example 1: strings -------")
name = "Michael Jackson"
print(name[::2])
print(name[0:5:2])
#print(name[3:10:2])
print("------- Example 2: string methods -------")
name1 = name.upper()
name2 = name.lower()
name3 = name.replace('Michael', 'Janet')
indexname = name.find('Jack')
print(f'Name in uppercase {name1}')
print(f'Name in lowercase {name2}')
print(f'Index for Jack = {indexname}')
print(f'split name = {name.split()}')

print("------- Example 3: regular expression -------")
#import the modle for regular expression, re
import re

s1 = "Michael Jackson is the best"
# define the pattern to search for
pattern = r"Jackson"
# use the search() function to search for the pattern in the string
result = re.search(pattern, s1)
# print result
print(f"The pattern result is = {result}")
if result:
    print("Match found")
else:
    print("Match not found")

pattern = r"\d\d\d\d\d" # matches any five consecutive digits
zipcode = "My zip code is = 12345 and my lucky number is 8"
match = re.search(pattern,zipcode)
if match:
    print(f"Zip code found = {match.group()}")
else:
    print("Zip code NOT found")

print("------- Example 4: tuples -------")
# create a tuple
tuple1 = ("disco", 10, 1.2)
print(type(tuple1))
print(f"Second element = {tuple1[1]}")
print(f"Second element = {tuple1[-1]}")
print(f"There are {len(tuple1)} elements in the tuple")

rating = (0,3,4,9,7)
print(f"Sorted tuple = {sorted(rating)}")

# nested tuple
nestedtuple = (1,2, ("pop","rock"), (3,4), ("disco", (8,9)))
print(f'original tuple = {nestedtuple}')
print(f"Nested tuple = {nestedtuple[2]}")
print(f"Nested subtuple = {nestedtuple[3][1]}")
print(f"Nested sub-subtuple = {nestedtuple[4][1][0]}")

print("------- Example 5: dictionary -------")
# create a dictionary
release_year_dict = {
    "Thriller" : 1982,
    "Back in Black" : 1980,
    "The Dark Side of the Moon" : 1973,
    "The Bodyguard" : 1992,
    "Rumours" : 1977
}

# get the value of a key
print(f"Year of The Bodyguard = {release_year_dict["The Bodyguard"]}")
print(f"All keys = {release_year_dict.keys()}")

# add or update an entry in a dictionary
release_year_dict["Graduation"] = 2007

# print all the keys
print(f"All keys = {release_year_dict.keys()}")

print("------- Example 6: sets -------")
# has no order, and automatically remove duplicate items
# create set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "disco", "rock"}
print(set1)
check1 = "AC/DC" in set1
print(f"Is AC/DC in genres? {check1}")
# add an element
set1.add("AC/DC")
check1 = "AC/DC" in set1
print(f"Is AC/DC in genres? {check1}")

album1 = {"Thriller", "Rumours", "Back in Black"}
album2 = {"Rumours", "The Dark Side of the Moon", "Back in Black"}
#intersections, &, returns the elements that are in both sets
print(album1 & album2)
# union, |, returns the element of both sets
print(album1 | album2)
# difference, ^ ,  returns the elements that are in set but not in the other set
print(album1 ^ album2)