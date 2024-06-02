import pandas as pd
import shutil
import os
import re
import ui

OUTPUT_DIRECTORY = './output_files/'

def clean_phone_number(phone):
    cleaned_phone = re.sub(r'\D', '', phone)
    cleaned_phone = '+1' + cleaned_phone
    
    return cleaned_phone

def process_csv(files):
    dataframes = []
    file_names = []

    if(len(files) > 0):
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
                if 'Phone' not in df.columns:
                    raise ValueError("The input CSV does not have a 'Phone' column.")
                df['Phone'] = df['Phone'].apply(clean_phone_number)
                output_file = os.path.join(OUTPUT_DIRECTORY, f"{file_names[i]}_processed.csv")
                df.to_csv(output_file, index=False)
                print(f"Processed file saved as {output_file}")
        except: 
            error = "An error occurred - contact CoCo for support";
            print(error)
            return 2 # If an error occurred
        else:
            return 1 # If files were processed successfully
    else:
        return 0 # If no files were selected

if __name__ == "__main__":
    ui.createUI()