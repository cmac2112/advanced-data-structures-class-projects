#semester project
#program to take a list of temperatures from years past and use such temperatures and trends to predict the next years temperatures
# Then use sort to find, warmest, coldest, coldest stretch, warmest stretch of the year

# Option to import your own temperatures
# Option to randomly generate temperatures accurate to what they may be in a specific location in real life
print('loading...')
from tkinter import Tk
from tkinter.filedialog import Open, askopenfilename
import random
import matplotlib.pyplot as plt
import pandas as pd
#import tensorflow as tf
#from tensorflow.keras.models import Sequential, load_model
#from tensorflow.keras.layers import Input, Dense
import numpy as np
loopcatch1 = False
loopcatch2 = False #loop catchers to stop list creation from iterating over same lists
loopcatch3 = False
loopcatch4 = False
loopcatch5 = False
counter = 0
#global variables needed to store lists of temperatures for each year





def list_creation(lst):
    global loopcatch1, loopcatch2, loopcatch3, loopcatch4, loopcatch5, counter
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = [] 
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
        ul1 = lst
        
    if len(l2) == 365 and loopcatch2:
        print("list 2 created...")
    else:
        loopcatch2 = True
        lst = l2
        randomizer(lst)
        ul2 = lst
    if len(l3) == 365 and loopcatch3:
        print("list 3 created...")
    else:
        loopcatch3 = True
        lst = l3
        randomizer(lst)
        ul3 = lst
    if len(l4) == 365 and loopcatch4:
        print("list 4 created...")
    else:
        loopcatch4 = True
        lst = l4
        randomizer(lst)
        ul4 = lst
    if len(l5) == 365 and loopcatch5:
        print("list 5 created...")
    else:
        loopcatch5 = True
        lst = l5
        randomizer(lst)
        ul5 = lst
    print_list(l1, l2, l3, l4, l5)

def randomizer(lst):
        #for randomization boundaries will be highest and lowest avg temp for the month according to google, may add rudamentary fronts and boundaries if i have time
        #this may lead to sharp inclines of temperatures when months begin and end, 
        #adding fronts and boundaries would mitigate sharp spikes between months, but would also produce sharp spikes of their own like real world
        # too complicated to code for only a semester 
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
        
        for i in range(jan): #generate random temps based on average low and high in newton ks in ferenhight
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
    print("-----------Temperture Forecaster-----------")
    print("This program will take temperatures from years past and use them to predict the temperature for the next year")
    print('Requires 5 years of temperature data')
    sel = 0
    print("1: Randomize 5 past years of temperatures")
    print('2: Choose your files:')
    print('-------------------------------------------')
    sel = int(input('Enter a Selection:'))
    if sel == 1:
        list_creation(lst)
    elif sel == 2:
        file_select()
    else:
        print('Enter a valid number')
        main()

def file_select():
    print('Select files in order of years...')
    Tk().withdraw()
    file1 = askopenfilename() #use tkinter to give a gui to find files
    print(file1)
    with open(file1) as f:
        ls1 = [line.rstrip() for line in f]#open the file to read #move over to a list for easy sorting later 
    #need to be converted to integers
    l1 = conv_int(ls1)
    ul1 = l1 #need to keep unsorted lists for plotting in case user sorts first
    #do this for each 5 required files
    Tk().withdraw()
    file2 = askopenfilename()
    print(file2)
    with open(file2) as f:
        ls2 = [line.rstrip() for line in f] #would be useful to have a loop but dont know how
    l2 = conv_int(ls2)
    ul2 = l2
    Tk().withdraw()
    file3 = askopenfilename()
    print(file3)
    with open(file3) as f:
        ls3 = [line.rstrip() for line in f] 
    l3 = conv_int(ls3)
    ul3 = l3
    Tk().withdraw()
    file4 = askopenfilename()
    print(file4) 
    with open(file4) as f:
        ls4 = [line.rstrip() for line in f]
    l4 = conv_int(ls4)
    ul4 = l4
    Tk().withdraw()
    file5 = askopenfilename()
    print(file5) 
    with open(file5) as f:
        ls5 = [line.rstrip() for line in f]
    l5 = conv_int(ls5)
    ul5 = l5
    print_list(l1, l2, l3, l4, l5)
    
