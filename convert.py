import pandas as pd
import sys

def parquet_to_csv(parquet_file, csv_file):
    try:
        # Read the Parquet file into a DataFrame
        df = pd.read_parquet(parquet_file)
        
        # Save the DataFrame as a CSV file
        df.to_csv(csv_file, index=False)
        print(f"Successfully converted {parquet_file} to {csv_file}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python parquet_to_csv.py <input_parquet_file> <output_csv_file>")
    else:
        parquet_file = sys.argv[1]
        csv_file = sys.argv[2]
        parquet_to_csv(parquet_file, csv_file)

