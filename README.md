# day-11 assignment 
day-11 pandas - groupby - merge - pivot assignment 

Submitted By

Name: Kolakaluri Sravanthi

Introduction

Pandas is a Python library used for data analysis and manipulation. It provides many useful functions to organize, analyze and transform data. In this assignment, I learned about GroupBy, Merge and Pivot functions in Pandas.

GroupBy()

The groupby() function is used to divide data into groups based on one or more columns. After grouping, we can perform calculations such as sum, mean, count, minimum and maximum values.

Steps of GroupBy

1. Split the data into groups.
2. Apply a function to each group.
3. Combine the results.

Example

import pandas as pd

data = {
    'Department': ['IT', 'IT', 'HR', 'HR'],
    'Salary': [50000, 60000, 45000, 55000]
}

df = pd.DataFrame(data)

result = df.groupby('Department')['Salary'].sum()
print(result)

Advantages of GroupBy

- Helps summarize large datasets.
- Makes data analysis easier.
- Useful for calculating statistics on groups.

---

Merge()

The merge() function is used to combine two DataFrames based on a common column.

Types of Merge

1. Inner Merge

Returns only matching records from both DataFrames.

merged_df = pd.merge(df1, df2, on='ID', how='inner')

2. Left Merge

Returns all records from the left DataFrame and matching records from the right DataFrame.

merged_df = pd.merge(df1, df2, on='ID', how='left')

3. Right Merge

Returns all records from the right DataFrame and matching records from the left DataFrame.

merged_df = pd.merge(df1, df2, on='ID', how='right')

4. Outer Merge

Returns all records from both DataFrames.

merged_df = pd.merge(df1, df2, on='ID', how='outer')

Benefits of Merge

- Combines information from multiple datasets.
- Helps create complete reports.
- Useful in real-world data analysis projects.

---

Pivot()

The pivot() function is used to reshape data and create a summary table.

Syntax

df.pivot(index, columns, values)

Parameters

- index: Rows of the new table.
- columns: Columns of the new table.
- values: Values to fill the table.

Example

import pandas as pd

df = pd.DataFrame({
    'Name': ['John', 'Boby', 'Mina'],
    'Education': ['Masters', 'Graduate', 'Graduate'],
    'Age': [27, 23, 21]
})

pivot_table = df.pivot(
    index='Name',
    columns='Education',
    values='Age'
)

print(pivot_table)

Advantages of Pivot

- Organizes data in a readable format.
- Helps compare values easily.
- Useful for reporting and visualization.

---

Conclusion

In this assignment, I learned how to use GroupBy, Merge and Pivot functions in Pandas. These functions are very useful for data cleaning, analysis and reporting. They help in organizing large datasets and extracting meaningful insights from data.
