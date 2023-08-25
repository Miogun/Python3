'''
점수값 하나를 입력 받아서 소수인가? 아닌가를 판단하세요
소수인 경우 : 소수입니다.
소수가 아닌 경우 : 소수가 아닙니다.
'''

N = int(input('정수입력 : '))
is_sosu = True

# 소수이면 is_sosu = False

for i in range(2, N):
    if N % i == 0:
        is_sosu = False
        break
    
if is_sosu:
    print("소수 입니다.")
else:
    print("소수가 아닙니다.")
