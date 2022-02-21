def gg():
    print("****************************")
    
### os module
import os
print(os.getcwd())
os.chdir(r'C:\Users\user\Desktop\파이썬\Do-it-Python\Do-it-python-practice\03 텍스트 파일 가공하기')
print(os.listdir())
gg()

### File write/read/add
f = open('a.txt', 'w')
f.write('Once upon a time a rich named Johnny lived.\n')

f = open('a.txt', 'r')
print(f.read())
f.seek(0)
line = f.read()
print(line)
print(line[:5])
f.close()

f = open('a.txt', 'a')
f.write('And he had a beautiful cat too.\n')
f.close()
f = open('a.txt', 'r')
print(f.read())
gg()

### With function
with open('a.txt', 'a') as f:
    f.write('Johnny''s favorite whisky is Johnny walker, of course.')

### codecs module
import codecs
f = codecs.open('a.txt', 'r', 'utf-8')
print(f.read())