def conv_int(lst):
    #needed to convert imported txt files to integers to be use
    for i in range(0, len(lst)):
        lst[i] = int(lst[i]) #element at i equals integer element at i
    return lst #return integer list



def print_list(l1, l2, l3, l4, l5):        
    print('--------------------------------------')
    print('If you would like to analyze some of the given data already, choose and option below.')
    print('1: to go to plotting')
    print('2: to view highlights of the data')
    print('3: to continue to predicting next year')
    print('--------------------------------------')
    choice = int(input('Enter a Choice:'))
    if choice == 1:
        plotting(l1, l2, l3, l4, l5)
    elif choice == 2:
        highlights(l1, l2, l3, l4, l5)
    else:
        predicting(l1, l2, l3, l4, l5)




def predicting(l1, l2, l3, l4, l5):                                                   #predicting function
    all_lists = [l1, l2, l3, l4, l5]

# Calculate the average of each list's corresponding index for each of the 365 elements
    averages = [] #create new list to store averages in
    for i in range(365): # the length of the lists
        sum_at_index = 0 #creates varible to be used and reset
        for lst in all_lists: #for index in all lists
            sum_at_index += lst[i] #adds all numbers at specific index
        averages.append(sum_at_index/5)#appends calculation to new list
# Print the averages
    print(averages) #lot easier than tensorflow
    print('1: plotting')
    print('2: Highlights')
    ch = int(input('Enter a value:'))
    if ch == 1:
        pre_plotting(averages, l1, l2, l3, l4, l5)
    elif ch == 2:
        pre_highlights(averages, l1, l2, l3, l4, l5)
    else:
        print('Enter valid choice')
        predicting(l1, l2, l3, l4, l5)
    
# old function using tensorflow, spent about 10 hours trying
    #to get it figured out, got it to predict 1 year after about
    #20 minutes of loading, would take to long to present in class
    #just going to leave it up to finding the average of each index
    #this part does not work and has been changed                                                
#def predicting(l1, l2, l3, l4, l5):                                               #old predicting function using tensorflow
    # Convert lists to numpy arrays
    #input_data = np.array(l1).reshape(-1, 365, 1)

   # Define the model
    #model = tf.keras.Sequential([
    #tf.keras.layers.Dense(64, activation='relu', input_shape=(365,)),
    #tf.keras.layers.Dense(64, activation='relu'),
    #tf.keras.layers.Dense(1)
    #])

    # Compile the model
    #model.compile(optimizer='adam', loss='mse')

    # Train the model on the input data
    #model.fit(input_data, l1, epochs=100)

    # Make a prediction for the same training data
    #new_data = input_data
    #prediction = model.predict(new_data)

    # Print the result in a new list
    #result = prediction.tolist()
    #print(result)


