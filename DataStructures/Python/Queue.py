# making a Queue
# Queue is FIFO, First in First out, always popping the element that went in first
# it is like waiting in a line

class Queue:
    # this function is always ran when the class is being initiated, somewhat like a constructor 
    # "The __init__() function is called automatically every time the class is being used to create a new object." -W3Schools
    # The object is the first arguement 
    # The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    def __init__(self): 
        self.qList = []
    
    def isEmpty(self):
        return len(self.qList) == 0
    
    def enqueue(self, data):
    
    def dequeue(self):

    def size(self):
        return len(self.qList)

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
    print("\nWelcome to the Queue!")
    print("EnqX  : to enqueue an element onto the queue")
    print("Deq   : to remove (dequeue) first element inserted into queue")
    print("S     : to get the size of the queue")
    print("E     : to see if the queue is empty")
    print("D     : display the queue")
    print("Q     : to quit the program")
    print()



def main(): 
    q = Queue()
    choice = "y"
    while choice != "Q" and choice != "q":
        Menu()
        q.display()
        print()
        choice = input("Enter your choice: ")
        print()
        if choice == "Deq":
            q.dequeue()
        elif choice.startswith("Enq"):
            try:
                number = int(choice[3:])  # Extract the number after "Enq"
                q.enqueue(number)
            except ValueError:
                print("Invalid input for Enqueue. Please use the format EnqX where X is an integer.")
        elif choice == "S":
            print("Size of queue is: ", q.size())
        elif choice == "E":
            print("Queue is empty" if q.isEmpty() else "Queue is not empty")
        elif choice == "D":
            q.display()



    # enable it where a user can insert and pop to do this for simplicity
    # fix spacing issue with display
    # Testing


main()