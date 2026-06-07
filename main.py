import pandas as pd

# GroupBy Example
data = {
    'Department': ['IT', 'IT', 'HR', 'HR'],
    'Salary': [50000, 60000, 45000, 55000]
}

df = pd.DataFrame(data)

print("GroupBy Example:")
print(df.groupby('Department')['Salary'].sum())

# Merge Example
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Ram', 'Ravi', 'Sita']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Salary': [25000, 30000, 28000]
})

print("\nMerge Example:")
print(pd.merge(df1, df2, on='ID'))

# Pivot Example
df3 = pd.DataFrame({
    'Name': ['John', 'Boby', 'Mina'],
    'Course': ['Masters', 'Graduate', 'Graduate'],
    'Age': [27, 23, 21]
})

print("\nPivot Example:")
print(df3.pivot(index='Name', columns='Course', values='Age'))