import pandas as pd


excel_file_path = "Sample Data.xlsx"
df = pd.read_excel(excel_file_path)
rows_with_unknown = df[df["Nature of injury"].str.lower() == "unknown"]

rows_with_unknown.to_excel("rows_with_unknown.xlsx", index=False)
