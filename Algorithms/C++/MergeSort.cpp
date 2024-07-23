#include <iostream>
#include <vector>

using namespace std; 

template <typename Type>
void displayVector(vector<Type>& vec) {
    for (int i = 0; i < vec.size(); i++) {
        cout << vec.at(i) << " ";
    }
    cout << endl;
}

template <typename Type>
void merge(vector<Type>& vec, int left, int right, int middle) {
    
}

template <typename Type>
void mergeSort(vector<Type>& vec, int left, int right) {
    // this is where we are going to break up everything with recursion

    // if we have reached the smallest possible list
    if (left >= right) {
        return;
    }
    int middle = left + ((right - left) / 2);

    // this below splits up the the vector into smaller lists each time for both the left and right sides
    mergeSort(vec, left, middle);
    mergeSort(vec, middle + 1, right);

    merge(vec, left, right, middle);
}



int main() {
    // later make it where you can enter your input as well in a seperate option.

    cout << "\nWelcome to the Merge Sort Algorithm (C++), created by Zane Christe\n";
    vector<int> vec1 = {38, 27, 43, 3, 9, 82, 10, 7}; // size is 8
    
    cout << "List before sorting: ";
    displayVector(vec1);

    mergeSort(vec1, 0, vec1.size() - 1);

    cout << "\nList after sorting: ";

    return 0;      
}

/*
    cd Algorithms/C++
    g++ -std=c++11 MergeSort.cpp -o tempExecutable && ./tempExecutable && rm tempExecutable

*/