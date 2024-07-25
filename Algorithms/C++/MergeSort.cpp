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
    vector<Type> tempVec;
    
    int i = left; // starting index for left half
    int j = middle + 1; // starting index for right half

    // comparing and copying with the indexes
    while (i <= middle && j <= right) {
        if(vec[i] <= vec[j]) {
            tempVec.push_back(vec[i]);
            i++;
        }
        else {
            tempVec.push_back(vec[j]);
            j++;
        }
    }

    // now we have to make sure all data is inserted
    while (i <= middle) {
        tempVec.push_back(vec[i]);
        i++;
    }
    while (j <= right) {
        tempVec.push_back(vec[j]);
        j++;
    }

    // now copy over elements
    // recursion is why we used the left starting index
    // if we had just started from index 0 instead we would overwrite elements not belonging to the subarray we are currently in 
    for(int z = 0; z < tempVec.size(); z++) {
        vec[left + z] = tempVec[z];
    }
}

template <typename Type>
void mergeSort(vector<Type>& vec, int left, int right) {
    // this is where we are going to break up everything with recursion

    // if we have reached the smallest possible list, left index is greater than right
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
    displayVector(vec1);

    return 0;      
}

/*
    cd Algorithms/C++
    g++ -std=c++11 MergeSort.cpp -o tempExecutable && ./tempExecutable && rm tempExecutable

*/