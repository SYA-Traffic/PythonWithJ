import pandas as pd


# 需要将两个原始文件复制到D盘，然后改为
# passenger_od_data.csv
# truck_od_data.csv
# 然后只需要改这个fileName变量即可
fileName = 'passenger_od_data'

# 读取Excel文件
file_path = 'D:/'+ fileName + '.csv'  # 替换为你的实际文件路径
df = pd.read_csv(file_path)

# 确保数据中没有起始地址和目的地址相同的数据
filtered_df = df[df['origin_zone_name'] != df['destination_zone_name']]

# 对目的地地址进行分组并求和

# 计算到达每个目的地址的卡车数量总和
destination_totals = filtered_df.groupby('destination_zone_name')['annual_total_trips'].sum().reset_index()

# 计算总卡车数量
total_trips = destination_totals['annual_total_trips'].sum()

# 计算每个目的地数量占总数量的比例，并将其添加为新列
destination_totals['Percentage_of_Total'] = destination_totals['annual_total_trips'] / total_trips

# 重命名列以便更清晰地表示数据
destination_totals.rename(columns={'destination_zone_name': 'Destination_Name',
                                   'annual_total_trips': 'Total_Trips'}, inplace=True)
# 如果你想将结果保存到一个新的Excel文件中，可以取消下面注释的代码行
destination_totals.to_csv('D:/' + fileName+ '_per_destination.csv', index=False)
print('目的地结果已存到D:/' +fileName + '_per_destination.csv')

# 计算各种统计量
# destination_totals = filtered_df.groupby('destination_zone_name')['annual_total_trips'].sum().reset_index()
mean_value = destination_totals['Total_Trips'].mean()
variance_value = destination_totals['Total_Trips'].var()
std_dev_value = destination_totals['Total_Trips'].std()
min_value = destination_totals['Total_Trips'].min()
max_value = destination_totals['Total_Trips'].max()
median_value = destination_totals['Total_Trips'].median()
quantiles = destination_totals['Total_Trips'].quantile([0.25, 0.5, 0.75])

# 打印统计结果
print(f"Mean: {mean_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {std_dev_value}")
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
print(f"Median: {median_value}")
print("Quantiles:")
print(quantiles)

stats_df = pd.DataFrame({
    'Metric': ['Mean', 'Variance', 'Standard Deviation', 'Minimum', 'Maximum', 'Median', 'Q1', 'Median', 'Q3'],
    'Value': [mean_value, variance_value, std_dev_value, min_value, max_value, median_value, quantiles[0.25], median_value, quantiles[0.75]]
})
stats_df.to_csv('D:/statistics_of_'+ fileName + '.csv', index=False)

print('统计分析结果已记录到D:/statistics_of_' + fileName + '.csv')