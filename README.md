# Titanic

## FILES:
* **Bar_Charts.py :** Creates bar charts for two columns where col2 is 2 categories (e.g. Any_category vs Survival)
* **Bar_Charts_col2_3cats.py :** Creates bar charts for two columns where col2 is 3 categories (e.g. Any_category vs PClass)
* **Check_Dist.py :** Creates a histogram for continuous variables and calculates Kolmogorov-Smirnov p-value for normality
* **Check_Dist_Advanced.py :** Creates a histogram, and calculates KS-test for every distribution. Can give you a "best match" if data fits no known distribution
* **Convert_Cols_to_Probs.py :** for probability-based analysis. Converts all vars into probability-based values
* **Run_Logistic.py :** use to run logistic analysis and test logistic reg against test set
* **sample_dist.txt :** use with Check_Dist.py

### Bar_Charts.py
#### _What should it be used with_:
* Any dataframe that has discrete categorical variable columns (ideally Titanic data)
#### _What it does:_
1. Displays a labeled bar chart of column 1 separated by categories of column 2
e.g. Column 1: PClass, Column 2: Survived -- gives Chart of Frequency of passengers by class, with bars for those who survived and those who died
#### _How to use this file_:
* Change lines 27 and 29 to change the columns you want to use
**Remember that col2 on line 29 has to be a binary variable like 'Survived'. There can only be 2 categories**
* Change the labels of column 1 in live 31 (**xlabels**). Each label should be a category within the variable listed as strings separated by commas
* Change dataset file on line 19 in quotes if dataset is not named 'train.csv'
* Change the category labels of column 2 on lines 77 and 79

### Bar_Charts_col2_3cats.py
### Check_Dist.py
#### _What should it be used with_:
* Any dataframe that has continuous variable columns (ideally Titanic data)
#### _What it does:_
1. Displays a histogram of a continuous variable
2. Displays a normal distribution based on your variable for comparison with the histogram
3. Upon exit of the histogram, leaves a p-value from the Kolmogorov-Smirnov Test for Normality in the Terminal Window. The display also includes the results from two other KS tests: one from a randomized normal distribution, and another from a real-life normal distribution of housefly wing lengths for comparison.
#### _How to use this file_:
* Change dataset file on line 18 in quotes if dataset is not named 'train.csv'
* Change column name on line 33 to indicate the continuous variable column you want to use
* Make sure to download sample_dist.txt too (housefly wing data)

### Check_Dist_Advanced.py
#### _What should it be used with_:
* _See Check_Dist.py_
#### _What it does:_
1. _See Check_Dist.py_
2. Also displays KS results for gumbel left and right skewed distributions and uniform distribution
3. If data does not match those distributions, gives user the choice to check all possible distributions
4. If none of the known distributions match with the KS test, offers user the chance to see "best-matched" distribution based on p-values of KS test
5. Allows user to see which tests could not be run without more information

### _How to use this file_:
* _See Check_Dist.py_
* Answer 'y' or 'n' in the terminal when prompted
