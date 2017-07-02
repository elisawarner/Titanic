""" BAR CHART FOR SEX """

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
col = 'Sex'
#sorting by:
col2 = 'Survived'
quant_dict = {}

#Separates each column and their quantities
for ID in trainset['PassengerId']:
	item = trainset['Sex'][trainset['PassengerId'] == ID].iloc[0]
	second_item = trainset['Survived'][trainset['PassengerId'] == ID].iloc[0]

	quant_dict[item] = quant_dict.get(item,0) + 1


#Converts to a list:
quantities = [quant_dict[item] for item in quant_dict]
print quantities

# create plot
n_groups = 2
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8
 
rects1 = plt.bar(index, quantities, bar_width,
                 alpha=opacity, color = 'y')
 
plt.xlabel('Sex')
plt.xticks(index, ('Male','Female'))
plt.ylabel('Frequency')
plt.title('Breakdown of passengers by %s' % col)
plt.legend()
 
plt.tight_layout()
plt.show()