# Making a linked list in python

class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None  # null

class LinkedList:
    def __init__(self): 
        self.head = None # head has null information currently

    def insert_at_beginning(self, data):
        if self.head == None: 
            self.head = Node(data)
        else:
            self.temp = Node(data)
            self.temp.next = self.head
            self.head = self.temp
    
    def display(self):
        self.temp = self.head
        while self.temp != None:
            print(self.temp.data, end=" -> ")
            self.temp = self.temp.next
        print("None")
            
        
        
def menu():
    print("Welcome to the LinkedList")
    print("BegX     : Insert X at the beginning of the list")



def main():
    print()
    LL = LinkedList()
    choice = "y"
    while choice != "Q" and choice != "q":
        menu()
        LL.display()
        print()
        choice = input("Enter your choice: ")

        print()
        if choice.startswith("Beg"):
            try:
                number = int(choice[3:])  # Extract the number after "Beg"
                LL.insert_at_beginning(number)
            except ValueError:
                print("Invalid input for Enqueue. Please use the format EnqX where X is an integer.")


main()