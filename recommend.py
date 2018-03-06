import pandas as pd
import datetime
import sys

# Load Tables from File
input_file = pd.read_csv("PATH_TO_FILE\\user_pref.csv", sep="\t")
product_file = pd.read_csv("PATH_TO_FILE\\prod_score.csv", sep="\t")

user_id = int(sys.argv[1])
input_file = input_file[input_file['uid']==user_id] # Filter only the selected user
input_file = pd.merge(input_file,product_file, on='pid') # Merge with product_file

input_file['age'] = (datetime.datetime(2018,3,6,0,0,0)- pd.to_datetime(input_file['ts'],unit='s')).dt.days # Today is 6th of March 2018
input_file['recommend'] = input_file['product_score'] * (1 + (input_file['score']*(0.95**input_file['age']))) # Calculate recommend value

input_file = input_file.sort_values(by='recommend', ascending=False) # Sort by recommend value
input_file = input_file.reset_index()
input_file = input_file[input_file.columns[1:]]

# Print top-5 result
if input_file['pid'].shape[0]>=5:
    for i in range(0,5):
        print(input_file['pid'][i])
else:
    for i in range(0,input_file['pid'].shape[0]):
        print(input_file['pid'][i])
