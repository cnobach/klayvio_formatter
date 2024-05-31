import pandas as pd
import shutil
import os
import re

INPUT_DIRECTORY = './input_files/'
OUTPUT_DIRECTORY = './output_files/'

def clean_phone_number(phone):
    # Remove any non-digit characters
    cleaned_phone = re.sub(r'\D', '', phone)
    # Add +1 at the beginning
    cleaned_phone = '+1' + cleaned_phone
    return cleaned_phone

def process_csv():
    
    # List of Files
    dataframes = []
    
    # List of File Names
    file_names = []
    
    for filename in os.listdir(INPUT_DIRECTORY):
        if filename.endswith('.csv'): # checks for existing csv file
            file_path = os.path.join(INPUT_DIRECTORY, filename)
            df = pd.read_csv(file_path)
            file_names.append(filename.split('.')[0])
            dataframes.append(df)
    
    shutil.rmtree(OUTPUT_DIRECTORY);
    os.mkdir(OUTPUT_DIRECTORY);
    
    for i, df in enumerate(dataframes):
        
        # Check if 'Phone' column exists
        if 'Phone' not in df.columns:
            raise ValueError("The input CSV does not have a 'Phone' column.")
        
        # Clean the phone numbers
        df['Phone'] = df['Phone'].apply(clean_phone_number)
        
        # Save the cleaned data to a new CSV file
        output_file = os.path.join(OUTPUT_DIRECTORY, f"{file_names[i]}_processed.csv")
        df.to_csv(output_file, index=False)
        print(f"Processed file saved as {output_file}")

    shutil.rmtree(INPUT_DIRECTORY);
    os.mkdir(INPUT_DIRECTORY);

if __name__ == "__main__":
    process_csv()