count = 1
def title(title):
    global count
    print('********* ', count,'. ',title," : ****************************")
    count += 1
    return count

# new module : csv
import csv, os
os.chdir(r'C:\Users\user\Desktop\파이썬\Do-it-Python\Do-it-python-practice\04 CSV 파일로 데이터 다루기')
f=open('a.csv', 'r')

title('csv module')
new = csv.reader(f)
print(new)
for i in new:
    print(i)

title('csv to list')
f.seek(0)
a_list = []
for i in new:
    print(i)
    a_list.append(i)
    
print(a_list)
f.close()

title('def opencsv')
def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output

print(opencsv('a.csv'))

title('write csv')
a= [['district', 'total population', 'residents', 'foreingers'],
['Gwanak-gu', '519864', '502089', '17775'],
['Gangnam-gu', '547602', '542498', '5104'],
['Songpa-gu', '686181', '679247', '6934'],
['Gangdong-gu', '428547', '424235', '4312']]

f = open('abc.csv', 'w', newline='')
csvobject=csv.writer(f, delimiter =',')
csvobject.writerows(a)
f.close()

title('def writecsv')
def writecsv(filename, the_list):
    with open(filename, 'w', newline = '') as f:
        a = csv.writer(f, delimiter = ',')
        a.writerows(the_list)
        
writecsv('def.csv', a)