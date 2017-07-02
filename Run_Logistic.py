"""KAGGLE: TITANIC CHALLENGE
USE WITH ANACONDA AND PYTHON 2.7

Designed as a class (Logistic). Visualize class can also give you scatter or density plot.

What it does:
	1. Runs logistic regression on given data
	2. Tests regression with training set and predicts accuracy
	3. Gives outfile csv with PassengerId and prediction

Critical issues:
	1. Patients from the Test set who have incomplete data are considered to have not survived.
"""

"""
THINGS TO DO:
    1. create a plot that isolates only one variable but holds the others constant
    2. run PCA analysis
    3. Try bootstrap method
    4. Try probability-based method
"""

import numpy as np
import pandas as p
import matplotlib.pyplot as plt
import ggplot as gg
from sklearn import linear_model


class Visualize(object):
	def __init__(self, data):
		self.data = data

	def view(self):
		return self.data

	def scatter_plot(self, inp1, inp2, inp3=''):
		p = gg.ggplot(gg.aes(x=inp1, y=inp2, color=inp3), data=self.data) + \
		gg.geom_point()

		print p

	def density(self, inp1, inp2, inp3):
		return gg.ggplot(self.data, gg.aes(x=inp1, color=inp2, fill=inp2)) +\
  	  		gg.geom_density(alpha=0.5, size=5) +\
  	  		gg.facet_grid(inp3) +\
  	  		gg.ggtitle('Density of Fare by Sex and Survival Status') +\
  	  		gg.ylab('Survival Status')

class Logistic(object):
	def __init__(self,data):
		#remember all vars should have the same shape
		self.data = data
		#interaction between Pclass and Fare
		try:
			self.newdf = data[['Survived','Pclass','Sex','SibSp','Parch','Age','Fare']].dropna(axis=0, how='any')
		except:
			self.newdf = data[['Sex','Pclass','Age','SibSp','Parch','Fare']]

		self.X = self.newdf[['Sex','Pclass','Age','SibSp','Parch','Fare']]

		try:
			self.y = self.newdf[['Survived']]
		except:
			self.y = []

	def tellshape(self):
		return self.data.values.shape

	def newdataframe(self):
		return self.newdf

	def model(self, x):
		return 1 / (1 + np.exp(-x))

#next move: create ROC curve?
	def runlog(self):
		clf = linear_model.LogisticRegression(C=1e5)
		clf.fit(self.X, self.y.values.ravel())


		#self.plotlog(clf)

		return (clf.coef_, clf.intercept_)

#rewrite this so that you're changing only one variable (age), but you're keeping all the other variables constant. The original sample code had only one variable,
#so they made a 300x1 array of random values. You need all the variables to be the same except Age in your 714xN array.
	def plotlog(self,inst):

		plt.figure(1, figsize=(10, 6))
		plt.clf()

		plt.scatter(self.X['Age'], self.y, color='black', zorder=20) #only plotted one var: 'Age' with 'Surivival'
		X_test = np.linspace(0, 100, 300) #create a bunch of random data points

		coefarray = np.dot(X_test.reshape(300,1),inst.coef_) #the coef should be 1x5 matrix
		coeflist = [x + inst.intercept_[0] for x in np.sum(coefarray,axis=1).tolist()]
		#loss = ((lambda x: 1 / (1 + np.exp(-x))) (np.asarray(coeflist))).ravel() #did it add the intercept to every element of the list?
		#loss = ((lambda x: 1 / (1 + np.exp(-x))) (coeflist)).ravel() #generates test line
		loss = self.model(np.asarray(coeflist)).ravel()
		print loss
		plt.plot(X_test, loss, color='red', linewidth=3)

		plt.axhline(.5, color='.5')

		plt.ylabel('Survived')
		plt.xlabel('Age')
		plt.xticks(range(0, 80, 10))
		plt.yticks([0, 0.5, 1])
		plt.ylim(-.25, 1.25)
		plt.xlim(0, 80)

		plt.show()

	def create_row_matrix(self,rowtuple):
		rowmatrix = []
		for el in rowtuple:
			rowmatrix.append(el)
		return rowmatrix[1:]

	def predict(self,coeflist,intercept):
		xlist = []
		#multiply the coefficients by the observations and sum all with intercept
		for row in self.X.itertuples():
			#print self.create_row_matrix(row) * coeflist #I confirmed they are multiplying correctly
			xlist.append(np.sum(self.create_row_matrix(row)*coeflist) + intercept)

		#plug into logistic equation
		resultlist = [self.model(x) for x in xlist]

		#convert results into a prediction
		predictlist = []

		for item in np.nan_to_num(resultlist):
			if item >= 0.5:
				predictlist.append(1)
			else:
				predictlist.append(0)
			
		print 'Number of Observations:', len(predictlist)

		return predictlist

	def calcacc(self,predictlist):
		#assess accuracy of prediction
		survived = self.y['Survived'].tolist()
		tally = 0

		for i in range(len(survived)):
			if survived[i] == predictlist[i]:
				tally += 1
		
		#Return Score
		return 'Accuracy: {}'.format(float(tally) / float(len(predictlist)))

#save results to a list
def outcsv(ID,resultlist):
	path = 'results.csv'
	fhnd = open(path,'w')

	fhnd.write('PassengerId,Survived\n')

	for index in range(len(resultlist)):
		fhnd.write(str(ID[index]) + ',' + str(resultlist[index])+'\n')

	fhnd.close()

#trainset = p.read_csv('train.csv')
trainset = p.read_csv('prob_train.csv')
#trainset = trainset.replace(to_replace={'Sex':{'female':1,'male':0}})
#trainset = trainset.replace(to_replace={'Survived':{0:'Dead',1:'Survived'}})
#d = Visualize(trainset)
#d.scatter_plot('Age','Fare','Survived')

e = Logistic(trainset)
#print e.tellshape()
#print e.newdataframe()
#e.runlog()
print e.calcacc(e.predict(*e.runlog()))

testset = p.read_csv('test.csv')
testset = testset.replace(to_replace={'Sex':{'female':1,'male':0}})
f = Logistic(testset)


outcsv(testset['PassengerId'],f.predict(*e.runlog()))