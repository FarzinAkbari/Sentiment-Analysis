import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file.
    """
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Clean the data by removing duplicates and handling missing values.
    """
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def save_data(df, file_path):
    """
    Save the cleaned data to a new CSV file.
    """
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    # File paths
    input_file_path = 'data/tweets.csv'
    output_file_path = 'data/cleaned_tweets.csv'

    # Load data
    df = load_data(input_file_path)
    print(f"Loaded data with {len(df)} records")

    # Clean data
    cleaned_df = clean_data(df)
    print(f"Cleaned data with {len(cleaned_df)} records")

    # Save cleaned data
    save_data(cleaned_df, output_file_path)
    print(f"Cleaned data saved to {output_file_path}")

