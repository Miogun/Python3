# print("연령 : %010d" % 10)

# print("원주율 : %10.3f" % 3.14195)

person = { 'name': '홍길동', 'age': 20 }
print(person['name'])
personstr = "이름 : {0[name]}, 연령 : {0[age]}".format(person)
personstr = "이름 : {0}, 연령 : {1}".format(person['name'],person['age'])
print(personstr)
print("{:,}원".format(100000000))
