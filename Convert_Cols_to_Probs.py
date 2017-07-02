"""TITANIC: LOOKING AT CONDITIONAL PROBABILITIES

What it does: Converts all numerical data relevant to log regression (Sex, Age, Pclass, Fare, Parch, Sibsp) into conditional probabilities.
Converts Age and Fare by creating categorical vars first
Age is based on 10-year spans
Fare is based on sextiles

"""

#Assignment this week: Make a 3D graph and get conditional probabilities for each variable and survival/death

import sys
import numpy as np
import pandas as p

#import as dataframe
trainset = p.read_csv('train.csv')
#female is 1, male is 0
trainset = trainset.replace(to_replace={'Sex':{'female':1,'male':0}})

####  SEX  ####

#Converting Sex into probabilities
sex_probs = trainset.groupby(['Sex']).size().div(len(trainset))
print "Total Sex breakdown:", sex_probs

cond_sex_probs = trainset.groupby(['Sex','Survived']).size().div(len(trainset)).div(sex_probs, axis=0, level='Sex')
print "Conditional Survival by Sex:", cond_sex_probs
#prints sex=0|survival=1
#print cond_sex_probs[0][1]
#prints sex=1|survival=0
#print cond_sex_probs[1][0]

probcol_sex = []
for value in trainset['PassengerId']:
#	print trainset['Sex'][trainset['PassengerId']==value].iloc[0]
	if trainset['Sex'][trainset['PassengerId'] == value].iloc[0] == 0:
		probcol_sex.append(cond_sex_probs[0][1]/cond_sex_probs[0][0])
	elif trainset['Sex'][trainset['PassengerId'] == value].iloc[0] == 1:
		probcol_sex.append(cond_sex_probs[1][1]/cond_sex_probs[1][0])
	else:
		probcol_sex.append(1)

print "LENGTH OF SEX", len(probcol_sex)

####  PCLASS  ####

#Converting Pclass into probabilities

Pclass_probs = trainset.groupby(['Pclass']).size().div(len(trainset))
print "Total Pclass breakdown:", Pclass_probs

cond_Pclass_probs = trainset.groupby(['Pclass','Survived']).size().div(len(trainset)).div(Pclass_probs, axis=0, level='Pclass')
print "Conditional Survival by Pclass:", cond_Pclass_probs

probcol_Pclass = []
for value in trainset['PassengerId']:
#	print trainset['Pclass'][trainset['PassengerId']==value].iloc[0]

	#Pclass = 1
	if trainset['Pclass'][trainset['PassengerId'] == value].iloc[0] == 1:
		probcol_Pclass.append(cond_Pclass_probs[1][1]/cond_Pclass_probs[1][0])
	#Pclass = 2
	elif trainset['Pclass'][trainset['PassengerId'] == value].iloc[0] == 2:
		probcol_Pclass.append(cond_Pclass_probs[2][1]/cond_Pclass_probs[2][0])
	#Pclass = 3
	elif trainset['Pclass'][trainset['PassengerId'] == value].iloc[0] == 3:
		probcol_Pclass.append(cond_Pclass_probs[3][1]/cond_Pclass_probs[3][0])
	else:
		probcol_Pclass.append(1)
		print trainset['Pclass'][trainset['PassengerId']==value].iloc[0]
#	sys.stdin.read(1)

print "LENGTH OF PCLASS", len(probcol_Pclass)

####  AGE  ####

#Converting Age Variable into Categorical
age_cat = []
for value in trainset['PassengerId']:
	if trainset['Age'][trainset['PassengerId'] == value].iloc[0] < 10:
		age_cat.append(1)
	elif trainset['Age'][trainset['PassengerId'] == value].iloc[0] >= 10 and trainset['Age'][trainset['PassengerId'] == value].iloc[0] <20:
		age_cat.append(2)
	elif trainset['Age'][trainset['PassengerId'] == value].iloc[0] >= 20 and trainset['Age'][trainset['PassengerId'] == value].iloc[0] <30:
		age_cat.append(3)
	elif trainset['Age'][trainset['PassengerId'] == value].iloc[0] >= 30 and trainset['Age'][trainset['PassengerId'] == value].iloc[0] <40:
		age_cat.append(4)	
	elif trainset['Age'][trainset['PassengerId'] == value].iloc[0] >= 40 and trainset['Age'][trainset['PassengerId'] == value].iloc[0] <60:
		age_cat.append(4)
	elif trainset['Age'][trainset['PassengerId'] == value].iloc[0] >= 60:
		age_cat.append(5)
	else:
		age_cat.append(99)
