def printPerson(name, age, major='전산학과'): # parameter = 형식 인자, 인자를 주고 호출
    print(f"이름 : {name}, 연령 : {age}, 전공 : {major}") 
    
printPerson('홍길동',20) # argument
printPerson('에디슨',55,'발명가') # argument
printPerson(age=50,major='장군',name='이순신') # 키워드 Parameter

# Default Parameter는 반드시 맨 뒤에 붙인다.

