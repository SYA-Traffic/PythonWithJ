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
destination_totals = filtered_df.groupby('destination_zone_name')['annual_total_trips'].sum().reset_index()

# 计算每个目的地的卡车数量百分比
total_trips = destination_totals['annual_total_trips'].sum()
destination_totals['percentage'] = destination_totals['annual_total_trips'] / total_trips * 100

# 计算各种统计量
mean_percentage = destination_totals['percentage'].mean()
variance_percentage = destination_totals['percentage'].var()
std_dev_percentage = destination_totals['percentage'].std()
min_percentage = destination_totals['percentage'].min()
max_percentage = destination_totals['percentage'].max()
median_percentage = destination_totals['percentage'].median()
quantiles_percentage = destination_totals['percentage'].quantile([0.25, 0.75])

# 打印百分比统计结果
print(f"Mean Percentage: {mean_percentage:.2f}%")
print(f"Variance Percentage: {variance_percentage:.2f}")
print(f"Standard Deviation Percentage: {std_dev_percentage:.2f}")
print(f"Minimum Percentage: {min_percentage:.2f}%")
print(f"Maximum Percentage: {max_percentage:.2f}%")
print(f"Median Percentage: {median_percentage:.2f}%")
print("Quantiles Percentage:")
print(quantiles_percentage)

# 如果需要，可以将这些统计数据保存到一个新的CSV文件中
stats_df = pd.DataFrame({
    'Metric': ['Mean', 'Variance', 'Standard Deviation', 'Minimum', 'Maximum', 'Median', 'Q1', 'Q3'],
    'Percentage': [mean_percentage, variance_percentage, std_dev_percentage, min_percentage, max_percentage, median_percentage, quantiles_percentage[0.25], quantiles_percentage[0.75]]
})
stats_df.to_csv('D:/statistics_of_percentage_totals.csv', index=False)

print('统计分析结果已记录到D:/statistics_of_percent' + fileName + '.csv')