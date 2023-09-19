from datasets import load_dataset
import pandas as pd

# 加载IMDb数据集
dataset = load_dataset('imdb', split='train')

# 将数据集转换为Pandas DataFrame
dataframe = pd.DataFrame(dataset)

# 导出为CSV
dataframe.to_csv('imdb_dataset_train.csv', index=False)