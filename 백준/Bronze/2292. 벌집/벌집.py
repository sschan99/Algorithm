n = int(input())

i = 1
while True:
    if n <= i*(i-1)*3+1:
        print(i)
        break
    i += 1