import pandas as pd

# Load the CSV files into dataframes
file1 = "file1.csv"
file2 = "file2.csv"

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Compare the two dataframes
if df1.equals(df2):
    print("The two CSV files are identical.")
else:
    print("The two CSV files are different.")

    # Identify rows that are different
    diff_rows = pd.concat([df1, df2]).drop_duplicates(keep=False)
    print("\nDifferences:")
    print(diff_rows)

    # Save the differences to a new CSV file (optional)
    diff_rows.to_csv("differences.csv", index=False)
    print("\nDifferences have been saved to 'differences.csv'.")