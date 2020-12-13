print(2**2) ##제곱근


#print함수
print("%5d" % 123)
print("%f" % 123.45)
print("%7.1f" % 123.45) #공백은 숫자나 문자 포함
print("%7.3f" % 123.45)

print("\n줄바꿈\n연습")
print("\t탭키\t연습")
print("글자가\'강조\'연습")
print("글자가\"강조\"연습")

var_str = "" #""는 문자열
total = 213
print(type(var_str))
print(type(total))
print("%d 이건 임의로 만든 문자열" % total)

var_str = "123"
var_str = "문자열"
var_int = 100
var_int = 100+100
print(var_str)
print(var_int)

var_int = 200
var_int = var_int+100
print(var_int)

var_str = "100"
print(int(var_str)+1)

var_str = input()
print(var_str)



#동전나머지 구하기

stor = 0

stor = int(input("교환할 금액을 입력하세요: "))

print("500원짜리 %d개" % (stor // 500))
stor = stor % 500

print("100원짜리 %d개" % (stor // 100))
stor = stor % 100

print("50원짜리 %d개" % (stor // 50))
stor = stor % 50

print("10원짜리 %d개" %(stor // 10))
stor = stor % 10

print("나머지 %d원" % stor)



#사칙연산
a, b =3, 5
print("덧셈 : %d" % (a + b))
print("뺄셈 : %d" % (a - b))
print("곱셈 : %d" % (a * b))
print("나눗셈 : %.1f" % (a / b))



#카페매출계산
am = 0
cl = 0
cp = 0

am =int(input("아메리카노 판매 개수 : "))
am = am * 2000
cl =int(input("카페라떼 판매 개수 : "))
cl = cl * 3000
cp =int(input("카푸치노 판매 개수 : "))
cp = cp * 3500

print("총 매출은 %d 입니다." % (am + cl + cp))



#bmi

h = int(input("키 : ")) /100
w = int(input("몸무게 : "))
bmi = w / (h ** 2)
print("bmi : %d" % bmi)



#몫, 나머지 구하기

s = int(input("분자를 입력하세요: " ))
m = int(input("분모를 입력하세요: " ))
print("나눗셈의 몫 : %d" % (s//m))
print("나눗셈의 나머지 : %d" % (s%m))