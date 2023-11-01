import os
import pandas as pd
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'D:/0 Hallie Jin/0 Hallie/0 QMSS/0 RA/Political Bias/nela-llm-11a9b19c5844.json'

from google.cloud import storage

client = storage.Client()

# 获取存储桶
bucket = client.get_bucket('nela_llm_data')

# 列出存储桶中的所有文件
blobs = bucket.list_blobs()

for blob in blobs:
    print(blob.name)

url = "gs://nela_llm_data/nela-gt-2017.csv"
df = pd.read_csv(url)
print(df.head())