#		print 'age is:', trainset['Age'][trainset['PassengerId'] == value].iloc[0]

trainset['age_cat'] = age_cat


#Converting age_cat into probabilities
agecat_probs = trainset.groupby(['age_cat']).size().div(len(trainset))
print "Total age_cat breakdown:", agecat_probs

cond_agecat_probs = trainset.groupby(['age_cat','Survived']).size().div(len(trainset)).div(agecat_probs, axis=0, level='age_cat')
print "Conditional Survival by age_cat:", cond_agecat_probs

#these print the same thing: the first value
#print cond_agecat_probs[0]
#print cond_agecat_probs[1][0]

#Prints cat#2 survival = 0 and cat#2 survival = 1
#print cond_agecat_probs[2][0]
#print cond_agecat_probs[2][1]

probcol_agecat = []
for value in trainset['PassengerId']:
#	print trainset['Pclass'][trainset['PassengerId']==value].iloc[0]

	#Pclass = 1
	if trainset['age_cat'][trainset['PassengerId'] == value].iloc[0] == 1:
		probcol_agecat.append(cond_agecat_probs[1][1]/cond_agecat_probs[1][0])
	#Pclass = 2
	elif trainset['age_cat'][trainset['PassengerId'] == value].iloc[0] == 2:
		probcol_agecat.append(cond_agecat_probs[2][1]/cond_agecat_probs[2][0])
	#Pclass = 3
	elif trainset['age_cat'][trainset['PassengerId'] == value].iloc[0] == 3:
		probcol_agecat.append(cond_agecat_probs[3][1]/cond_agecat_probs[3][0])
	elif trainset['age_cat'][trainset['PassengerId'] == value].iloc[0] == 4:
		probcol_agecat.append(cond_agecat_probs[4][1]/cond_agecat_probs[4][0])
	elif trainset['age_cat'][trainset['PassengerId'] == value].iloc[0] == 5:
		probcol_agecat.append(cond_agecat_probs[5][1]/cond_agecat_probs[5][0])
	else:
		probcol_agecat.append(1)
#		print trainset['age_cat'][trainset['PassengerId']==value].iloc[0]

print "LENGTH OF AGE", len(probcol_agecat)

####  FARE  ####

#Create a categorical fare variable based on an ungrouped fare with quartiles
#print trainset['Fare'].describe() # Gives you a 5 number summary
fare_cat = p.qcut(trainset['Fare'],6,labels=False)
trainset['fare_cat'] = fare_cat

#Converting fare_cat into probabilities
farecat_probs = trainset.groupby(['fare_cat']).size().div(len(trainset))
print "Total fare_cat breakdown:", farecat_probs

cond_farecat_probs = trainset.groupby(['fare_cat','Survived']).size().div(len(trainset)).div(farecat_probs, axis=0, level='fare_cat')
print "Conditional Survival by fare_cat:", cond_farecat_probs

probcol_farecat = []
for value in trainset['PassengerId']:
#	print trainset['Pclass'][trainset['PassengerId']==value].iloc[0]

	if trainset['fare_cat'][trainset['PassengerId'] == value].iloc[0] == 0:
		probcol_farecat.append(cond_farecat_probs[0][1]/cond_farecat_probs[0][0])
	elif trainset['fare_cat'][trainset['PassengerId'] == value].iloc[0] == 1:
		probcol_farecat.append(cond_farecat_probs[1][1]/cond_farecat_probs[1][0])
	elif trainset['fare_cat'][trainset['PassengerId'] == value].iloc[0] == 2:
		probcol_farecat.append(cond_farecat_probs[2][1]/cond_farecat_probs[2][0])
	elif trainset['fare_cat'][trainset['PassengerId'] == value].iloc[0] == 3:
		probcol_farecat.append(cond_farecat_probs[3][1]/cond_farecat_probs[3][0])
	elif trainset['fare_cat'][trainset['PassengerId'] == value].iloc[0] == 4:
		probcol_farecat.append(cond_farecat_probs[4][1]/cond_farecat_probs[4][0])
	elif trainset['fare_cat'][trainset['PassengerId'] == value].iloc[0] == 5:
		probcol_farecat.append(cond_farecat_probs[5][1]/cond_farecat_probs[5][0])
	else:
		probcol_farecat.append(1)

print "LENGTH OF FARE",len(probcol_farecat)

