#pragma once
#include <iostream>

using namespace std;


template <typename DT>
class LinkedList {
    private:
        struct Node {
            DT data;
            Node* next;
            Node(DT data) {
                this->data = data;
                next = nullptr;
            }
        };

        Node* head;
        int size;

    public:
        LinkedList(); // default constructor, initializes an empty list
        ~LinkedList(); // destructor

        void Insert(DT data);
        void RemoveNode(DT data); 

        void InsertAt();
        void Search();
        void Display();

        // add copy constructor and assignment operator if you are copying lists. 
        // add error handling.
};

#include "S-LinkedList.cpp" 
// backwards way of having this run by having the inclusion of the cpp file at the bottom.
// would have been easier making in Visual Studio 2019, but ya live ya learn