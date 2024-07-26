# making a stack
# stack is LIFO in this case, last in first out, the top part of the stack will always be popped first

class Stack:
    # this function is always ran when the class is being initiated, somewhat like a constructor 
    # "The __init__() function is called automatically every time the class is being used to create a new object." -W3Schools
    # The object is the first arguement 
    # The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    def __init__(self): 
        self.stackList = []
    
    def isEmpty(self):
        return len(self.stackList) == 0
    
    def push(self, data):
        self.stackList.append(data)
    
    def pop(self):
        if self.isEmpty() == True:
            # throwing exception for the stack being empty
            return print("Popping from empty list")
        else:
            # removes item at the last index, which is the default of pop method
            return self.stackList.pop() 


    def size(self):
        return len(self.stackList)

    def display(self) :
        if self.isEmpty() == True:
            print("Empty List, nothing to print")
            return
        
        print()
        for i in range(len(self.stackList)):
            # printing each element, remember we can make the print function end with a space instead of how it ends always with a new line
            print(self.stackList[i], end = " ")

        

def main(): 
    s = Stack()
    s.push(1)
    s.push(7)
    s.push(16)
    s.display()
    s.pop()
    s.display()

main()