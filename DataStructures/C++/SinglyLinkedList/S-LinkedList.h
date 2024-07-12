#pragma once
#include <iostream>

using namespace std;

class LinkedList {
    private:
        struct Node {
            char data;
            Node* next;
            Node(char data) {
                this->data = data;
                next = nullptr;
            }
        };

        Node* head;
        int size;

    public:
        LinkedList(); // default constructor, initializes an empty list
        ~LinkedList(); // destructor

        void Insert(char data);
        void RemoveNode(char data); 
        void ClearList();
        void getNth(char data);

        void InsertAt(char data, char dataBeingPushed);
        void Search(char data);
        void Display() const;

        // add copy constructor and assignment operator if you are copying lists. 
        // add error handling.
};

// backwards way of having this run by having the inclusion of the cpp file at the bottom.
// would have been easier making in Visual Studio 2019, but ya live ya learn