def pre_plotting(lst, l1, l2, l3, l4, l5):                                              #predicted temperature plotting function
    print('====Predicted Plotting====')
    # Generate line plot for each of the five lists
    fig, axs = plt.subplots(6, 1, figsize=(10, 20)) #line graph parameters
    axs[0].plot(range(len(l1)), l1)
    axs[0].set_title('Year 1')
    axs[1].plot(range(len(l2)), l2)
    axs[1].set_title('Year 2')
    axs[2].plot(range(len(l3)), l3)
    axs[2].set_title('Year 3')
    axs[3].plot(range(len(l4)), l4)
    axs[3].set_title('Year 4')
    axs[4].plot(range(len(l5)), l5)
    axs[4].set_title('Year 5')
    axs[5].plot(range(len(lst)), lst)
    axs[5].set_title('Next Year')

    # Set common x and y labels for all subplots
    fig.text(0.5, 0.04, 'Days', ha='center', va='center', fontsize=16)
    fig.text(0.06, 0.5, 'Temperature (F)', ha='center', va='center', rotation='vertical', fontsize=16)

    # Show the plot
    plt.show()

    fig, axs = plt.subplots(6, 1, figsize=(10, 20)) #scatter plot parameters
    axs[0].scatter(range(len(l1)), l1)
    axs[0].set_title('Year 1')
    axs[1].scatter(range(len(l2)), l2)
    axs[1].set_title('Year 2')
    axs[2].scatter(range(len(l3)), l3)
    axs[2].set_title('Year 3')
    axs[3].scatter(range(len(l4)), l4)
    axs[3].set_title('Year 4')
    axs[4].scatter(range(len(l5)), l5)
    axs[4].set_title('Year 5')
    axs[5].scatter(range(len(lst)), lst)
    axs[5].set_title('Next Year')
    # Set common x and y labels for all subplots
    fig.text(0.5, 0.04, 'Days', ha='center', va='center', fontsize=16)
    fig.text(0.06, 0.5, 'Temperature (F)', ha='center', va='center', rotation='vertical', fontsize=16)
    plt.show()
    pre_highlights(lst, l1, l2, l3, l4, l5)




def pre_highlights(lst, l1, l2, l3, l4, l5):                                                #predicted temperature highlights
    print('Highlights of the predicted year.') 
    print('---------------------------------')
    print('Here you can view the hottest and coldestdays.')
    print('And you can also find the hottest streches of days, and coldest streches of days.')
    print('1: View hottest and coldest days of the year.')
    choice = 0
    print('2: Hottest and Coldest strech of days:')
    print('3: To continue to plotting')
    print('---------------------------------')
    choice = int(input('Enter a value to continue:'))
    if choice == 1:
        unsorted = lst.copy()                           #copy unsorted lists so they dont get sorted if user wishes to see plotting after running this
        slist = sorting(lst)
        print('------------------------')
        print('Coldest Day predicted...')
        print(lst[0])
        print('Warmest Day predicted...')
        print(lst[364])
        print('------------------------')
        pre_highlights(unsorted, l1, l2, l3, l4, l5)
    elif choice == 2:
        max_mean = highest_temp(lst)
        print('------------------------------------------------------------------')
        print('Warmest Mean Temp - Temps those days - What day start')
        print(max_mean)
        print('------------------------------------------------------------------')
        low = lowest_temp(lst)
        print('------------------------------------------------------------------')
        print('Coldest Mean Temp - Temps those days - What day start')
        print(low)
        print('------------------------------------------------------------------')
        pre_highlights(lst, l1, l2, l3, l4, l5)
    elif choice == 3:
        pre_plotting(lst, l1, l2, l3, l4, l5)

    else:
         print('Invalid entry')
         pre_highlights(lst)
def pre_storeforsort(lst, l1, l2, l3, l4, l5):                          #stores unsorted values and passes them back to the pre_highlight function so plotting is not wrong
    ul1 = l1.copy()
    ul2 = l2.copy()
    ul3 = l3.copy()
    ul4 = l4.copy()
    ul5 = l5.copy()
    ulst = lst.copy()
    sort_print(l1, l2, l3, l4, l5)
    highlights(ulst, ul1, ul2, ul3, ul4, ul5)


    
