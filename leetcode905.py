
A=[3,1,2,4]
def sortArrayByParity(A:list):
    listOdd  = []
    listEven = []
    for i in A:
        i = int(i)
        if i % 2 == 0:
            listEven.append(i)
        elif i % 2 == 1:
            listOdd.append(i)

    for j in listOdd:
        listEven.append(j)
    return listEven

print(sortArrayByParity(A))