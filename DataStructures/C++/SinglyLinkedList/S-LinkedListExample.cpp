#include "S-LinkedList.h"
#include <iostream>

using namespace std; 

/*
Functions to add:

Reverse: Reverses the linked list.
GetSize: Returns the size of the linked list.
IsEmpty: Checks if the linked list is empty.
FindMiddle: Finds and returns the middle element of the linked list.
RemoveDuplicates: Removes duplicate elements from the linked list.
Merge: Merges another linked list into this linked list.
Sort: Sorts the linked list.

MAKE THIS TEMPLATE *FACEPALM*

*/


void displayMenu() {
 cout << "Commands: " << endl;
 cout << "+<char>                        : To begin the insert function" << endl;
 cout << "-<char>                        : To begin the remove function" << endl;
 cout << "?<char>                        : To begin the search function" << endl;
 cout << "@<char> <dataBeingPushedUp>    : To begin the InsertAt function" << endl; // inserts at the nodes location and moves the old one forward
 cout << "*<char>                        : To get item at Nth location" << endl;
 cout << "C                              : To clear current linkedlist" << endl;
 cout << "D                              : To display current linkedlist" << endl;
 cout << "Q                              : To quit the program" << endl;
}

int main() {
    LinkedList list;
    displayMenu();
    string command = "N";
    char character;

    while (command != "Q" && command != "q") {
        cout << "\nCommand: ";
        getline(cin, command);

        if (command[0] == '+') { // inserting an integer
            char character = command[1]; // taking the value not the plus to insert
            list.Insert(character);
            cout << endl;
            list.Display();
        }

        else if (command == "D" || command == "d") { 
            list.Display();
        }

        else if (command == "C" || command == "c") { 
            list.ClearList();
            list.Display();
        }

        else if (command[0] == '-') { 
            char character = command[1];
            list.RemoveNode(character);
            cout << endl;
            list.Display();
        }

        else if (command[0] == '?') {
            char character = command[1];
            list.Search(character);
            cout << endl;
            list.Display();
        }

        else if (command[0] == '@') { 
            char character = command[1];
            char dataBeingPushed = command[3];
            list.InsertAt(character, dataBeingPushed);
            list.Display();
        }
        else if (command[0] == '*') {  // getNTH so if it was *3 get the third value
            char character = command[1];
            list.getNth(character);
            list.Display();
        }
    }

    cout << "Program terminated.\n" << endl;
    return 0;
}

/*
To compile and run:

cd DataStructures/C++/SinglyLinkedList
g++ -std=c++17 S-LinkedList.cpp S-LinkedListExample.cpp -o tempExecutable && ./tempExecutable && rm tempExecutable


*/