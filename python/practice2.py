import re

name_file = open("names.txt", encoding="utf-8", mode="r")
data = name_file.read()
name_file.close



# .match() matches a set of characters starting at the beginning of string

# print(re.match(r'Hawkins', data))
# print(re.match(r'Derek', data))

# print(re.findall(r'\D*\d{3}\D*\d{3}\D\d{4}',data))

# print(re.findall(r'\w+@\w+.\w+',data))
# print(re.findall(r'[-\w+.]+@codingtemple.com',data))
# print(re.findall(r'[Teachr]{7}',data))

# def num_digits(count,string):
#     return re.findall(r'',string) 

# print(num_digits(4,data))


# print(re.findall(r'''
#     \b@[-\w\d+.]+ 
#     [^gov\t]+
#     \b
# ''',data, re.X|re.I))

# print(re.findall(r'''
#     \b@[-\w\d+.]+ # match a boundary, an @ symbol and then 1+ number of characters
#     [^gov\t]+ # exclude instances of 'g', 'o', 'v', or 't' and a tab
#     \b # match a word boundary
# ''', data, re.X|re.I))


# grouping
info = re.compile(r'''
    ^([-\w ]*,\s[-\w ]+)\t # last and first names
    ([-\w\d.+]+@[-\w\d.]+)\t # email
    (\(?\d{3}\)?-?\s?\d{3}-\d{4})\t # phone
    ([\w\s]+,\s[\w\s.]+)\t? # job and company
    (@[\w\d]+)?$ # twitter
    ''',re.X|re.M)

for i in info.finditer(data):
    print(i.group("name"))