# import matplotlib.pyplot as plt
# import seaborn as sb
# import numpy as np
# import pandas as pd

# Step 1
# read the data set of "marketing-data"
# When importing your data, skip the first two rows to overcome the skewed rows.
# This will ensure that your column names are populated correctly.
# data = pd.read_csv("marketing-data.csv", skiprows=2)
# data = pd.read_csv("marketing-data.csv")

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

# by plotting correlation matrix
# A correlation matrix is used to see the correlation between different variables.
# The correlation coefficient determines how two variables are correlated.
# The below table shows the correlation between duration, age, and balance.
# Correlation tells you how one variable affects the other.
# This helps us determine how changes in one variable will also cause
# a change in the other.

# creating a matrix of age, balance and duration as rows and columns
# data[['age', 'balance', 'duration']].corr()
# # plot the correlation matrix of age, balance and duration in data frame
# sb.heatmap(data[['age', 'balance', 'duration']].corr(), annot=True, cmap='Reds')
# plt.show()

# Step 5b : Numeric-Categorical Analysis
# When one variable is of numeric type, and another is a categorical variable,
# you perform numeric-categorical analysis.

# group by marital status to find mean/median balance
# print(data.groupby('marital')['balance'].mean())
# print(data.groupby('marital')['balance'].median())

# You can also plot the box plot of marital vs balance.
# A boxplot will show you the range of values that fall under a certain category
# sb.boxplot(x=data.marital, y=data.balance)
# plt.show()

# Step 5c : Categorical-Categorical Analysis
# When both the variables contain categorical data,
# you perform categorical-categorical analysis.
# creating success rate of numerical data type where is_success "yes" = 1, "no" = 0
# data["is_success"] = np.where(data.is_success == "yes", 1, 0)
# print(data.is_success.value_counts())

# plot the bar graph of marital status and average value of success rate
# data.groupby('marital')['is_success'].mean().plot.bar()
# plt.show()
