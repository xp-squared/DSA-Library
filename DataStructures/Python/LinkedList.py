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

    def get_length_of_list(self):
        counter = 0
        self.temp = self.head
        while self.temp != None:
            counter+=1
            self.temp = self.temp.next
        print("List Length: ", counter)

    def get_total(self):
        if self.head == None:
            print("Empty list, total is NULL.")
            print()
        else:
            counter = 0
            self.temp = self.head
            while self.temp!= None:
                counter += self.temp.data
                self.temp = self.temp.next
            print("Total of list: ", counter, "\n")

    # function to remove the first instance of a value that user wants removed, if there are two fours in the list it will remove the 4 closest to the front
    def remove_first_instance_of_value_given(self, data):
        if self.head == None:
            print("Empty list.")
        elif self.head.data == data:
            self.head = self.head.next
        else:
            self.temp = self.head
            prev = None
            while self.temp != None and self.temp.data != data:
                prev = self.temp
                self.temp = self.temp.next
            if self.temp == None:
                print("Data not found within list.")
            else:
                prev.next = self.temp.next

    

def menu():
    print("+X       : Insert X at the beginning of the list.")
    print("/X       : Insert X at the end of the list.")
    print("-X       : To remove first instance of that element in list.")
    print("<        : To remove frontmost element.")
    print(">        : To remove backmost element.")
    print("L        : To get length of the list.")
    print("T        : Get total sum of numbers from list.")
    print("Q        : Insert Q to quit the program.")




def main():
    print()
    print("Welcome to the LinkedList")
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

        elif choice.startswith("/"):
            try:
                number = int(choice[1:])  # Extract the number after ""
                LL.insert_at_end(number)
            except ValueError:
                print("Invalid input.")
    
        elif choice.startswith("-"):
            try:
                number = int(choice[1:])  # Extract the number after "-"
                LL.remove_first_instance_of_value_given(number)
            except ValueError:
                print("Invalid input.")

        elif choice == "<":
            LL.remove_front()

        elif choice == ">":
            LL.remove_back()
        
        elif choice == "L" or choice == "l":
            LL.get_length_of_list()

        elif choice == "T" or choice == "t":
            LL.get_total()


main()