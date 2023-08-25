a = 10

def add(x):
    global a
    a += 10
    
add(100)
print(a)