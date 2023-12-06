import random
loopcatch1 = False
loopcatch2 = False
loopcatch3 = False
loopcatch4 = False
loopcatch5 = False
counter = 0

l1 = []
l2 = []
l3 = []
l4 = []
l5 = []

def list_creation(lst):
    global loopcatch1, loopcatch2, loopcatch3, loopcatch4, loopcatch5, counter
    global l1, l2, l3, l4, l5
    #variables needed
    if counter == 1:
        l1 = lst #list 1 becomes lst
        lst = [] #clears lst to be used on l2
    elif counter == 2:
        l2 = lst
        lst = []
    elif counter == 3:
        l3 = lst
        lst = []
    elif counter == 4:
        l4 = lst
        lst = []
    elif counter == 5:
        l5 = lst
        lst = []
    counter += 1
    #first start comes here first
    if len(l1) == 365 and loopcatch1:
        print("list 1 created...")
    else:
        loopcatch1 = True #catches get flipped to true on pass
        lst = l1
        randomizer(lst)

    if len(l2) == 365 and loopcatch2:
        print("list 2 created...")
    else:
        loopcatch2 = True
        lst = l2
        randomizer(lst)

    if len(l3) == 365 and loopcatch3:
        print("list 3 created...")
    else:
        loopcatch3 = True
        lst = l3
        randomizer(lst)

    if len(l4) == 365 and loopcatch4:
        print("list 4 created...")
    else:
        loopcatch4 = True
        lst = l4
        randomizer(lst)

    if len(l5) == 365 and loopcatch5:
        print("list 5 created...")
    else:
        loopcatch5 = True
        lst = l5
        randomizer(lst)

    printlist(l1, l2, l3, l4, l5)
def randomizer(lst):
        #for randomization boundaries will be highest and lowest avg temp for the month according to google, may add rudamentary fronts and boundaries if i have time
        #this may lead to sharp inclines of temperatures when months begin and end, 
        #adding fronts and boundaries would mitigate sharp spikes between months, but would also produce sharp spikes of their own like real world
        jan = 31
        feb = 28 #one month with 28
        mar = 31
        apr = 30
        may = 31
        jun = 30
        jul = 31
        aug = 31
        sep = 30
        octo = 31
        nov = 30
        dec = 31
        
        for i in range(jan): #generate random temps based on average low and high in newton ks
            lst.append(random.randint(19, 41))
        for i in range(feb):
            lst.append(random.randint(24, 47))
        for i in range(mar):
            lst.append(random.randint(33, 56))
        for i in range(apr):
            lst.append(random.randint(42, 66))
        for i in range(may):
            lst.append(random.randint(54, 76))
        for i in range(jun):
            lst.append(random.randint(64, 86))
        for i in range(jul):
            lst.append(random.randint(69, 92))
        for i in range(aug):
            lst.append(random.randint(67, 91))
        for i in range(sep):
            lst.append(random.randint(58, 82))
        for i in range(octo):
            lst.append(random.randint(45, 69))
        for i in range(nov):
            lst.append(random.randint(33, 55))
        for i in range(dec):
            lst.append(random.randint(22, 42))


def main():
    lst = []
    print("Temperture Forecaster")
    print("--generate 5 files of yearly temps because i dont want to put it in by hand--")
    print('--Requires 5 years of temperature data--')
    sel = 0
    print("Enter 1 to randomize 5 past years of temperatures,")
    sel = int(input('Enter 2 to choose your files:'))
    if sel == 1:
        list_creation(lst)
    elif sel == 2:
        print('bruh')



def printlist(l1, l2, l3, l4, l5):
    #write each list into corresponding file
    with open("temp1.txt", "w") as output:
        output.write(str(l1))

    with open("temp2.txt", "w") as output:
        output.write(str(l2))

    with open("temp3.txt", "w") as output:
        output.write(str(l3))

    with open("temp4.txt", "w") as output:
        output.write(str(l4))

    with open("temp5.txt", "w") as output:
        output.write(str(l5))
    print('done')
main()
