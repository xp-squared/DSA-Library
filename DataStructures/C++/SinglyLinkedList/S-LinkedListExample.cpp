#include "S-LinkedList.h"
#include <iostream>

using namespace std; 

void displayMenu() {
 cout << "Commands: " << endl;
 cout << "+<char>     : To begin the insert function" << endl;
 cout << "-<char>     : To begin the remove function" << endl;
 cout << "?<char>     : To begin the search function" << endl;
 cout << "@<char> <dataBeingPushedUp>    : To begin the InsertAt function" << endl; // inserts at the nodes location and moves the old one forward
 cout << "D     : To display current linkedlist" << endl;
 cout << "Q     : To quit the program" << endl;
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

        else if (command == "D") { // displaying the current list
            list.Display();
        }

        else if (command[0] == '-') { // displaying the current list
            char character = command[1];
            list.RemoveNode(character);
            cout << endl;
            list.Display();
        }

        else if (command[0] == '?') { // displaying the current list
            char character = command[1];
            list.Search(character);
            cout << endl;
            list.Display();
        }

        else if (command[0] == '@') { // displaying the current list
            char character = command[1];
            char dataBeingPushed = command[3];
            list.InsertAt(character, dataBeingPushed);
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