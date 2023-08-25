import sys
jumsu = int(input('점수입력 : '))

'''
콘솔로부터 정수값을 입력받아서
90이상이면 A
80이상이면 B
70이상이면 C
그렇지 않으면 F
'''

#if jumsu > 100:
#    print(f"{jumsu}로 점수를 잘못 입력하였습니다.")

if jumsu > 100:
    print("점수를 잘못 입력하였습니다.",file=sys.stderr)
    sys.exit(1)

match jumsu // 10:
    case 9 | 10:
        print("A")
    case 8:
        print("B")
    case 7:
        print("C")
    case _:
        print("F")
        
        
