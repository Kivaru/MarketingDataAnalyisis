import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import pandas as pd

# Step 1
# read the data set of "marketing-data"
# When importing your data, skip the first two rows to overcome the skewed rows.
# This will ensure that your column names are populated correctly.
# data = pd.read_csv("marketing-data.csv", skiprows=2)
data = pd.read_csv("marketing-data.csv")

# print the data
# print(data.head())

# step 2
# checking missing values
# print(data.isnull().sum())

# step 3
# if there are missing values drop the unnecessary columns e.g. age
# data = data[~data.age.isnull()].copy()

# or if you have to fill some missing data,
# you can use some techniques like feeling the most occurring months e.g.
# step 3a:get mode month
# month_mode = data.month.mode()[0]
# fill the missing values with the mode value of month in data
# data.month.fillna(month_mode, inplace= True)

# step 4: Univariate Analysis
# Univariate outliers: Univariate outliers are the data points whose values lie outside
# the expected range. Here, only a single variable is being considered.

# Let's calculate the percentage of each job status category
# Normalize the data to ensure that they lie in the same range and are comparable.
# data.job.value_counts(normalize=True)
# plot the bar graph of percentage for each job category
# data.job.value_counts(normalize=True).plot.barh()
# plt.show()
# plot the pie chart for education category comparison
# data.education.value_counts(normalize=True).plot.pie(autopct='%.2f')
# plt.show()

# Step 5 : Bivariate Analysis
# Step 5a : Numeric-Numerical Analysis
# by scatter plotting age and balance variables in the data
# plt.scatter(data.age, data.balance)
# plt.show()

# by plotting pair plot of age, balance and duration:
# Pair plots are used to compare multiple variables simultaneously.
# They plot a scatter plot of all input variables against each other,
# which helps save space and allows us to compare various variables simultaneously.
# sb.pairplot(data=data, vars=['age', 'balance', 'duration'])
# plt.show()



