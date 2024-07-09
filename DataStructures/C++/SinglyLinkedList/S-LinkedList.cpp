#include "S-LinkedList.h" 

LinkedList::LinkedList() {
    head = nullptr;
    size = 0;
}


LinkedList::~LinkedList() { // come back to destructor

}


void LinkedList::Insert(char data) {
    // this insert is where you are inserting at the front of the list and the original head becomes the next node
    Node* newNode = new Node(data); // creating the newnode, which is going to become the head.
    newNode->next = head;
    head = newNode;
    size++;
    Display();
}


void LinkedList::RemoveNode(char data) {
    // removing a node with specficic data
    cout << "Removing Node with the data: " << data << endl;
    // if there is no information available in the list
    if (head == nullptr) {
        cout << "Currently no elements to remove.";
        return;
    }

    // if the head has the information we want to delete
    if (head->data == data) {
        Node* temp = head;
        head = head->next;
        delete temp;
        size--;
        return;
    }

    // if you have to go through the list to find the element to delete
    Node* current = head;
    Node* previous = nullptr;
    while (current != nullptr && current->data != data) {
        previous = current;
        current = current->next;
    }
    if (current == nullptr) {
        cout << "Item could not be found." << endl;
        return;
    }
    
    // now if it is found we update the pointers and remove it making sure we have the correct order without it
    previous->next = current->next;
    delete current;
    size--;
}


void LinkedList::Display() const {
    if (head == nullptr) {
        cout << "Empty List." << endl;
        cout << "Current Size: " << size << endl;
        return;
    }
    Node* temp = head;
    while (temp != nullptr) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULLPTR" << endl;
    cout << "Current Size: " << size << endl << endl;
    }