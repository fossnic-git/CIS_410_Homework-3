import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("hw3_avocado.csv")


def show_info(data):
    print("#2. File Information\n")
    data.info()  
    

print("#3. Unique Values\n")
print(data.nunique())  

print("#4. All Rows\n")
pd.set_option('display.max_rows', None)  
print(data)  
pd.reset_option('display.max_rows')  

print("#5. First 5 and Last 5 Rows\n")
print("First 5 rows:")
print(data.head())
print("\nLast 5 rows:")
print(data.tail())

print("#6. First/Last Rows of Specific Columns\n")
print(data.iloc[:, :4].head())  
print(data.iloc[:, -4:].tail())  


print("#6. First 5 Rows of Three Columns\n")
selected_columns = data[['Total Volume', 'AveragePrice', 'Total Bags']]
print(selected_columns.head())


print("#7. One Column using Dot Notation")
print(data['Total Volume'].head())  

print("#8. Multiply Total Volume and AveragePrice\n")
data['EstimatedRevenue'] = data['Total Volume'] * data['AveragePrice']
print(data[['Total Volume', 'AveragePrice', 'EstimatedRevenue']].head())


print("#9. Group By Region and Type (AveragePrice)\n")

grouped_data = data.groupby(['region', 'type'])['AveragePrice'].mean().reset_index()
print(grouped_data.head())

print("#10. Plot Mean, Median, and Std of Total Volume by Year\n")
grouped_year = data.groupby('year')['Total Volume'].agg(['mean', 'median', 'std']).reset_index()
grouped_year.plot(x='year', y=['mean', 'median', 'std'], kind='bar')
plt.title('Total Volume Statistics by Year')
plt.ylabel('Total Volume')
plt.show()

print("#11. Group By Type and Sum of Bags\n")
bags_data = data.groupby('type')[['Small Bags', 'Large Bags', 'XLarge Bags']].sum().reset_index()
print(bags_data)

print("#12. Plot Bags by Type\n")
bags_data.plot(x='type', y=['Small Bags', 'Large Bags', 'XLarge Bags'], kind='bar')
plt.title('Number of Small, Large, and XLarge Bags by Type')
plt.ylabel('Bags Count')
plt.show()

print("#13. Scatter Plot of Total Volume vs AveragePrice\n")
data.plot(kind='scatter', x='Total Volume', y='AveragePrice')
plt.title('Total Volume vs AveragePrice')
plt.show()