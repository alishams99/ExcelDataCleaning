import pandas as pd


df1 = pd.read_excel('filtered_data.xlsx')

df2 = pd.read_excel('predicted_results.xlsx')
columns_to_append = df1.columns.tolist()

# Append data from the second dataframe to the first one based on common columns
merged_df = pd.concat([df1, df2[columns_to_append]], ignore_index=True)

# Sort the merged dataframe by the "Year" column
sorted_df = merged_df.sort_values(by='Year')

sorted_df.to_excel('merged_and_sorted.xlsx', index=False)

