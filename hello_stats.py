from pathlib import Path

import pandas as pd

csv_path = Path(__file__).with_name("sample.csv")
df = pd.read_csv(csv_path, encoding="gbk")

print("行数:", len(df))
print("列名:", list(df.columns))
print("分子量平均值:", df["分子量"].mean())
