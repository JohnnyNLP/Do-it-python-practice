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

title('csv number process')
import re, usecsv
os.chdir(r'C:\Users\user\Desktop\파이썬\Do-it-Python\Do-it-python-practice\04 CSV 파일로 데이터 다루기')
total = usecsv.opencsv('popSeoul.csv')
for i in total [:5]:
    print(i)
    
title('number conversion to float')
k=[]
for i in total:
    for j in i:
        if re.search('\d', j):
            k.append(float(re.sub(',','',j)))
        else:
            k.append(j)
print(k)

title('converting even without k')
print(total)
for i in total:
    for j in i:
        if re.search('[A-Za-z]', j):
            i[i.index(j)] = j
        else:
            i[i.index(j)] = (float(re.sub(',', '', j)))
print(total)

title('using try-except to prevent errors')
total[1][1] = '9,740,398!'
total[1][2] = '285,529명'
total[1][3] = '1,498,146s'
for i in total:
    for j in i:
        try:
            i[i.index(j)] = (float(re.sub(',', '', j)))
        # if error happens here, i[i.index(j)] has characters that are not numbers
        except:
            pass
print(total)
