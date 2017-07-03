""" BAR CHARTS FOR CATEGORICAL DATA (3 categories)

Rules:
	1. col2 must have only three categories (e.g. Sex or Survived)
	2. col can be any categorical variable column name
	3. Change xlabels to change the x labels. Data should be in numerical (0123) or alphabetical order (abcd)
"""

#Create Bar Charts for Categorical Data
#Side-by-side bar charts for survived [1] vs [0]
#Pclass, Sex, SibSp, Parch, Embarked


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

# data to plot
#sorting:
col = 'Embarked'
#sorting by:
col2 = 'Pclass'
quant_dict = {}
xlabels = ('C','Q','S','unknown')

#Separates each column and their quantities
for ID in trainset['PassengerId']:
	item = trainset[col][trainset['PassengerId'] == ID].iloc[0]
	second_item = trainset[col2][trainset['PassengerId'] == ID].iloc[0]
	name = str(item) + '_' + str(second_item)

	quant_dict[name] = quant_dict.get(name,0) + 1

print quant_dict


#Converts to a list:
quantit_0 = [quant_dict[item] for item in sorted(quant_dict) if item[-1] == '1'] #so female first
quantit_1 = [quant_dict[item] for item in sorted(quant_dict) if item[-1] == '2'] #so female first
#temp
quantit_2 = [quant_dict[item] for item in sorted(quant_dict) if item[-1] == '3']

#check that quantities are even
if len(quantit_0) > len(quantit_1):
	for x in range(len(quantit_0) - len(quantit_1)):
		quantit_1.append(0)
elif len(quantit_0) < len(quantit_1):
	for x in range(len(quantit_1) - len(quantit_0)):
		quantit_0.append(0)
#temp
if len(quantit_2) < len(quantit_1):
	for x in range(len(quantit_1) - len(quantit_2)):
		quantit_2.append(0)

print quantit_0
print quantit_1
print quantit_2

# create plot
n_groups = len(quantit_1)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8
 
rects1 = plt.bar(index, quantit_0, bar_width,
                 alpha=opacity, 
                 color = 'b',
                 label = '1')

rects2 = plt.bar(index + bar_width, quantit_1, bar_width,
                 alpha=opacity,
                 color='r',
                 label='2')
#temp
rects3 = plt.bar(index + bar_width*2, quantit_2, bar_width,
                 alpha=opacity,
                 color='g',
                 label='3')
 
plt.xlabel(col)
plt.xticks(index + bar_width, xlabels)
plt.ylabel('Frequency')
plt.title('Breakdown of passengers by %s by %s' % (col, col2))
plt.legend(title=col2)
 
plt.tight_layout()
plt.show()