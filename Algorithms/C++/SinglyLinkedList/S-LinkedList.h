#include <iostream>

using namespace std;


template <typename DT>
class LinkedList {
    private:
        struct Node {
            DT data;
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

        // for these functions we need to come back to and add the parameters
        void Insert();
        void InsertAt();
        void RemoveNode(); 
        void Search();

        void Display();

        // add copy constructor and assignment operator if you are copying lists. 
        // add error handling.
};