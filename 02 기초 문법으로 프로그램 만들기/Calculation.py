def gg():
    print("****************************")
   
#100 미만에서 7의 배수  찾기
for i in range(100):
	if i%7 ==0:
		print(i)
gg()

#round 함수
avgage=(50+45+33+39+29+30)/6
print(avgage)
print(round(avgage,1))
gg()

#구구단 연습
number = [1,2,3,4,5,6,7,8,9]
for i in number:
    print(2 * i)
gg()

#구구단 심화
for i in range(2, 10):
    print (i,"단")
    for j in range(1, 10) :
        print ('%d X %d = %d'%(i, j, i*j))
gg()

#lambda로 부가세 구하기
def service_price():
    service = float(input('서비스 가격을 입력하세요: '))
    valueAdded = input('부가세를 포함합니까? y/n ')
    if valueAdded is 'y':
       print('%d원 입니다' %service)
    else:
       print('%d원 입니다' %(service*1.1))

service_price()
