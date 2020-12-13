#조건문 만들기
bool_Data = False
a = 7

if bool_Data == False :
    print("거짓")

#if type(a) = int :
#    print("숫자입니다")



#계산기

choose, a, b, result = 0, 0, 0, 0


choose = input("연산자를 고르세요.\n 1 : 덧셈, 2 : 뺄셈, 3 : 곱셈, 4 : 나눗셈\n ")
a = int(input("첫번째 갑을 입력하세요 : "))
b = int(input("두번째 갑을 입력하세요 : "))

if choose == '1':
    result = a + b
    print(result)
elif choose == '2':
    result = a - b
    print(result)
elif choose == '3':
    result = a * b
    print(result)
elif choose == '4':
    result = a / b
    print(result)
else:
    result = "1, 2, 3, 4 중에서 입력하세요"
    print(result)


#1부터 100까지 합 구하기
int_sum, i = 0, 0

for i in range(0, 101 , 1):
    int_sum = int_sum + i

print(int_sum)



#피보나치 수열

int_result = 0
int_a = 1
int_sum = 0

for i in range(1, 11, 1):
    print(int_result, end=" ")
    int_sum = int_result + int_a
    int_result = int_a
    int_a = int_sum