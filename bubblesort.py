from generatelist import myList

n = len(myList)

for i in range(n - 1) :
    flag = 0

    for j in range(n - 1) :
            
        if myList[j] > myList[j + 1] : 
            tmp = myList[j]
            myList[j] = myList[j + 1]
            myList[j + 1] = tmp
            flag = 1

    if flag == 0:
        break