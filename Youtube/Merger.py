import pandas as pd
import os

os.chdir('d:\\0 Hallie Jin\\0 Hallie\\0 QMSS\\0 RA\\Media Lab\\RA_Media-Lab_Columbia\\Youtube')

# 替换以下文件名为你的CSV文件名
files = ['youtubers_data_2020.csv', 'youtubers_data_2021.csv', 'youtubers_data_2022.csv', 'youtubers_data_2023.csv']

# 读取所有文件到一个DataFrame列表中
dfs = [pd.read_csv(f) for f in files]

# 使用concat函数合并所有的DataFrames
merged_df = pd.concat(dfs, ignore_index=True)

# 去除重复行
merged_df.drop_duplicates(inplace=True)

# 将合并后的数据保存到一个新的CSV文件
merged_df.to_csv('merged_output.csv', index=False)