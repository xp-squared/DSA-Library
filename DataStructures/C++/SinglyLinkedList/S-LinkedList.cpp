#include "S-LinkedList.h" 

LinkedList::LinkedList() {
    head = nullptr;
    size = 0;
}


LinkedList::~LinkedList() { // come back to destructor
    ClearList();
    cout << "List has been cleared." << endl;
}


void LinkedList::Insert(char data) {
    // this insert is where you are inserting at the front of the list and the original head becomes the next node
    Node* newNode = new Node(data); // creating the newnode, which is going to become the head.
    newNode->next = head;
    head = newNode;
    size++;
}

void LinkedList::InsertAt(char newData, char dataBeingPushed) {
    Node* newNode = new Node(newData);
    if (head == nullptr) {
        newNode->next = head;
        head = newNode;
        size++;
        return;
    }
    Node* temp = head;
    if (head->data == dataBeingPushed) { // example if you are inserting 5 where 7 is the head type @5 7
        newNode->next = head;
        head = newNode;
        size++;
        return;
    }
    else {
        Node* previous;
        while(temp->data != dataBeingPushed && temp->next != nullptr) {
            previous = temp;
            temp = temp->next;
        }
        if (temp->next == nullptr && temp->data != dataBeingPushed) { // this account for if inserting an item and we do not find the location user gives
            temp->next = newNode;
            size++;
            return;
        }
        else { // fixing the pointers to put the newnode before the dataBeingPushed and after the the one behind the dataBeingPushed
            previous->next = newNode;
            newNode->next = temp;
            size++;
        }
    }

}

void LinkedList::Search(char data) {
    Node* temp = head;
    while(temp != nullptr && temp->data != data) {
        temp = temp->next;
    }
    if (temp == nullptr) {
        cout << "Data was not found." << endl;
        return;
    }
    else if (temp->data == data) {
        cout << "Data was found!" << endl;
        return;
    }
}

void LinkedList::getNth(char character) {
    int index = character - '0'; // converting the index character to int to compare with size
    if (index < 0 || index >= size) {
        cout << "Invalid index" << endl;
        return;
    }
    
    Node* temp = head;
    int counter = 0;
    while (temp != nullptr && counter < index) {
        temp = temp->next;
        counter++;
    }
    
    if (temp != nullptr) {
        cout << temp->data << " is at index " << index << endl;
    } else {
        cout << "Node not found at index " << index << endl;
    }
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
    else if (head->data == data) {
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
        cout << "\nEmpty List." << endl;
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

void LinkedList::ClearList() {
    Node* temp = head;
    while (temp != nullptr) {
        Node* current = temp;
        temp = temp->next;
        delete current;
    }
    head = nullptr;
    size = 0;
}