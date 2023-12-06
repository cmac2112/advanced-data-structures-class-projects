# Implement an Array data structure as a simplified type of list.

class Array(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0  # No items in array initially

    def __len__(self):  # Special def for len() func
        return self.__nItems  # Return number of items

    def get(self, n):  # Return the value at index n
        if 0 <= n < self.__nItems:  # Check if n is in bounds, and
            return self.__a[n]  # only return item if in bounds

    def set(self, n, value):  # Set the value at index n
        if 0 <= n < self.__nItems:  # Check if n is in bounds, and
            self.__a[n] = value  # only set item if in bounds

    def swap(self, j, k):  # Swap the values at 2 indices
        if (0 <= j < self.__nItems and  # Check if indices are in
                0 <= k < self.__nItems):  # bounds, before processing
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def insert(self, item):  # Insert item at end
        self.__a[self.__nItems] = item  # Item goes at current end
        self.__nItems += 1  # Increment number of items

    # The find function is part of the search function. This
    # will find the index of the item being searched. It returns
    # -1 if the item is not found.
    def find(self, item):  # Find index for item
        for j in range(self.__nItems):  # Among current items
            if self.__a[j] == item:  # If found,
                return j  # then return index to item
        return -1  # Not found -> return -1

    def search(self, item):  # Search for item
        return self.get(self.find(item))  # and return item if found

    def delete(self, item):  # Delete first occurrence
        for j in range(self.__nItems):  # of an item
            if self.__a[j] == item:  # Found item
                self.__nItems -= 1  # One fewer at end
                for k in range(j, self.__nItems):  # Move items from
                    self.__a[k] = self.__a[k + 1]  # right over 1
                return True  # Return success flag

        return False  # Made it here, so couldn't find the item

    def traverse(self, function=print):  # Traverse all items
        for j in range(self.__nItems):  # and apply a function
            function(self.__a[j])

    def __str__(self):  # Special def for str() func
        ans = "["  # Surround with square brackets
        for i in range(self.__nItems):  # Loop through items
            if len(ans) > 1:  # Except next to left bracket,
                ans += ", "  # separate items with comma
            ans += str(self.__a[i])  # Add string form of item
        ans += "]"  # Close with right bracket
        return ans

    def bubbleSort(self):  # Sort comparing adjacent vals
        for last in range(self.__nItems - 1, 0, -1):  # and bubble up
            for inner in range(last):  # inner loop goes up to last
                if self.__a[inner] > self.__a[inner + 1]:  # If item less
                    self.swap(inner, inner + 1)  # than adjacent item, swap

    def selectionSort(self):  # Sort by selecting min and
        for outer in range(self.__nItems - 1):  # swapping min to leftmost
            min = outer  # Assume min is leftmost
            for inner in range(outer + 1, self.__nItems):  # Hunt to right
                if self.__a[inner] < self.__a[min]:  # If we find new min,
                    min = inner  # update the min index

            # __a[min] is smallest among __a[outer]...__a[__nItems-1]
            self.swap(outer, min)  # Swap leftmost and min

    def insertionSort(self):  # Sort by repeated inserts
        for outer in range(1, self.__nItems):  # Mark one item
            temp = self.__a[outer]  # Store marked item in temp
            inner = outer  # Inner loop starts at mark
            while inner > 0 and temp < self.__a[inner - 1]:  # If marked
                self.__a[inner] = self.__a[inner - 1]  # item smaller, then
                inner -= 1  # shift item to right
            self.__a[inner] = temp  # Move marked item to 'hole'

    def oddEvenSort(self, n):
        Sorted = 0
        evenpasses = 0
        oddpasses = 0
        
        while Sorted == 0:
            print('Even Passes:', evenpasses)
            print('Odd Passes:', oddpasses)
            print('Total Passes:', (evenpasses + oddpasses))
            Sorted = 1
            #odd sorter
            for i in range(1, n-1, 2): #range start at 1 end at end, 2 steps between (odd)
                if self.__a[i] > self.__a[i+1]:#compare values found
                    self.__a[i], self.__a[i+1] = self.__a[i+1], self.__a[i] #swap variables
                    Sorted = 0
                    evenpasses += 1
                    #even sorter
            for i in range(0, n-1, 2):#range through array, start at i0 two step (even)
                if self.__a[i] > self.__a[i+1]: #compare outputted elements
                    self.__a[i], self.__a[i+1] = self.__a[i+1], self.__a[i] #swap if needed
                    Sorted = 0
                    oddpasses += 1
        return
                        
                                        
