# Klayvio Formatter for Zoni Work

## Requirements

* Python 3.12.3 version used : Any *should* work
* **To install** - [Python](https://www.python.org/downloads/release/python-3123/)
* **Dependency Management** through pip - should be included in python install
* Run the following commands:
  * `python venv -m venv`
  * `source venv/Scripts/activate`
  * `pip install -r requirements.txt`

## Running the Application

* Create folders called 'input_files' & 'output_files' in the project directory
* Save your files in need of processing into the 'input_files' folder
  * If you have already done this - delete the existing files in both the 'input_files' and 'output_files' folders
* In the terminal, run the following command:
  * `python main.py`
* The new files will now be saved in the 'output_files' directory

## Deactivating Venv

* Run the following command:
  * `deactivate`