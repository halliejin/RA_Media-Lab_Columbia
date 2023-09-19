from datasets import load_dataset
import pandas as pd

# 加载Amazon US Reviews数据集的特定子集
dataset = load_dataset('amazon_us_reviews', name='Apparel_v1_00')

# 查看可用的分割
print(dataset.keys())
