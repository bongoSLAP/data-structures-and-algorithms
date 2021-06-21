from generatelist import myList

n = len(myList)
for i in range(n):
    minimum = i

    for j in range(i+1, n):
      if (myList[j] < myList[minimum]):
        minimum = j

    temp = myList[i]
    myList[i] = myList[minimum]
    
    myList[minimum] = temp