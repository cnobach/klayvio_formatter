import pandas as pd
import shutil
import os
import re
import ui # Importing the UI file

OUTPUT_DIRECTORY = './output_files/'

def clean_phone_number(phone):
    # Remove any non-digit characters
    cleaned_phone = re.sub(r'\D', '', phone)
    # Add +1 at the beginning
    cleaned_phone = '+1' + cleaned_phone
    return cleaned_phone

def process_csv(files):
    
    # List of Files
    dataframes = []
    
    # List of File Names
    file_names = []
    try: 
        for filename in files:
            if filename.endswith('.csv'):
                df = pd.read_csv(filename)
                names = filename.split('/')
                file_names.append(names[len(names)-1].split('.')[0])
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
    except: 
        error = "An error occurred - contact CoCo for support";
        print(error)
        return False
    else:
        return True
        

if __name__ == "__main__":
    ui.createUI() # Call the createUI function from the ui.py file