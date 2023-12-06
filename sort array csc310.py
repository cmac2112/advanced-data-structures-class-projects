# Implement an Array data structure as a simplified type of list.

import random
import timeit

class Array(object):
    def __init__(self, initialSize):  # Constructor
        self.__array = [None] * initialSize  # The array stored as a list
        self.__nItems = 0  # No items in array initially

    def __len__(self):  # Special def for len() func
        return self.__nItems  # Return number of items

    def get(self, n):  # Return the value at index n
        if 0 <= n < self.__nItems:  # Check if n is in bounds, and
            return self.__array[n]  # only return item if in bounds

    def set(self, n, value):  # Set the value at index n
        if 0 <= n < self.__nItems:  # Check if n is in bounds, and
            self.__array[n] = value  # only set item if in bounds

    def swap(self, j, k):  # Swap the values at 2 indices
        if (0 <= j < self.__nItems and  # Check if indices are in
                0 <= k < self.__nItems):  # bounds, before processing
            self.__array[j], self.__array[k] = self.__array[k], self.__array[j]

    def insert(self, item):  # Insert item at end
        self.__array[self.__nItems] = item  # Item goes at current end
        self.__nItems += 1  # Increment number of items

    # The find function is part of the search function. This
    # will find the index of the item being searched. It returns
    # -1 if the item is not found.
    def find(self, item):  # Find index for item
        for j in range(self.__nItems):  # Among current items
            if self.__array[j] == item:  # If found,
                return j  # then return index to item
        return -1  # Not found -> return -1

    def search(self, item):  # Search for item
        return self.get(self.find(item))  # and return item if found

    def delete(self, item):  # Delete first occurrence
        for j in range(self.__nItems):  # of an item
            if self.__array[j] == item:  # Found item
                self.__nItems -= 1  # One fewer at end
                for k in range(j, self.__nItems):  # Move items from
                    self.__array[k] = self.__array[k + 1]  # right over 1
                return True  # Return success flag

        return False  # Made it here, so couldn't find the item

    def traverse(self, function=print):  # Traverse all items
        for j in range(self.__nItems):  # and apply a function
            function(self.__array[j])

    def __str__(self):  # Special def for str() func
        ans = "["  # Surround with square brackets
        for i in range(self.__nItems):  # Loop through items
            if len(ans) > 1:  # Except next to left bracket,
                ans += ", "  # separate items with comma
            ans += str(self.__array[i])  # Add string form of item
        ans += "]"  # Close with right bracket
        return ans

    def bubbleSort(self):  # Sort comparing adjacent vals
        for last in range(self.__nItems - 1, 0, -1):  # and bubble up
            for inner in range(last):  # inner loop goes up to last
                if self.__array[inner] > self.__array[inner + 1]:  # If item less
                    self.swap(inner, inner + 1)  # than adjacent item, swap

    def selectionSort(self):  # Sort by selecting min and
        for outer in range(self.__nItems - 1):  # swapping min to leftmost
            min = outer  # Assume min is leftmost
            for inner in range(outer + 1, self.__nItems):  # Hunt to right
                if self.__array[inner] < self.__array[min]:  # If we find new min,
                    min = inner  # update the min index

            # __array[min] is smallest among __array[outer]...__array[__nItems-1]
            self.swap(outer, min)  # Swap leftmost and min

    def insertionSort(self):  # Sort by repeated inserts
        for outer in range(1, self.__nItems):  # Mark one item
            temp = self.__array[outer]  # Store marked item in temp
            inner = outer  # Inner loop starts at mark
            while inner > 0 and temp < self.__array[inner - 1]:  # If marked
                self.__array[inner] = self.__array[inner - 1]  # item smaller, then
                inner -= 1  # shift item to right
            self.__array[inner] = temp  # Move marked item to 'hole'

    def evenOddSort(self):
        n = self.__nItems
        isSorted = 0  # flag
        while isSorted == 0:
            isSorted = 1

            # Perform Bubble sort on odd indexed items
            for i in range (1, n-1, 2):
                if self.__array[i] > self.__array[i+1]:
                    self.swap(i, i + 1)  # swap items
                    isSorted = 0

            # Perform Bubble sort on even indexed items
            for i in range (0, n-1, 2):
                if self.__array[i] > self.__array[i+1]:
                    self.swap(i, i + 1)  # swap items
                    isSorted = 0
    def shellSort(self):
        a = self.__nItems
        gap = 1
        while 3 * gap + 1 < len(self.__array):
            gap = 3 * gap + 1

        while gap > 0:
            for outer in range(gap, self.__nItems):
                temp = self.get(outer)
                inner = outer
                while inner >= gap and temp < self.get(inner-gap):
                    self.set(inner, self.get(inner-gap))
                    inner -= gap
                if inner < outer:
                    self.set(inner, temp)
            gap = (gap - 1) // 3
        



# Add Shell Sort as part of Array Class

def initArray(size=100, maxValue=100, seed=3.14159):
    """Create an Array of the specified size with a fixed sequence of
       'random' elements"""
    sortarray = Array(size)                   # Create the Array object
    random.seed(seed)                   # Set random number generator
    for i in range(size):               # to known state, then loop
        sortarray.insert(random.randrange(maxValue))  # Insert random numbers
    return sortarray                         # Return the filled Array


sortarray = initArray()
print("Array containing", len(sortarray), "items:\n", sortarray)

for test in ['initArray().bubbleSort()',
             'initArray().selectionSort()',   # < == Add Shell Sort
             'initArray().insertionSort()',
             'initArray().shellSort()']:
    elapsed = timeit.timeit(test, number=100, globals=globals())
    print(test, "took", elapsed, "seconds", flush=True)

#sortarray.insertionSort()
#sortarray.evenOddSort()
#sortarray.OddEvenSort()
sortarray.shellSort()   #<====

print('Sorted array contains:\n', sortarray)
