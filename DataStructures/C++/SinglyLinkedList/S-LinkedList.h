#pragma once
#include <iostream>

using namespace std;

class LinkedList {
    private:
        struct Node {
            int data;
            Node* next;
            Node(int data) {
                this->data = data;
                next = nullptr;
            }
        };

        Node* head;
        int size;

    public:
        LinkedList(); // default constructor, initializes an empty list
        ~LinkedList(); // destructor

        void Insert(int data);
        void RemoveNode(int data); 

        void InsertAt();
        void Search();
        void Display() const;

        // add copy constructor and assignment operator if you are copying lists. 
        // add error handling.
};

// backwards way of having this run by having the inclusion of the cpp file at the bottom.
// would have been easier making in Visual Studio 2019, but ya live ya learn

