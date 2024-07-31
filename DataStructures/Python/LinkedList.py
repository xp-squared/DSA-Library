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
        if self.head == None:
            print("No Data Available.")
        else:
            self.temp = self.head
            while self.temp != None:
                print(self.temp.data, end=" -> ")
                self.temp = self.temp.next
            print("None")
            
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            self.temp = self.head
            while self.temp.next != None:
                self.temp = self.temp.next
            self.temp.next = Node(data)
    
    def remove_front(self):
        if self.head == None:
            print("No data to remove")
            print()
        else:
            self.temp = self.head
            self.head = self.temp.next
            self.temp = None

    def remove_back(self):
        if self.head == None:
            print("No data to remove")
            print()
        elif self.head.next == None:
            self.head = None
        else:
            self.temp = self.head
            while self.temp.next.next != None:
                self.temp = self.temp.next
            self.temp.next = None
        

    

def menu():
    print("Welcome to the LinkedList")
    print("+X     : Insert X at the beginning of the list.")
    print(">X     : Insert X at the end of the list.")
    print("-        : To remove frontmost element")
    print("--       : To remove backmost element")
    print("Q        : Insert Q to quit the program.")




def main():
    print()
    LL = LinkedList()
    choice = "y"
    while choice != "Q" and choice != "q":
        menu()
        print()
        LL.display()
        print()
        choice = input("Enter your choice: ")

        print()
        if choice.startswith("+"):
            try:
                number = int(choice[1:])  # Extract the number after "Beg"
                LL.insert_at_beginning(number)
            except ValueError:
                print("Invalid input.")

        elif choice.startswith(">"):
            try:
                number = int(choice[1:])  # Extract the number after "End"
                LL.insert_at_end(number)
            except ValueError:
                print("Invalid input.")

        elif choice == "-":
            LL.remove_front()

        elif choice == "--":
            LL.remove_back()


main()