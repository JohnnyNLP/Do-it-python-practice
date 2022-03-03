def gg():
    print("****************************")

# directory setting    
import os, re
os.chdir(r'C:\Users\user\Desktop\파이썬\Do-it-Python\Do-it-python-practice\03 텍스트 파일 가공하기')
print(os.getcwd())
gg()

# file load
f = open('friends101.txt', 'r', encoding='utf8')
script101 = f.read()
print(script101[:100])
gg()

# only extract Monica's lines
Line = re.findall(r'Monica:.+', script101)
for item in Line[:3]:
    print(item)
f.close()
gg()

# save extracted lines 
f = open('monica.txt', 'w', encoding = 'utf8')
monica=''
for i in Line:
    monica += i+'\n'
f.write(monica)
f.close()
# extract character names
# in the script every line starts with 'character :' format
char=re.compile(r'[A-Z][a-z]+:')
print(re.findall(char, script101))
gg()

# to remove duplicated names, use 'set' data type
names = set(re.findall(char, script101))
print(names)
gg()

# to remove ":", change the 'set' to a 'list'
characters = []
for i in list(names):
    characters += [i[:-1]]
print(characters)
gg()

# to make it simpler, one can also condense everything above into a single code
characters = [x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+:', script101)))]
print(characters)
gg()

# What if I want to remove the 'directions' from the lines?
# They start with '(' and ends with ')'
f = open('monica_except_directions.txt', 'w', encoding = 'utf8')
monica_except_directions=''
# test = 'Monica: (explaining to the others) Carol moved her stuff out today.'
# test = re.sub(r'\s\(.+\)', '', test)
# print(test)
for i in Line:
    i = re.sub(r'\s\(.+\)', '', i)
    monica_except_directions += i +'\n'
# print(monica_except_directions)
f.write(monica_except_directions)
f.close()
gg()


