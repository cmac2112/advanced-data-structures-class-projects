#stack driver
import adstack

def main():
    stack = adstack.Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6) #stack stize of 5 wont push a 6th element
    print(stack.peek())
main()
    
