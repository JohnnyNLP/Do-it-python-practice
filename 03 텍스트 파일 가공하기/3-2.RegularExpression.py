def gg():
    print("****************************")
    
import re

example = "Movies can only be either interesting or bad(Johnny, 2022). Oh, at last(Johnny, 2023)!"
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
gg()

### findall method
### re.findall('pattern', 'target string')
### returns results in []
number = 'My favorite numbers are 12523.12 and 623416.23 and 23534.70'
print(re.findall('\d{5}', number))
gg()

### comma in regular expressions means all
### to stop at certain point, add a question mark
example1 = 'I was born in Seoul in 1996. And my military service ends in 2023.'
print(re.findall(r'in+\s\d.+\.', example1))
print(re.findall(r'in+\s\d.+?\.', example1))
print(re.findall(r'\(.+\)', example))
print(re.findall(r'\(.+?\)', example))
gg()

### split method
### re.split('pattern', 'string')
example2 = 'Today I lost two games of LOL in a row. What kind of jerks are playing this game? I can\'t believe this is happening to me!'
print(re.split(r'[.!?]', example2))
data = 'a:1; b:2; c:3'

print(re.split(r';', data))
for i in re.split(r';', data):
    ### returns [a:1, b:2, c:3]
    print(re.split(r':', i))
gg()
### sub method
### re.sub('pattern', 'substitution', 'string')
print(re.sub('LOL', 'Warcraft', example2))
example3 = 'I wanna\n\nsleep in tomorrow.\n\n\n\nBut I gotta work...'
print(example3)
print(re.sub('\n','',example3))
gg()

example4 = 'Usually the words that end with ''ly'' is adverb. But friendly and lovely are adjectives.'
print(re.findall(r'\S+ly', example4))