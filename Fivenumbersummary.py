
#from __future__ import division

def median(list_of_numbers):
# this function takes a list of sorted numbers and calculates the median
    if (len(list_of_numbers)%2 ==0):

        firstMiddleNumber=list_of_numbers[(len(list_of_numbers)/2)-1]

        lowerlimitIndex=len(list_of_numbers)/2 # I aded -1  because the index starts from 0
        secondMiddleNumber=list_of_numbers[(len(list_of_numbers)/2)]

        Median=float(firstMiddleNumber + secondMiddleNumber)/2



    else:
        MiddleNumber=list_of_numbers[((len(list_of_numbers)+1)/2)-1]

        lowerlimitIndex=len(list_of_numbers)/2 # I aded -1  because the index starts from 0
        Median=MiddleNumber

    return Median


def getLowerandUpperhalf(list_of_numbers):
    # this function takes a list of numbers and seperates them into two lists lowerhalf and upperhalf
    list_of_numbers.sort()
    if (len(list_of_numbers)%2 ==0):

        lowerlimitIndex=len(list_of_numbers)/2 # I aded -1  because the index starts from 0
        lowerhalf=list_of_numbers[0: lowerlimitIndex]
        print "Lowerhalf",lowerhalf,'\n'
        upperhalf=list_of_numbers[(lowerlimitIndex):]
        print "Upperhalf",upperhalf,'\n'
    else:

        lowerlimitIndex=len(list_of_numbers)/2 # I aded -1  because the index starts from 0

        # getting lower half and upper half
        lowerhalf=list_of_numbers[0: lowerlimitIndex]
        print "lowerhalf",lowerhalf,'\n'
        upperhalf=list_of_numbers[(lowerlimitIndex+1):]
        print "upperhalf",upperhalf,'\n'
    return lowerhalf,upperhalf



def outlierDetection(Q1,Q3,list_of_numbers):
    #this function takes a list of numbers and prints out those numbers that are considered outliers
    IQR= float(Q3-Q1)
    print "IQR",IQR
    lowerthreshold=Q1-(IQR*1.5)
    print "Lowerthreshold= ",lowerthreshold
    upperthreshold=Q3+(IQR*1.5)
    print "Upperthreshold= ",upperthreshold
    for i in list_of_numbers:
        lowflag=0
        highflag=0
        if (i <lowerthreshold):
            lowflag=1
        if (i>upperthreshold):
            highflag=1
        if (lowflag):
            print i , "is an outlier because it is lower than than the lowerthreshold"
        if (highflag):
            print i , "is an outlier because it is higher than than the upperthreshold"

# different lists
list_of_numbers=[53,79,80,82,87,91,93,98]
#list_of_numbers=[53,79,80,82,87,91,93,98,57,79,99,66]
#list_of_numbers=[1,1,4,4,9,11]

#the numbers need to be sorted first
list_of_numbers.sort()
print "The observations after sorting: ", list_of_numbers,'\n'


# printing the number of observations
print  "Number of observations =  ",len(list_of_numbers),'\n'

# getting the Value of Q2 which is the median of the whole dataset
Q2= median(list_of_numbers)

#extracting the numbers that will be used to calculate Q1 which I refere to as the lowerhalf
# and the numbers that will be used to calculate the Q3 which I refere to as the upperhalf
lowerhalf,upperhalf=getLowerandUpperhalf(list_of_numbers)


# calculating the Q1 from the lowerhalf
Q1=median(lowerhalf)
# calculating the Q3 from the upperhalf
Q3=median(upperhalf)


# getting the minimum number of the list
Min=list_of_numbers[0]

#getting the maximum number of the list
Max=list_of_numbers[-1]



# printing the five number summary
print "Five Number Summary ",Min, Q1, Q2, Q3, Max,'\n'

# getting the outliers
outlierDetection(Q1,Q3,list_of_numbers)