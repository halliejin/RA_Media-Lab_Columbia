import pandas as pd

# # read distinct media sources from 2017
# absolute_path = 'D:/0 Hallie Jin/0 Hallie/0 QMSS/0 RA/Political Bias/2017/nela-gt-2017.csv'
# df = pd.read_csv(absolute_path)

# distinct_sources = df['source'].drop_duplicates()

# distinct_sources.to_csv('source_2017.csv', index=False)


# 文件路径列表
file_paths = [
    'D:/0 Hallie Jin/0 Hallie/0 QMSS/0 RA/Political Bias/List/source 2017.csv',
    'D:/0 Hallie Jin/0 Hallie/0 QMSS/0 RA/Political Bias/List/source 2018.csv',
    'D:/0 Hallie Jin/0 Hallie/0 QMSS/0 RA/Political Bias/List/source 2019.csv',
    'D:/0 Hallie Jin/0 Hallie/0 QMSS/0 RA/Political Bias/List/source 2020.csv',
    'D:/0 Hallie Jin/0 Hallie/0 QMSS/0 RA/Political Bias/List/source 2021.csv',
    'D:/0 Hallie Jin/0 Hallie/0 QMSS/0 RA/Political Bias/List/source 2022.csv'
]

# 读取每个文件的内容并存储为集合
sets = [set(pd.read_csv(path).iloc[:, 0]) for path in file_paths]

# 使用集合运算找到在每个文件中都出现的元素、在五个文件中出现的元素等
all_files = set.intersection(*sets)
five_files = set.union(*[set.intersection(*[s for j, s in enumerate(sets) if j != i]) for i in range(6)]) - all_files
four_files = set.union(*[set.intersection(*[s for j, s in enumerate(sets) if j not in [i, k]]) for i in range(6) for k in range(i+1, 6)]) - all_files - five_files
three_files = set.union(*[set.intersection(*[s for j, s in enumerate(sets) if j not in [i, k, l]]) for i in range(6) for k in range(i+1, 6) for l in range(k+1, 6)]) - all_files - five_files - four_files
two_files = set.union(*[set.intersection(*[s for j, s in enumerate(sets) if j not in [i, k, l, m]]) for i in range(6) for k in range(i+1, 6) for l in range(k+1, 6) for m in range(l+1, 6)]) - all_files - five_files - four_files - three_files
one_file = set.union(*sets) - all_files - five_files - four_files - three_files - two_files

# 将结果保存到一个CSV文件的不同子表中
with pd.ExcelWriter('distinct list.xlsx') as writer:
    pd.DataFrame(list(all_files), columns=['Element']).to_excel(writer, sheet_name='All Files', index=False)
    pd.DataFrame(list(five_files), columns=['Element']).to_excel(writer, sheet_name='Five Files', index=False)
    pd.DataFrame(list(four_files), columns=['Element']).to_excel(writer, sheet_name='Four Files', index=False)
    pd.DataFrame(list(three_files), columns=['Element']).to_excel(writer, sheet_name='Three Files', index=False)
    pd.DataFrame(list(two_files), columns=['Element']).to_excel(writer, sheet_name='Two Files', index=False)
    pd.DataFrame(list(one_file), columns=['Element']).to_excel(writer, sheet_name='One File', index=False)