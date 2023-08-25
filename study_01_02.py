# names = ['홍길동','이순신','심청이']
# i = 0
# while i < 3:
#    print(names[i])
#    print("%d번째 : %s" % (i,names[i]))
#    print(i, "번째 :", names[i])
#    print("{}번째 : {}".format(num=i,name=names[i]))
#    print(f"{i}번째 : {names[i]}")
#    i += 1
#    if i == 3:
#        break
#else:
#    print("총 %d명이 출력되었습니다." %i)
   
# %d = 형식문자, %d = 10진수 정수 %f = float, %x = 16진수 %s = 문자열 %o = 8진수
# len(names)

# names = "ABCDE" # A B C D E
# names = ('홍길동','이순신','심청이')
# cnt = 0
# for name in names:  # 시퀀스 타입은 순서를 가지는 타입
#    print(name)
#    cnt += 1
# names = "ABCDE"
# cnt = 0
# for n in range(21,0,-2):  # 시퀀스 타입은 순서를 가지는 타입
#    print(n)
#    cnt += 1
# else:
#    print(f"{cnt}명을 출력하였습니다.")
    
cnt = 0
for n in range(21,0,-2):  # 시퀀스 타입은 순서를 가지는 타입
    print(n)
    cnt += 1
else:
    print(f"{cnt}명을 출력하였습니다.") 