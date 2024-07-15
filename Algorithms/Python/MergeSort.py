# just run python file with upper right corner and press "Run Python File" from drop down menu
# What we are making is a mergesort algorithm in python, it is a divide and conquer algo so we want to use recursion
# remember it divides the arrays in half and sorts recursively and then merges the sorted halves

# The helper function of the mergesort
def merge(left, right): 
    results = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        # compare each element to see what order it needs to be in
        if left[i] < right[j]:
            results.append(left[i])
            i = i + 1
        else:
            results.append(right[j])
            j = j + 1

    # Append the remaining elements from the left and right arrays
    results.extend(left[i:])
    results.extend(right[j:])

    return results
    

def mergeSort(array):
    if len(array) <= 1:
        return array
    
    # find the middle index
    middle = len(array) //  2

    # using slicing notation to access parts of the list
    leftHalf = array[:middle] # slice of the list up to but not including the middle index
    rightHalf = array[middle:] # slice of the list including the middle index to the end
    
    # using recursion to keep making smaller lists
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)
    
    

def main():
    # later make it where you can enter your input as well in a seperate option.

    print("\nWelcome to the Merge Sort Algorithym, created by Zane Christe\n")
    intList = [7, 3, -5, 18, 1000, 1522, -9, 1, 9, 420, 69, 777, -252, -6, 4, 99, 0]
    print("List before sorting: ")
    print(intList)

    print("\nList after sorting: ")
    sortedList = mergeSort(intList)
    print(sortedList)

main()