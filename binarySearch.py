def binarySearch(list, item):
    low = 0
    high = len(list) -1
    steps = 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid, steps
        if guess > item:
            steps += 1
            high = mid - 1
        else:
            steps += 1
            low = mid + 1
    return None, steps # Number does not exist in list
    
myList = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49, 51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99]
    
print(binarySearch(myList, 47))
print(binarySearch(myList, -1))
print(binarySearch(myList, 25))
print(binarySearch(myList, 55))