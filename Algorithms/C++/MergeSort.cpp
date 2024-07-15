#include <iostream>
#include <vector>

using namespace std; 



int main() {
    // later make it where you can enter your input as well in a seperate option.

    cout << "\nWelcome to the Merge Sort Algorithm (C++), created by Zane Christe\n";
    vector<int> vec1 = {38, 27, 43, 3, 9, 82, 10}; 
    
    cout << "List before sorting: ";
    for (int i = 0; i < vec1.size(); i++) {
        cout << vec1.at(i) << " ";
    }

    cout << "\nList after sorting: ";

    return 0;      
}

/*
    cd Algorithms/C++     
    g++ -std=c++11 -o MergeSort MergeSort.cpp
    ./MergeSort     
*/