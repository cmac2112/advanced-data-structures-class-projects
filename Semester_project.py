#semester project
#program to take an array of temperatures from years past and use such temperatures and trends to predict the next years temperatures
# Then use sort to find, warmest, coldest, coldest stretch, warmest stretch of the year

# Option to import your own temperatures
# Option to randomly generate temperatures accurate to what they may be in a specific location in real life
from tkinter import *
from tkinter import filedialog
import random
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
import pandas as pd
loopcatch1 = False
loopcatch2 = False
loopcatch3 = False
loopcatch4 = False
loopcatch5 = False
counter = 0
#global variables needed to store lists of temperatures for each year
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
        

    print_list(l1, l2, l3, l4, l5)
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
    print("--This program will take temperatures from years past and use them to predict the temperature for the next year--")
    sel = 0
    print("Enter 1 to randomize 5 past years of temperatures,")
    sel = int(input('Enter 2 to choose your files:'))
    if sel == 1:
        list_creation(lst)
    elif sel == 2:
        print('wip')


def print_list(l1, l2, l3, l4, l5):
    choice = 0
    print('list 1')
    print(l1)
    print('list 2')
    print(l2)
    print('list 3')
    print(l3)
    print('list 4')
    print(l4)
    print('list 5')
    print(l5)
    print('Enter 1 to continue to plotting')
    print('Enter 2 to go to highlights')
    print('Enter 3 to predict next years temps')
    if choice == 1:
        plotting(l1, l2, l3, l4, l5)
    elif choice == 2:
        highlights(l1, l2, l3, l4, l5)
    else:
        predicting(l1, l2, l3, l4, l5)



def plotting(l1, l2, l3, l4, l5):
    print('----Plotting Menu----')
    # Generate line plot for each of the five lists
    fig, axs = plt.subplots(5, 1, figsize=(10, 20))
    axs[0].plot(range(len(l1)), l1)
    axs[0].set_title('List 1')
    axs[1].plot(range(len(l2)), l2)
    axs[1].set_title('List 2')
    axs[2].plot(range(len(l3)), l3)
    axs[2].set_title('List 3')
    axs[3].plot(range(len(l4)), l4)
    axs[3].set_title('List 4')
    axs[4].plot(range(len(l5)), l5)
    axs[4].set_title('List 5')

    # Set common x and y labels for all subplots
    fig.text(0.5, 0.04, 'Days', ha='center', va='center', fontsize=16)
    fig.text(0.06, 0.5, 'Temperature (F)', ha='center', va='center', rotation='vertical', fontsize=16)

    # Show the plot
    plt.show()

    fig, axs = plt.subplots(5, 1, figsize=(10, 20))
    axs[0].scatter(range(len(l1)), l1)
    axs[0].set_title('List 1')
    axs[1].scatter(range(len(l2)), l2)
    axs[1].set_title('List 2')
    axs[2].scatter(range(len(l3)), l3)
    axs[2].set_title('List 3')
    axs[3].scatter(range(len(l4)), l4)
    axs[3].set_title('List 4')
    axs[4].scatter(range(len(l5)), l5)
    axs[4].set_title('List 5')

    # Set common x and y labels for all subplots
    fig.text(0.5, 0.04, 'Days', ha='center', va='center', fontsize=16)
    fig.text(0.06, 0.5, 'Temperature (F)', ha='center', va='center', rotation='vertical', fontsize=16)

    # Show the plot
    plt.show()
def highlights(l1, l2, l3, l4, l5):
    print('wip')
def predicting(l1, l2, l3, l4 ,l5):
    #using tensorflow to train on these pipelines
    model = Sequential() #units are neurons, 
    model.add(Dense(units=32, activation='relu', input_dim=len(l1)))
    model.add(Dense(units=64, activation='relu'))
    model.add(Dense(units=1, activation='sigmoid'))#sigmoid activation will take
    #ouput from 2 above and convert it to 1 or 0 or 'yes' and 'no' filter
    model.compile(loss='binary_crossentropy', optimizer='sqd', metrics='accuracy')
    gp = model.fit(l1, epochs=200, batch_size = 32)

main()
