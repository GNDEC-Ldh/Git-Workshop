import pandas as pd
df = pd.read_csv (r'marks.csv') 

# block 1 - simple stats
mean1 = df['Marks'].mean()
sum1 = df['Marks'].sum()
max1 = df['Marks'].max()
min1 = df['Marks'].min()
count1 = df['Marks'].count()
median1 = df['Marks'].median() 
std1 = df['Marks'].std() 
var1 = df['Marks'].var()  

# block 2 - group by
groupby_sum1 = df.groupby(['Subject']).sum() 
groupby_count1 = df.groupby(['Subject']).count()

# print block 1
print ('Mean marks: ' + str(mean1))
print ('Sum of marks: ' + str(sum1))
print ('Max marks: ' + str(max1))
print ('Min marks: ' + str(min1))
print ('Count of marks: ' + str(count1))
print ('Median marks: ' + str(median1))
print ('Std of marks: ' + str(std1))
print ('Var of marks: ' + str(var1))

# print block 2
print ('Sum of values, grouped by the Subject:\n' + str(groupby_sum1))
print ('Count of values, grouped by the Subject:\n' + str(groupby_count1))