def plotting(l1, l2, l3, l4, l5):                                   #plotting function
    print('----Plotting Menu----')
    # Generate line plot for each of the five lists
    fig, axs = plt.subplots(5, 1, figsize=(10, 20)) #line graph
    axs[0].plot(range(len(l1)), l1)
    axs[0].set_title('Year 1')
    axs[1].plot(range(len(l2)), l2)
    axs[1].set_title('Year 2')
    axs[2].plot(range(len(l3)), l3)
    axs[2].set_title('Year 3')
    axs[3].plot(range(len(l4)), l4)
    axs[3].set_title('Year 4')
    axs[4].plot(range(len(l5)), l5)
    axs[4].set_title('Year 5')

    # Set common x and y labels for all subplots
    fig.text(0.5, 0.04, 'Days', ha='center', va='center', fontsize=16)
    fig.text(0.06, 0.5, 'Temperature (F)', ha='center', va='center', rotation='vertical', fontsize=16)

    # Show the plot
    plt.show()

    fig, axs = plt.subplots(5, 1, figsize=(10, 20)) #scatter plot 
    axs[0].scatter(range(len(l1)), l1)
    axs[0].set_title('Year 1')
    axs[1].scatter(range(len(l2)), l2)
    axs[1].set_title('Year 2')
    axs[2].scatter(range(len(l3)), l3)
    axs[2].set_title('Year 3')
    axs[3].scatter(range(len(l4)), l4)
    axs[3].set_title('Year 4')
    axs[4].scatter(range(len(l5)), l5)
    axs[4].set_title('Year 5')

    # Set common x and y labels for all subplots
    fig.text(0.5, 0.04, 'Days', ha='center', va='center', fontsize=16)
    fig.text(0.06, 0.5, 'Temperature (F)', ha='center', va='center', rotation='vertical', fontsize=16)

    # Show the plot
    plt.show()
    print('Continuing to highlights....')
    highlights(l1, l2, l3, l4, l5)
    
def highlights(l1, l2, l3, l4, l5):                                      #highlight function
    print('Highlights of the year.')
    print('----------------------')
    print('Here you can view the hottest and coldest days.')
    print('And you can also find the hottest streches of days, and coldest streches of days.')
    print('1: View hottest and coldest days of the year.')
    choice = 0
    print('2: Hottest and Coldest strech of days:')
    print('------------------------')
    choice = int(input('Enter a value to continue:'))
    if choice == 1:
        storeforsort(l1, l2, l3, l4, l5)
    elif choice == 2:
         stret(l1, l2, l3, l4, l5)
    else:
         print('Invalid Entry')
         highlights(l1, l2, l3, l4, l5)

def sorting(lst):               
    print('----Sorting----')
    #must sort first
    for i in range(1, len(lst)):                #insertino sort
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1
    return lst

def storeforsort(l1, l2, l3, l4, l5):           #store for sort for non predicted items
                                                #probably just could have used this function again for predicted items but it works and im not trying it
    ul1 = l1.copy()
    ul2 = l2.copy()
    ul3 = l3.copy()
    ul4 = l4.copy()
    ul5 = l5.copy()
    sort_print(l1, l2, l3, l4, l5)
    print_list(ul1, ul2, ul3, ul4, ul5)
   
    #return back to the menu
    #return back only the non sorted version so plotting still works
    print_list(l1, l2, l3, l4, l5, ul1, ul2, ul3, ul4, ul5)
    #now take all of these and find hottest and coldest
def sort_print(l1, l2, l3, l4, l5):                             #sorting and printing the results
    sl1 = sorting(l1)
    sl2 = sorting(l2)   #sends lists to sorting function which is an insertion sort
    sl3 = sorting(l3)
    sl4 = sorting(l4)
    sl5 = sorting(l5)
    print('----Coldest Temperatures----')
    print(sl1[0])
    print(sl2[0])
    print(sl3[0])   #prints the first (0) index to find the coldest temp
    print(sl4[0])
    print(sl5[0])
    print('----Warmest Temperatures----')
    print(sl1[364])
    print(sl2[364])
    print(sl3[364])     #prints the last (364) index to find the warmest temps
                        #these more often than not, all 5 are often the same number, this is a limitation with this program, it does not account for outliers
    print(sl4[364])
    print(sl5[364])




