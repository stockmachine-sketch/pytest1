#반복문&break문 : 1~100 사이 홀수의 합에서 최초로 600이 넘는 위치
i, hap = 0, 0

for i in range(1, 100, 2):
    hap += i

    if hap >= 600 :
        break

print("1~100 사이 홀수의 합에서 최초로 600이 넘는 위치 : %d" % i)
