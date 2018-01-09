# Five Number Summary/BoxPlot


## This is an assignment where students were asked to do the following:


Use any programming language that you are familiar with and write a program that calculates the five-number summary min, Q1, Q2, Q3, max and determines the outliers from a given observation of numbers.

The program should have the following three functions:

•	Median: to calculate the Q1, Q2, Q3 after determining if the number of observations is an even or an odd number. 

•	GetTheLowerHalfandTheUpperHalf: that separates the observations into the lower-half and upper-half.

•	DetectTheOutliers: the function scans each number from the observation and prints it if it is an outlier.

The program should output a BoxPlot as well.
Don't forget to sort the observations.

There is two python files that produce the same output,
Fivenumbersummary.py and
 FivenumbersummaryNUMPY.py

## The difference between the two programs is that the former is shorter due to using the NUMPY library capabilities.


## The output of Fivenumbersummary.py and FivenumbersummaryNUMPY.py is as follows:

The observations after sorting:  [53, 79, 80, 82, 87, 91, 93, 98]

Number of observations =   8

Five Number Summary  53 79.75 84.5 91.5 98

IQR=  11.75

Lowerthreshold=  62.125

Upperthreshold=  109.125

53 is an outlier because it is lower than than the lowerthreshold

![Screenshot](boxplotnumpy.png)
