import oddevenarrayhomework as arr

def main():
    a = arr.Array(13) #build array
    a.insert(1)#insert elements
    a.insert(2)
    a.insert(15)
    a.insert(8)
    a.insert(10)
    a.insert(120)
    a.insert(-1)
    a.insert(42)
    a.insert(41)
    a.insert(125)
    a.insert(720)
    a.insert(155)
    a.insert(-120)
    print(a) #before the sort
    a.oddEvenSort(13)#call sort
    print(a)#print sorted array
    

main()
