""" DISTRIBUTION TEST: ADVANCED

1. This program gives you a distribution of the variables that you select in colname
2. This program runs the Kolmogorov-Smirnov tests for normal, uniform, and gumbel left and right skewed
3. If none of those distributions match, it allows you to test every distribution to find one that fits
4. If no distribution fits, it allows you to find the distribution with the best match (beta)

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

#col_data_to_zscore = stats.halfnorm.rvs(size=100) ##### FOR TESTING: DISREGARD #####

col_data_to_zscore = [(x-np.mean(h))/np.std(h) for x in h] #colname data
normal_test1 = stats.norm.rvs(size=100) #made-up normal distribution
normal_test2 = [(x-np.mean(wings))/np.std(wings) for x in wings] #wings data

pvalues = [stats.kstest(col_data_to_zscore,'norm')[1],stats.kstest(col_data_to_zscore,'gumbel_r')[1],stats.kstest(col_data_to_zscore,'gumbel_l')[1],stats.kstest(col_data_to_zscore,'uniform')[1]]

print "\nP-VALUE > 0.05 MEANS DISTRIBUTION IS NORMAL\n"
print "KOLMOGOROV-SMIRNOV NORMAL P-VALUE FOR %s\n" % (colname), pvalues[0]
print "COMPARE TO NORMAL RESULTS 1 (RANDOM NORMAL DATA)\n",stats.kstest(normal_test1,'norm')[1]
print "COMPARE TO NORMAL RESULTS 2 (REAL DATA)\n",stats.kstest(normal_test2,'norm')[1]


print "\n\nKOLMOGOROV-SMIRNOV SKEW RIGHT P-VALUE FOR %s\n" % (colname), pvalues[1]
print "KOLMOGOROV-SMIRNOV SKEW LEFT P-VALUE\n", pvalues[2]
print "KOLMOGOROV-SMIRNOV UNIFORM P-VALUE FOR %s\n" % (colname), pvalues[3]

dist_dict = {
			'alpha':'An alpha continuous random variable','anglit':'An anglit continuous random variable','arcsine':'An arcsine continuous random variable',
			'beta':'A beta continuous random variable','betaprime':'A beta prime continuous random variable','bradford':'A Bradford continuous random variable',
			'burr':'A Burr continuous random variable','cauchy':'A Cauchy continuous random variable','chi':'A chi continuous random variable',
			'chi2':'A chi-squared continuous random variable','cosine':'A cosine continuous random variable','dgamma':'A double gamma continuous random variable',
			'dweibull':'A double Weibull continuous random variable','erlang':'An Erlang continuous random variable','expon':'An exponential continuous random variable',
			'exponweib':'An exponentiated Weibull continuous random variable','exponpow':'An exponential power continuous random variable','f':'An F continuous random variable',
			'fatiguelife':'A fatigue-life (Birnbaum-Sanders) continuous random variable','fisk':'A Fisk continuous random variable','foldcauchy':'A folded Cauchy continuous random variable',
			'foldnorm':'A folded normal continuous random variable','frechet_r':'A Frechet right (or Weibull minimum) continuous random variable',
			'frechet_l':'A Frechet left (or Weibull maximum) continuous random variable','genlogistic':'A generalized logistic continuous random variable',
			'genpareto':'A generalized Pareto continuous random variable','genexpon':'A generalized exponential continuous random variable',
			'genextreme':'A generalized extreme value continuous random variable','gausshyper':'A Gauss hypergeometric continuous random variable',
			'gamma':'A gamma continuous random variable','gengamma':'A generalized gamma continuous random variable','genhalflogistic':'A generalized half-logistic continuous random variable',
			'gilbrat':'A Gilbrat continuous random variable','gompertz':'A Gompertz (or truncated Gumbel) continuous random variable','gumbel_r':'A right-skewed Gumbel continuous random variable',
			'gumbel_l':'A left-skewed Gumbel continuous random variable','halfcauchy':'A Half-Cauchy continuous random variable','halflogistic':'A half-logistic continuous random variable',
			'halfnorm':'A half-normal continuous random variable','hypsecant':'A hyperbolic secant continuous random variable','invgamma':'An inverted gamma continuous random variable',
			'invgauss':'An inverse Gaussian continuous random variable','invweibull':'An inverted Weibull continuous random variable',
			'johnsonsb':'A Johnson SB continuous random variable','johnsonsu':'A Johnson SU continuous random variable','ksone':'General Kolmogorov-Smirnov one-sided test',
			'kstwobign':'Kolmogorov-Smirnov two-sided test for large N','laplace':'A Laplace continuous random variable','logistic':'A logistic (or Sech-squared) continuous random variable',
			'loggamma':'A log gamma continuous random variable','loglaplace':'A log-Laplace continuous random variable','lognorm':'A lognormal continuous random variable',
			'lomax':'A Lomax (Pareto of the second kind) continuous random variable','maxwell':'A Maxwell continuous random variable',
			'mielke':'A Mielkes Beta-Kappa continuous random variable','nakagami':'A Nakagami continuous random variable','ncx2':'A non-central chi-squared continuous random variable',
			'ncf':'A non-central F distribution continuous random variable','nct':'A non-central Students T continuous random variable.','norm':'A normal continuous random variable',
			'pareto':'A Pareto continuous random variable','pearson3':'A pearson type III continuous random variable','powerlaw':'A power-function continuous random variable',
			'powerlognorm':'A power log-normal continuous random variable','powernorm':'A power normal continuous random variable','rdist':'An R-distributed continuous random variable',
			'reciprocal':'A reciprocal continuous random variable','rayleigh':'A Rayleigh continuous random variable','rice':'A Rice continuous random variable',
			'recipinvgauss':'A reciprocal inverse Gaussian continuous random variable', 'semicircular':'A semicircular continuous random variable','t':'A semicircular continuous random variable',
			'triang':'A triangular continuous random variable', 'truncexpon':'A truncated exponential continuous random variable','truncnorm':'A truncated normal continuous random variable',
			'tukeylambda':'A Tukey-Lamdba continuous random variable','uniform':'A uniform continuous random variable','vonmises':'A Von Mises continuous random variable',
			'wald':'A Wald continuous random variable','weibull_min':'A Frechet right (or Weibull minimum) continuous random variable','weibull_max':'A Frechet left (or Weibull maximum) continuous random variable',
			'wrapcauchy':'A wrapped Cauchy continuous random variable','bernoulli':'A Bernoulli discrete random variable','binom':'A binomial discrete random variable',
			'boltzmann':'A Boltzmann (Truncated Discrete Exponential) random variable','dlaplace':'A Laplacian discrete random variable','geom':'A geometric discrete random variable',
			'hypergeom':'A hypergeometric discrete random variable','logser':'A Logarithmic (Log-Series, Series) discrete random variable','nbinom':'A negative binomial discrete random variable',
			'planck':'A Planck discrete exponential random variable','poisson':'A Poisson discrete random variable','randint':'A uniform discrete random variable','skellam':'A Skellam discrete random variable',
			'zipf':'A Zipf discrete random variable'
			}

#if distribution not found with previous results, request test to find distribution?

if all(x < 0.05 for x in pvalues):
	answer = raw_input("Distribution not found. Test for possible distribution? (False Negatives or Positives may Ensue) y/n:  ")

	possible_dists = []
	test_results = {}
	missing_dists = []
	if answer == 'y' or answer == 'Y':
		for key in dist_dict:
			#print key
			try:
				#print stats.kstest(normal_test1,key)
				test_results[key] = stats.kstest(col_data_to_zscore,key)[1]
				if(float(stats.kstest(col_data_to_zscore,key)[1])) > 0.05:
					possible_dists.append(dist_dict[key])
			except:
				missing_dists.append(key)

#		possible_dists = [] ### FOR TESTING: DISREGARD ###
		if possible_dists == []:
			print "No distributions found."
			response_closest_answer = raw_input("Would you like to see the closest distribution? y/n: ")
			if response_closest_answer == 'y' or response_closest_answer == 'Y':
				highest_key = test_results.keys()[0]
				for key in test_results:
					if test_results[key] > test_results[highest_key]:
						highest_key = key
				if test_results[highest_key] != 0.0:
					print "BEST RESULT:",highest_key
				else:
					print "No results found"
				print "\n\nAll results:",test_results
		else:
			print "Possible Distributions:\n",', '.join(possible_dists)

		view_answer = raw_input("View untested distributions? y/n: ")
		if view_answer == 'y' or answer == 'Y':
			print view_answer
			print missing_dists


#results are 0 because Age has over 800 observations