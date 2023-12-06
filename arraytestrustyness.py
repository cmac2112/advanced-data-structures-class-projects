import arrayexample as arr

def main():
    arra = arr.Array(5)
    arra.insert(2)
    arra.insert(3)
    arra.insert(8)
    print(arra.delete(8))
    print("---")
    print(arra.traverse())
    print('---')
    print(arra.maximum())
    print(arra.delMax())
main()
