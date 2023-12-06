#array in class example

class Array(object):
    def __init__(self, initialSize): #constructing the object
        self.__a = [None] * initialSize #array stored as list
        self.__nItems = 0 #no item in array initially

    def __len__(self): #special def for length
        return self.__nItems #return number of items

    def get(self, n ): #return the value at index n\
        if 0 <= n and n < self.__nItems: #check if n in is bounds
            return self.__a[n] #only return item if in bounds

    def set (self, n, value): #set the value at index n
        if 0 <= n and n < self.__nItems: #check if n is in bounds
            self.__a[n] = value # only set item if in bounds

    def insert(self, item): #insert item at end
        self.__a[self.__nItems] = item #item goes at current end
        self.__nItems += 1 #incriment number of items

    #find function is part of search function, this will find the index of item being searched
    #returns -1 if not found
    def find(self, item): #find index for item
        for j in range(self.__nItems): #look through array
            if self.__a[j] == item: #if value is found
                return j #return index to item
        return -1 #if not found
    def search(self, item): #search for item
        return self.get(self.find(item)) #return item if found

    def delete(self, item): #delete first occurance deletes first object?
        for j in range(self.__nItems): # of item
            if self.__a[j] == item:#if found #remove element dpes not work dont care to fix
                self.__nItems -= 1 #reduce index
                del(self.a[j])#does not work
                for k in range(j, self.__nItems): #move items from
                    self.__a[k] = self.__a[k + 1] #move right
            return True #return success flah
        return False
    def traverse(self, function=print): #traverse
        for j in range(self.__nItems):
            function(self.__a[j])

    def maximum(self):
        myMax = None
        for j in range(self.__nItems): #iterate through whole array
            if isinstance(self.__a[j], (int, float)): #only numeric values
                if myMax is None:
                    myMax = self.__a[j] #change if there is no initial value
                else:
                    myMax = max(myMax, self.__a[j]) #find max of both values presented
        return myMax

    def delMax(self):
        myMax = None
        for j in range(self.__nItems): #iterate through whole array
            if isinstance(self.__a[j], (int, float)): #only numeric values
                if myMax is None:
                    myMax = self.__a[j] #change if there is no initial value
                else:
                    myMax = max(myMax, self.__a[j]) #find max of both values presented
            if myMax is not None:
                self.delete(myMax)


