import os, usecsv
os.chdir(r'C:\Users\user\Desktop\파이썬\Do-it-Python\Do-it-python-practice\04 CSV 파일로 데이터 다루기')
a = [['Korean', 'English', 'Math'], [99, 88, 77]]
usecsv.writecsv('test.csv', a)