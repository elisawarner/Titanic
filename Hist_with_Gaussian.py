""" HISTOGRAM FOR Pclass, but can change to anything by replacing 'Pclass' in lines 24 and 29 with different column """

#Assignment this week: Check the distributions of the data
#Which distribution is the best fit: uniform, Gaussian, skewed


import sys
import numpy as np
import pandas as p
import pylab as pl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.stats as stats

#import as dataframe
trainset = p.read_csv('train.csv')
#female is 1, male is 0
trainset = trainset.replace(to_replace={'Sex':{'female':1,'male':0}})

#trainset.hist(column = 'Age')
#plt.show()


h = sorted([x for x in trainset['Pclass'] if np.isnan(x) == False])
print h

fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed

pl.title('Pclass Histogram with Gaussian Distribution')
pl.plot(h,fit,'-o')
pl.hist(h,normed=True)
pl.show()                   #use may also need add this 

#issue dataframe file has NaN values. So you can't use pylab or matplotlib for a histogram of the data - only numpy. But it seems to be difficult to graph a histogram with the density curve on top if you're not using the same packages

#the issue with the plot graph is that the data is not sorted, so you're getting wacky staggered stuff. You want to sort the data, then
# have it plot for evenly numbered spaces, the normal distribution. Probably you need to make your own linespaces, but make the normal curve
# match to the trainset data.

#No, you should plot age as the x axis first. Then plot a normal curve of the data. Later you can figure out how to overlay that.

#Or, you can just try to plot everything with the matplotlib histogram function but clean the data first. Might be the best choice honestly to avoid all the math.

#https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html.  #the easiest solution
#https://stackoverflow.com/questions/10138085/python-pylab-plot-normal-distribution #if you want to try to manipulate the data