### ParCh ###
#print trainset['Parch'].describe()

parch_probs = trainset.groupby(['Parch']).size().div(len(trainset))
print "Total Parch breakdown:", parch_probs

cond_parch_probs = trainset.groupby(['Parch','Survived']).size().div(len(trainset)).div(parch_probs, axis=0, level='Parch')
print "Conditional Survival by Parch:", cond_parch_probs

probcol_parch = []
for value in trainset['PassengerId']:
#	print trainset['Pclass'][trainset['PassengerId']==value].iloc[0]
	if trainset['Parch'][trainset['PassengerId'] == value].iloc[0] == 0:
		probcol_parch.append(cond_parch_probs[0][1]/cond_parch_probs[0][0])
	elif trainset['Parch'][trainset['PassengerId'] == value].iloc[0] == 1:
		probcol_parch.append(cond_parch_probs[1][1]/cond_parch_probs[1][0])
	elif trainset['Parch'][trainset['PassengerId'] == value].iloc[0] == 2:
		probcol_parch.append(cond_parch_probs[2][1]/cond_parch_probs[2][0])
	elif trainset['Parch'][trainset['PassengerId'] == value].iloc[0] == 3:
		probcol_parch.append(cond_parch_probs[3][1]/cond_parch_probs[3][0])
	elif trainset['Parch'][trainset['PassengerId'] == value].iloc[0] == 4:
		probcol_parch.append(0)
	elif trainset['Parch'][trainset['PassengerId'] == value].iloc[0] == 5:
		probcol_parch.append(cond_parch_probs[5][1]/cond_parch_probs[5][0])
	elif trainset['Parch'][trainset['PassengerId'] == value].iloc[0] == 6:
		probcol_parch.append(0)
	else:
		probcol_parch.append(1)

print "LENGTH OF PARCH",len(probcol_parch)

### SibSp ###
sibsp_probs = trainset.groupby(['SibSp']).size().div(len(trainset))
print "Total SibSp breakdown:", sibsp_probs

cond_sibsp_probs = trainset.groupby(['SibSp','Survived']).size().div(len(trainset)).div(parch_probs, axis=0, level='SibSp')
print "Conditional Survival by SibSp:", cond_sibsp_probs

probcol_sibsp = []
for value in trainset['PassengerId']:
#	print trainset['Pclass'][trainset['PassengerId']==value].iloc[0]
	if trainset['SibSp'][trainset['PassengerId'] == value].iloc[0] == 0:
		probcol_sibsp.append(cond_sibsp_probs[0][1]/cond_sibsp_probs[0][0])
	elif trainset['SibSp'][trainset['PassengerId'] == value].iloc[0] == 1:
		probcol_sibsp.append(cond_sibsp_probs[1][1]/cond_sibsp_probs[1][0])
	elif trainset['SibSp'][trainset['PassengerId'] == value].iloc[0] == 2:
		probcol_sibsp.append(cond_sibsp_probs[2][1]/cond_sibsp_probs[2][0])
	elif trainset['SibSp'][trainset['PassengerId'] == value].iloc[0] == 3:
		probcol_sibsp.append(cond_sibsp_probs[3][1]/cond_sibsp_probs[3][0])
	elif trainset['SibSp'][trainset['PassengerId'] == value].iloc[0] == 4:
		probcol_sibsp.append(cond_sibsp_probs[4][1]/cond_sibsp_probs[4][0])
	elif trainset['SibSp'][trainset['PassengerId'] == value].iloc[0] == 5:
		probcol_sibsp.append(0)
	elif trainset['SibSp'][trainset['PassengerId'] == value].iloc[0] == 8:
		probcol_sibsp.append(0)
	else:
		probcol_sibsp.append(1)

print "LENGTH OF SIBSP",len(probcol_sibsp)


#Print out:
path = 'prob_train.csv'
fhnd = open(path,'w')

stor_dict = {'PassengerId':trainset['PassengerId'],'Survived':trainset['Survived'],'Sex':probcol_sex,'Age':probcol_agecat,'PClass':probcol_Pclass,'Parch':probcol_parch,'SipSp':probcol_sibsp,'Fare':probcol_farecat}
for key in stor_dict:
	print len(stor_dict[key])
prob_based_trainset = p.DataFrame(stor_dict)
print prob_based_trainset

prob_based_trainset.to_csv(path_or_buf=path,columns=['PassengerId','Survived','Sex','Age','PClass','Parch','SibSp','Fare'])