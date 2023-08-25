a = 0
while True:
    a = a + 1
    if(a%2) == 0:
        continue
    if(a>=10):
        break
    print({}.format(a))