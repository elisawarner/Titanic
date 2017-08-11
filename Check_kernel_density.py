import numpy as np
import pandas as p
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.neighbors.kde import KernelDensity

#import as dataframe
trainset = p.read_csv('train.csv')


############### CHANGE THIS BOX ####################
colname = 'Age'
min = 0
max = 100
bandwidth = 3
####################################################

x_grid = np.linspace(min, max, 1000)


#SET UP DATA
trainset = trainset.replace(to_replace={'Sex':{'female':1,'male':0}})
h = np.array(sorted([x for x in trainset[colname] if np.isnan(x) == False]))
#print h[:, np.newaxis]


#FIT DATA
"""Kernel Density Estimation with Scikit-learn"""
kde = KernelDensity(kernel='gaussian', bandwidth=bandwidth).fit(h[:, np.newaxis])
# score_samples() returns the log-likelihood of the samples
log_pdf = kde.score_samples(x_grid[:, np.newaxis])
test_data = np.exp(log_pdf)


#PLOT
# The grid we'll use for plotting
fig, ax = plt.subplots()

ax.plot(x_grid, test_data, color='red', alpha=1, lw=3)
ax.hist(h,color='0.75',normed=True)
plt.title(colname + ' Distribution, bandwidth =' + str(bandwidth))
plt.xlabel(colname)
plt.ylabel('Density')

plt.show()