def gg():
    print("****************************")
    
import re

example = "Johnny said movies can only be either interesting or bad, and there's nothing like in between. (Johnny, 2022)"
result = re.findall(r'\([A-Za-z가-힣]+, \d+\)', example)
print(result)
gg()

### match method
### re.match('pattern', 'string')
### match() finds the target string from the start of the pattern!!
pattern = r'life'
script = 'life'
print(re.match(pattern, script))
print(re.match(pattern, script).group())
gg()

### example
def refinder(pattern, script):
    if re.match(pattern, script):
        print('Match!')
    else:
        print('Not a Match!')

pattern = r'Life'
script = 'Life is so cool'
refinder(pattern, script)

pattern = r'is'
script = 'Life is so cool'
refinder(pattern, script)
gg()

### search method
### re.search('pattern', 'string')
### search() finds the target string within the whole pattern
def refinder(pattern, script):
    if re.search(pattern, script):
        print('Match!')
    else:
        print('Not a Match!')
refinder(pattern, script)