def stret(l1, l2, l3, l4, l5):                  #function for the longest stretches of hot/ cold weather
    print('-----Stretches----')
    print('Here you can enter your year to analyze the longes stretch of warmest days.')
    print('------------------')
    print('Year 1')
    print('Year 2')
    print('Year 3')
    print('Year 4')
    print('Year 5')
    print('------------------')
    print('6: Exit')
    ch = int(input('Enter year number to continue:'))
    
    if ch == 1:                 #display and find mean temps, stretch of days, and what day the stretch lasted
       lst = l1
       max_mean = highest_temp(lst) #sends list to highest temp function
       print('-----------------------------------------------------------------')
       print('Warmest Mean Temp - Temps those days - What day start')
       print(max_mean)
       low = lowest_temp(lst) #sends list to lowest temp functoion
       print('------------------------------------------------------------------')
       print('Coldest Mean Temp - Temps those days - What day end')
       print(low)    #print results for selected 
       print('------------------------------------------------------------------')
    elif ch == 2:
       lst = l2
       max_mean = highest_temp(lst)
       print('-----------------------------------------------------------------')
       print('Warmest Mean Temp - Temps those days - What day start')
       print(max_mean)
       low = lowest_temp(lst)
       print('------------------------------------------------------------------')
       print('Coldest Mean Temp - Temps those days - What day end')
       print(low)
       print('------------------------------------------------------------------')
    elif ch == 3:
       lst = l3
       max_mean = highest_temp(lst)
       print('-----------------------------------------------------------------')
       print('Warmest Mean Temp - Temps those days - What day start')
       print(max_mean)
       low = lowest_temp(lst)
       print('------------------------------------------------------------------')
       print('Coldest Mean Temp - Temps those days - What day end')
       print(low)
       print('------------------------------------------------------------------')
    elif ch == 4:
       lst = l4
       max_mean = highest_temp(lst)
       print('-----------------------------------------------------------------')
       print('Warmest Mean Temp - Temps those days - What day start')
       print(max_mean)
       low = lowest_temp(lst)
       print('------------------------------------------------------------------')
       print('Coldest Mean Temp - Temps those days - What day end')
       print(low)
       print('------------------------------------------------------------------')
    elif ch == 5:
       lst = l5
       max_mean = highest_temp(lst)
       print('-----------------------------------------------------------------')
       print('Warmest Mean Temp - Temps those days - What day start')
       print(max_mean)
       low = lowest_temp(lst)
       print('------------------------------------------------------------------')
       print('Coldest Mean Temp - Temps those days - What day end')
       print(low)
       print('------------------------------------------------------------------')
    elif ch == 6:
        print_list(l1, l2, l3, l4, l5)
    stret(l1, l2, l3, l4, l5)




def lowest_temp(lst):                                       #lowest temperature stretch function
    lowest_mean = float('inf')  # initialize to infinity
    mean_days = None        #initialize varaibles to be used
    mean_start = None       #same
    for i in range(len(lst) - 6): 
        mean = sum(lst[i:i+7]) / 7  #make a sublist and find the mean between those
        if mean < lowest_mean:  #if found mean in sublist is less than the lowest found mean
            lowest_mean = mean  #lowest mean is replaced
            lowest_mean_days = lst[i:i+7]   #sublist is stored for use
            lowest_start = i        #start day is stored
    return lowest_mean, lowest_mean_days, lowest_start




def highest_temp(lst):                                      #highest temperature strech function
    n = len(lst) #find the length of the list to iterate
    max_mean = float('-inf') #equals some number
    mean_days = None #no days at first
    mean_start = None #index of days
    max_mean_days = None
    for i in range(n - 6): # iterate through each 7 day consecutive days
        mean = sum(lst[i:i+7])/7 #mean is equal to the sum of those
        #seven days divided by seven
        if mean > max_mean: #if found mean is greater than previous mean
            max_mean = mean #swap places
            max_mean_days = lst[i:i+7] #store those days to print later
            max_start = i
    return max_mean, max_mean_days, max_start
main()
