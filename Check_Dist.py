""" DISTRIBUTION TEST

This program gives you a distribution of the variables that you select in colname

"""

#Assignment this week: Check the distributions of the data
#Which distribution is the best fit: uniform, Gaussian, skewed


import sys
import numpy as np
import pandas as p
import pylab as pl
import scipy.stats as stats

#import as dataframe
trainset = p.read_csv('train.csv')

####### SAMPLE: DELETE LATER ##########
path = "sample_dist.txt"
file = open(path,'r')

wings = []
for val in file:
	wings.append(float(val))

#######################################



############### CHANGE THIS BOX ####################
colname = 'Fare'
####################################################

h = sorted([x for x in trainset[colname] if np.isnan(x) == False])
#print h
trainset = trainset.replace(to_replace={'Sex':{'female':1,'male':0}})


fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed


pl.title('%s Histogram with Gaussian Distribution' % (colname))
pl.ylabel('Frequency')
pl.xlabel(colname)
pl.plot(h,fit,'-o')
pl.hist(h,normed=True)
pl.show()                  

###### RUN KOLMOGOROV-SMIRNOV TEST ######
#significance should be > 0.05 and <= 1
#kstest needs z-scores

col_data_to_zscore = [(x-np.mean(h))/np.std(h) for x in h] #colname data
normal_test1 = stats.norm.rvs(size=100) #made-up normal distribution
normal_test2 = [(x-np.mean(wings))/np.std(wings) for x in wings] #wings data

print "\nP-VALUE > 0.05 MEANS DISTRIBUTION IS NORMAL\n"
print "KOLMOGOROV-SMIRNOV P-VALUE FOR %s\n" % (colname), stats.kstest(col_data_to_zscore,'norm')[1]
print "COMPARE TO NORMAL RESULTS 1 (RANDOM NORMAL DATA)\n",stats.kstest(normal_test1,'norm')[1]
print "COMPARE TO NORMAL RESULTS 2 (REAL DATA)\n",stats.kstest(normal_test2,'norm')[1]



# issue: fit is a list of z scores
# Age is a list of ages
# Solution: either convert z scores to ages or ages to z scores
# kstest is giving p-value of 0