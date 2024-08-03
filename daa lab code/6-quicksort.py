# quick sorting - sorting an array by dividing it and then dividing it and then sorting it
#divide and conqure approach 
#TC- O(nlog(n)) for best , O(n^2) for worst

#take array input to be sorted 
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

#create a function to make partition of arr
def partition(array, low, high):
    pivot = array[low] #according to question first element is selected as pivoted element
    i = low + 1
    for j in range(low + 1, high + 1):
        if array[j] <= pivot: 
            array[i], array[j] = array[j], array[i] #swaping
            i += 1
    array[low], array[i - 1] = array[i - 1], array[low] #swaping 
    return i - 1
#function to sort both the partitioned array
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high) #calling the partition func
        quickSort(array, low, pi-1)
        quickSort(array, pi+1, high)

quickSort(arr, 0, len(arr)-1) 
print("Sorted array is:", arr) 