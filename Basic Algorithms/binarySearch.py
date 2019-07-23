def binarySearch(arr, elem):
    # Initialize the first index to 0
    first = 0
    # Initializd the last index to length of the array - 1
    last = len(arr) - 1
    
    # Initialize the found parameter to False
    found = False
    
    while first <= last and found == False:
        # Update the mid parameter
        mid = int((first + last)/2)
        # If the element at mid is the element we are searching
        if (arr[mid] == elem):
            found = True
        else:
            # If the element we are searching for is less than the element at mid
            if elem < arr[mid]:
                # Update last to the element before mid
                # i.e. search in the portion of the array before the current mid
                last = mid - 1
            else:
                # Update first to the element after mid
                # i.e. search in the portion of the array after the current mid
                first = mid + 1
                
    return found

a = [1,2,3,4,6,7,8,9]
print(binarySearch(a, 6))
