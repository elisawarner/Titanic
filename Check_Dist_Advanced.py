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
colname = 'Age'
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

#Dictionary of all possible tests and their distributions
dist_dict = {
			'alpha':'An alpha continuous distribution','anglit':'An anglit continuous distribution','arcsine':'An arcsine continuous distribution',
			'beta':'A beta continuous distribution','betaprime':'A beta prime continuous distribution','bradford':'A Bradford continuous distribution',
			'burr':'A Burr continuous distribution','cauchy':'A Cauchy continuous distribution','chi':'A chi continuous distribution',
			'chi2':'A chi-squared continuous distribution','cosine':'A cosine continuous distribution','dgamma':'A double gamma continuous distribution',
			'dweibull':'A double Weibull continuous distribution','erlang':'An Erlang continuous distribution','expon':'An exponential continuous distribution',
			'exponweib':'An exponentiated Weibull continuous distribution','exponpow':'An exponential power continuous distribution','f':'An F continuous distribution',
			'fatiguelife':'A fatigue-life (Birnbaum-Sanders) continuous distribution','fisk':'A Fisk continuous distribution','foldcauchy':'A folded Cauchy continuous distribution',
			'foldnorm':'A folded normal continuous distribution','frechet_r':'A Frechet right (or Weibull minimum) continuous distribution',
			'frechet_l':'A Frechet left (or Weibull maximum) continuous distribution','genlogistic':'A generalized logistic continuous distribution',
			'genpareto':'A generalized Pareto continuous distribution','genexpon':'A generalized exponential continuous distribution',
			'genextreme':'A generalized extreme value continuous distribution','gausshyper':'A Gauss hypergeometric continuous distribution',
			'gamma':'A gamma continuous distribution','gengamma':'A generalized gamma continuous distribution','genhalflogistic':'A generalized half-logistic continuous distribution',
			'gilbrat':'A Gilbrat continuous distribution','gompertz':'A Gompertz (or truncated Gumbel) continuous distribution','gumbel_r':'A right-skewed Gumbel continuous distribution',
			'gumbel_l':'A left-skewed Gumbel continuous distribution','halfcauchy':'A Half-Cauchy continuous distribution','halflogistic':'A half-logistic continuous distribution',
			'halfnorm':'A half-normal continuous distribution','hypsecant':'A hyperbolic secant continuous distribution','invgamma':'An inverted gamma continuous distribution',
			'invgauss':'An inverse Gaussian continuous distribution','invweibull':'An inverted Weibull continuous distribution',
			'johnsonsb':'A Johnson SB continuous distribution','johnsonsu':'A Johnson SU continuous distribution','ksone':'General Kolmogorov-Smirnov one-sided test',
			'kstwobign':'Kolmogorov-Smirnov two-sided test for large N','laplace':'A Laplace continuous distribution','logistic':'A logistic (or Sech-squared) continuous distribution',
			'loggamma':'A log gamma continuous distribution','loglaplace':'A log-Laplace continuous distribution','lognorm':'A lognormal continuous distribution',
			'lomax':'A Lomax (Pareto of the second kind) continuous distribution','maxwell':'A Maxwell continuous distribution',
			'mielke':'A Mielkes Beta-Kappa continuous distribution','nakagami':'A Nakagami continuous distribution','ncx2':'A non-central chi-squared continuous distribution',
			'ncf':'A non-central F distribution continuous distribution','nct':'A non-central Students T continuous distribution.','norm':'A normal continuous distribution',
			'pareto':'A Pareto continuous distribution','pearson3':'A pearson type III continuous distribution','powerlaw':'A power-function continuous distribution',
			'powerlognorm':'A power log-normal continuous distribution','powernorm':'A power normal continuous distribution','rdist':'An R-distributed continuous distribution',
			'reciprocal':'A reciprocal continuous distribution','rayleigh':'A Rayleigh continuous distribution','rice':'A Rice continuous distribution',
			'recipinvgauss':'A reciprocal inverse Gaussian continuous distribution', 'semicircular':'A semicircular continuous distribution','t':'A semicircular continuous distribution',
			'triang':'A triangular continuous distribution', 'truncexpon':'A truncated exponential continuous distribution','truncnorm':'A truncated normal continuous distribution',
			'tukeylambda':'A Tukey-Lamdba continuous distribution','uniform':'A uniform continuous distribution','vonmises':'A Von Mises continuous distribution',
			'wald':'A Wald continuous distribution','weibull_min':'A Frechet right (or Weibull minimum) continuous distribution','weibull_max':'A Frechet left (or Weibull maximum) continuous distribution',
			'wrapcauchy':'A wrapped Cauchy continuous distribution','bernoulli':'A Bernoulli discrete distribution','binom':'A binomial discrete distribution',
			'boltzmann':'A Boltzmann (Truncated Discrete Exponential) distribution','dlaplace':'A Laplacian discrete distribution','geom':'A geometric discrete distribution',
			'hypergeom':'A hypergeometric discrete distribution','logser':'A Logarithmic (Log-Series, Series) discrete distribution','nbinom':'A negative binomial discrete distribution',
			'planck':'A Planck discrete exponential distribution','poisson':'A Poisson discrete distribution','randint':'A uniform discrete distribution','skellam':'A Skellam discrete distribution',
			'zipf':'A Zipf discrete distribution'
			}

###### TEST TO FIND A DISTRIBUTION THAT PASSES KS TEST ######
#if distribution not found with previous results, request test to find distribution
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

###### IF NO DISTRIBUTION IS FOUND, GIVES BEST RESULT BASED ON P-VALUE (FIND MAX P-VALUE) ######

#		possible_dists = [] ### FOR TESTING: DISREGARD ###
		if possible_dists == []:
			print "No distributions found."
			response_closest_answer = raw_input("\nWould you like to see the closest distribution? y/n: ")
			if response_closest_answer == 'y' or response_closest_answer == 'Y':
				highest_key = test_results.keys()[0]
				for key in test_results:
					if test_results[key] > test_results[highest_key]:
						highest_key = key
				if test_results[highest_key] != 0.0:
					print "\nBEST RESULT:",highest_key
				else:
					print "No results found"
				print "\n\nAll results:",test_results
		else:
			print "Possible Distributions:\n",', '.join(possible_dists)

###### GIVES UNTESTED DISTRIBUTIONS: those that threw an error, need more arguments ######
		view_answer = raw_input("\nView untested distributions? y/n: ")
		if view_answer == 'y' or answer == 'Y':
			print view_answer
			print missing_dists


#results are 0 because Age has over 800 observations