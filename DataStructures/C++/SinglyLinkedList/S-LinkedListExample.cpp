#include "S-LinkedList.h"
#include <iostream>

using namespace std; 

void displayMenu() {
 cout << "Commands: " << endl;
 cout << "+     : To begin the insert function" << endl;
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
        cin >> command;

        if (command == "+") { // inserting
            cout << "Enter an char to insert into list: ";
            cin >> character;
            cout << endl;
            list.Insert(character);
        }

        if (command == "D") { // displaying the current list
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