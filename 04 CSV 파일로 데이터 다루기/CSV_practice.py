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