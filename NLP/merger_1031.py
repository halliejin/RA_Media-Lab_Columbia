import sqlite3
import pandas as pd
import re

# 数据库路径列表
db_paths = [
    "D:/0 Hallie Jin/0 Hallie/0 QMSS/0 RA/Political Bias/2022/nela-gt-2022.db/nela-gt-2022.db",
    "D:/0 Hallie Jin/0 Hallie/0 QMSS/0 RA/Political Bias/2021/dataverse_files/databases/nela-gt-2021.db",
    "D:/0 Hallie Jin/0 Hallie/0 QMSS/0 RA/Political Bias/2020/nela-gt-2020.db",
    "D:/0 Hallie Jin/0 Hallie/0 QMSS/0 RA/Political Bias/2019/nela-gt-2019.db"
]

# 输出的 Excel 文件路径
excel_path = r"D:/0 Hallie Jin/0 Hallie/0 QMSS/0 RA/Political Bias/db/newsmax_19_22.xlsx"

# 创建 Excel 写入器
with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    for db_path in db_paths:
        # 提取年份作为子工作表的名字
        # year = db_path.split('/')[-2].split('-')[-1]
        year_match = re.search(r'(\d{4})', db_path)
        if year_match:
            year = year_match.group(1)
        else:
            print(f"Could not extract year from path: {db_path}")
            continue
        
        # 连接到数据库
        conn = sqlite3.connect(db_path)
        
        # 执行查询
        query = "SELECT * FROM newsdata WHERE source = 'newsmax'"
        df = pd.read_sql(query, conn)
        
        # 将 DataFrame 保存到指定的子工作表中
        df.to_excel(writer, sheet_name=year, index=False)
        
        # 关闭数据库连接
        conn.close()

print(f"数据已保存到 {excel_path}")