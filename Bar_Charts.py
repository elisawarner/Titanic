""" BAR CHARTS FOR CATEGORICAL DATA (2 categories)

Rules:
	1. col2 must have only two categories (e.g. Sex or Survived)
	2. col can be any categorical variable column name
	3. Change xlabels to change the x labels. Data should be in numerical (0123) or alphabetical order (abcd)
"""

#Create Bar Charts for Categorical Data
#Side-by-side bar charts for survived [1] vs [0]
#Pclass, Sex, SibSp, Parch, Embarked


import numpy as np
import matplotlib.pyplot as plt
import pandas as p
 
#import as dataframe
trainset = p.read_csv('train.csv')
#female is 1, male is 0
#trainset = trainset.replace(to_replace={'Sex':{'female':1,'male':0}})


################# CHANGE DATA HERE ONLY ####################
# data to plot
#sorting:
col = 'Pclass'
#sorting by:
col2 = 'Survived'
quant_dict = {}
xlabels = ('1','2','3') #Remember should be in order numerically lowest to highest or alphabetically (not reversed)

############################################################

#Separates each column and their quantities
for ID in trainset['PassengerId']:
	item = trainset[col][trainset['PassengerId'] == ID].iloc[0]
	second_item = trainset[col2][trainset['PassengerId'] == ID].iloc[0]
	name = str(item) + '_' + str(second_item)

	quant_dict[name] = quant_dict.get(name,0) + 1

print quant_dict


#Converts to a list:
quantit_0 = [quant_dict[item] for item in sorted(quant_dict) if item[-1] == '0'] #so female first
quantit_1 = [quant_dict[item] for item in sorted(quant_dict) if item[-1] == '1'] #so female first


#check that quantities are even
if len(quantit_0) > len(quantit_1):
	for x in range(len(quantit_0) - len(quantit_1)):
		quantit_1.append(0)
elif len(quantit_0) < len(quantit_1):
	for x in range(len(quantit_1) - len(quantit_0)):
		quantit_0.append(0)

print quantit_0
print quantit_1

# create plot
n_groups = len(quantit_1)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8
 
rects1 = plt.bar(index, quantit_1, bar_width,
                 alpha=opacity, 
                 color = 'b',
                 label = 'Survived')

rects2 = plt.bar(index + bar_width, quantit_0, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Died')

 
plt.xlabel(col)
plt.xticks(index + bar_width, xlabels)
plt.ylabel('Frequency')
plt.title('Breakdown of passengers by %s and %s' % (col, col2))
plt.legend(title=col2)
 
plt.tight_layout()
plt.show()