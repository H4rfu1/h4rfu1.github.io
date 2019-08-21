data = [1,2,3,4,5,6,7,8,9,10]
for i in data:
    for j in range(i,20):
        print('*',end="")
        if(j % 2 == 0):
            print('-',end='')
    print()
print(sum(data))
