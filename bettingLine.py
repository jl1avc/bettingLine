# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 03:50:08 2022

@author: Jon

attached is a file of the first 8 weeks of the NFL season. 
 Columns are week, visit team, home team,
 the line (first entry is DAL at TB the betting line is -7.5,
 that means bookmakers expect if a large number of games were played between DAL and TB,
 at TB, the average difference in scores would be Tampa Bay to win by 7.5.
  The last column is the actual difference; in this case TB actually won by 2.   

Line 12  CLE at KC- the betting line is -8.  That means that the bookmakers expect,
 on average, KC would win by 8   The average difference in score CLE - KC would be 8.
  So the betting line is KC-8.  And it turned out that KC LOST the game by 4.

Using the data in the .csv file, construct a linear model:  actual score = b0 + b1* line

If the bookmakers were perfect, b0 would be 0 and b1 would be 1.
lineVSactual.csv 

Interpret the results.  Is b0 significantly different from 0?
 Is b1 significantly different from 1?

What does this mean about betting line in the NFL?
"""
import pandas as pd
from os import chdir
import matplotlib.pyplot as plt
import numpy as np

chdir('D:/')


dataSet = pd.read_csv('lineVSactual-1.csv')

type(dataSet)
dataSet.columns
BL = dataSet['line']
Result = dataSet['actual ']

print(f"mean of the line: {np.mean(BL): .2f}")
print(f"mean of the actual: {np.mean(Result): .3f}")

error = Result - BL
meanError = np.mean(error)
stdError = np.std(error)
print(f"mean error: {meanError: .2f}")
print(f"standard deviation: {stdError: .2f}")

y = normalApprox = np.random.normal(meanError, stdError, 1000)

plt.hist(dataSet['line'], alpha=0.5, label='line', density=True)
plt.hist(dataSet['actual '], alpha=0.5, label='actual ', density=True)
plt.hist(y, alpha=0.6, label='error', density=True)
plt.legend()
plt.grid()
plt.show()

plt.hist(y, density = True)



bllist = list(BL)
actlist = list(Result)
size = len(bllist)

#betting on the home team 

total = 0 
for x in range(size):
    if (bllist[x] + actlist[x] > 0):
        total += 10

    else:
        total -= 11
        
print(total)


#betting on visiting team


total = 0 
for x in range(size):
    if (bllist[x] + actlist[x] < 0):
        total += 10
    else:
        total -= 11
        
print(total)