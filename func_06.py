# def printPersons(**kwargs):
#     print(f'이름 : {kwargs['name']}')
#     print(f'연령 : {kwargs['age']}')
#     print(f'전공 : {kwargs['major']}')
# #    print(kwargs)        
# printPersons(name='홍길동',age=20,major='학생')

def printPersons(name, age, major):
    print(name, age, major)
    
person = {'name': '홍길동', 'age': 20, 'major': '전산'}
printPersons(**person)
#printPersons()