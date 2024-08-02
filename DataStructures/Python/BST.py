# Binary Search Tree in python
# Left is less than the root, right is more than the root
# a key factor of exploring the BST is recursion!
# No node can have more than 2 children

class Node:
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self): 
        self.root = None

    def insert(self, insData):
        if self.root is None:
            self.root = Node(insData)
        else:
            self.insertion(self.root, insData)
    
    def insertion(self, currentNode, insData):
        if currentNode is None: # base case: when we reach where no data is available we can make our node
            return Node(insData) 
        elif insData < currentNode.data:  # if our data we are inserting is less than our current nodes data we move to the left node recursively
            currentNode.left = self.insertion(currentNode.left, insData)
        else: # moving to the right node recursively if insData is more than the current node
            currentNode.right = self.insertion(currentNode.right, insData)
        return currentNode

    def display(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self.display_helper(self.root, 0)

    def display_helper(self, currentNode, level):
        if currentNode is None:
            return
        print(currentNode.data)
        print("\n /  \ ")
        



def menu():
    print("+X       : To add X to the tree")
    print("D        : To display the binary search tree")


def main():
    print()
    print("Welcome to the Binary Search Tree")
    BST = BST()
    choice = "y"
    while choice != "Q" and choice != "q":
        menu()
        print()
        BST.display()
        print()
        choice = input("Enter your choice: ")
        print()
        if choice.startswith("+"):
            try:
                number = int(choice[1:])  # Extract the number after "+"
                BST.insert(number)
            except ValueError:
                print("Invalid input.")
        



main()