#slection sort example
def selectionSort(itemsList):
    n = len(itemsList) #getting length of list
    for i in range (n-1): #iterate through list
        minValueIndex = i 

        for j in range( i + 1, n): #compare left most items to the right
            if itemsList[j] < itemsList[minValueIndex]:
                    minValueIndex = j
        if minValueIndex != i:
                temp = itemsList[i]
                itemsList[i] = itemsList[minValueIndex]
                itemsList[minValueIndex] = temp
    return itemsList

e1 = [21, 6, 9, 33, 3]
print(selectionSort(e1))
