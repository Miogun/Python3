def printPersons(leader, *persons):
    print(len(persons))
    print(persons)
    print('leader:',leader)
    for name in persons:
        print(name)
    
printPersons("홍길동","이순신","에디슨")
# 튜플로 받는다.
