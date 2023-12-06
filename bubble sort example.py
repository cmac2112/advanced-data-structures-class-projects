#bubble sort example

def bubbleSort(arr): #inherits array name used below
    n = len(arr) #gets amount of elements in array

    for i in range (n-1):
        flag = 0

        for j in range (n-1):

            if arr[j] > arr[j + 1]: #if current element is > next index element
                tmp = arr[j] #that element becomes a temp element
                arr[j] = arr[j + 1] #temp element becomes next element in line
                arr[j + 1] = tmp #next element becomes temp element to be sorted
                flag = 1
        if flag == 0:
            break

    return arr

bsort = [56, 21, 6, 9, 33, 3, 45]

result = bubbleSort(bsort)

print(result)
