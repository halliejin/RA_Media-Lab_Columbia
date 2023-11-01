import os
import csv
import json

# 设置目录路径
base_directory = "D:/0 Hallie Jin/0 Hallie/0 QMSS/0 RA/Political Bias/2017"

# 创建或打开CSV文件
with open('source 2017.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    
    # 写入CSV的头部
    writer.writerow(['id', 'date', 'source', 'title', 'content', 'author', 'url', 'published', 'published_utc', 'collection_utc'])

    # 遍历目录结构
    for root, dirs, files in os.walk(base_directory):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as txtfile:
                    data = txtfile.read()
                    content_json = json.loads(data)
                    
                    # 提取所需的字段
                    _id = ""  # 从内容中或其他方式获取ID
                    date = root.split('-')[-1]  # 从目录名获取日期
                    source = content_json.get('source', '')
                    title = content_json.get('title', '')
                    content = content_json.get('content', '')
                    author = content_json.get('author', '')
                    url = content_json.get('link', '')
                    published = content_json.get('published', '')
                    published_utc = ""  # 如果有需要，从内容或其他方式获取
                    collection_utc = ""  # 如果有需要，从内容或其他方式获取
                    
                    # 写入CSV
                    writer.writerow([_id, date, source, title, content, author, url, published, published_utc, collection_utc])

print("CSV文件写入完成!")


