# numbers = [9,2,4,1,8,6,3,7,5,0]
# for num in numbers:
#    if num in numbers:
#        if num != 0:
#            print(num)
#            continue
#        break

numbers = [-1,2,9,2,4,1,8,6,3,7,5,0,-3,-4]
# 0이 있으면 "0이 포함되어 있습니다." 출력
# num in numbers
# 0이 없으면 "0이 포함되어 있지 않습니다." 출력
# 
for num in numbers:
    if num in numbers:
        if num != 0:
            print("0이 포함되어 있지 않습니다.")
        else:
            print("0이 포함되어 있습니다.")