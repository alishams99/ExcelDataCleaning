import pandas as pd

filtered_data = pd.read_excel('filtered_data.xlsx')
predicted_results = pd.read_excel('predicted_results.xlsx')

merged_data = pd.concat([filtered_data, predicted_results], ignore_index=True)

# Sort the merged dataframe by the "Date" column
merged_data.sort_values(by='Date', inplace=True)

# Save the merged and sorted dataframe to a new Excel file
merged_data.to_excel('final_data.xlsx', index=False)
