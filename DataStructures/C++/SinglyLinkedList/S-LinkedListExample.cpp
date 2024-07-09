#include "S-LinkedList.h"
#include <iostream>

int main() {
    LinkedList list;

    // Test inserting elements
    list.Insert(10);
    list.Insert(20);
    list.Insert(30);

    // Display the list
    std::cout << "List after inserting 10, 20, 30:" << std::endl;
    list.Display();

    // Test removing an element
    list.RemoveNode(20);

    // Display the list after removal
    std::cout << "List after removing 20:" << std::endl;
    list.Display();

    // Test removing an element that doesn't exist
    list.RemoveNode(40);

    // Display the list after trying to remove a non-existent element
    std::cout << "List after attempting to remove 40 (non-existent):" << std::endl;
    list.Display();

    return 0;
}

/*
To compile and run:

cd MultiLanguage-DSA-Library/DataStructures/C++/SinglyLinkedList
g++ -std=c++17 S-LinkedList.cpp S-LinkedListExample.cpp -o tempExecutable && ./tempExecutable && rm tempExecutable


*/