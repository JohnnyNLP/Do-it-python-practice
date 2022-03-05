#Trying to find a 'gu' that has more than 3% of foreigners
import os, re, usecsv, test

test.gg('Trying to find a \'gu\' that has more than 3% of foreigners')
os.chdir(r'C:\Users\user\Desktop\파이썬\Do-it-Python\Do-it-python-practice\04 CSV 파일로 데이터 다루기')
total = usecsv.opencsv('popSeoul.csv')
usecsv.switch(total)

targetGu=[]
perGu=[]

for i in total:
    try:
        for_per = round(i[2]/(i[1]+i[2])*100, 1)
        if for_per >= 3:
            targetGu.append(i[0])
            perGu.append(for_per)
    except:
        pass

for i in range(len(targetGu)):
    print(targetGu[i], perGu[i])
    
test.gg('Save the list as a file')
new = []
new.append(['Gu', 'Koreans', 'Foreigners', 'Rate'])
for i in total:
    try:
        for_per = round(i[2]/(i[1]+i[2])*100, 1)
        if for_per >= 3:
            new.append([i[0], i[1], i[2], for_per])
    except:
        pass
usecsv.writecsv('newpopSeoul.csv', new)