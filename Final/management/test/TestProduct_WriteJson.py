import pandas as pd

df = pd.read_excel(r"D:\Final (4)\management\dataset\Product.xlsx", engine="openpyxl")

json_data = df.to_json(orient="records", indent=4, force_ascii=False)

print(json_data)

with open("../dataset/Product.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)
