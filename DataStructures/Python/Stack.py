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
    
    # appending an element to the front of stack, this becomes the new head of it
    def push(self, data):
        self.stackList.append(data)
    
    # function to remove the top most element of the stack
    def pop(self):
        if self.isEmpty() == True:
            # throwing exception for the stack being empty
            return print("Popping from empty list")
        else:
            # removes item at the last index, which is the default of pop method
            # we can display which element we are removing by using our peek function
            print("\nWe are popping: ", self.peek())
            print()
            return self.stackList.pop() 

    # function to peek at what is at the top of the stack 
    def peek(self):
        if self.isEmpty == 0:
            print("Size is 0, cannot peek")
        else:
            return self.stackList[-1]

    def size(self):
        return len(self.stackList)

    def display(self) :
        if self.isEmpty() == True:
            print("Empty List, nothing to print")
            return
        print("Current List: ", end = " ")
        for i in range(len(self.stackList)):
            # printing each element, remember we can make the print function end with a space instead of how it ends always with a new line
            print(self.stackList[i], end = " ")
        print()


def Menu():
    print("\nWelcome to the Stack!")
    print("PushX : to push an element onto the stack")
    print("Pop   : to pop topmost element from the stack")
    print("P     : peek at last pushed element of stack")
    print("S     : to get the size of the stack")
    print("E     : to see if the stack is empty")
    print("D     : display the stack")
    print("Q     : to quit the program")
    print()



def main(): 
    s = Stack()
    choice = "y"
    while choice != "Q" and choice != "q":
        Menu()
        s.display()
        print()
        choice = input("Enter your choice: ")
        print()
        if choice == "Pop":
            s.pop()
        elif choice.startswith("Push"):
            try:
                number = int(choice[4:])  # Extract the number after "Push"
                s.push(number)
            except ValueError:
                print("Invalid input for Push. Please use the format PushX where X is an integer.")
        elif choice == "P":
            print("Top element of stack is: ", s.peek())
        elif choice == "S":
            print("Size of stack is: ", s.size())
        elif choice == "E":
            print("Stack is empty" if s.isEmpty() else "Stack is not empty")
        elif choice == "D":
            s.display()



    # enable it where a user can insert and pop to do this for simplicity
    # fix spacing issue with display
    # Testing


main()