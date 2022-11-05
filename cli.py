import pandas as pd
import json, hashlib, os, sys

try:
    csv_file = sys.argv[1]
    csv_filename = csv_file.split(".")
    csv_filename = csv_file[0]
    file_format = csv_file[1]
    if file_format != "csv":
        print("Invalid file format")
        print("In this format: python cli.py <filename.csv>")
        sys.exit(1)
except IndexError:
    print("Please pass the csv filename as the first argument.")
    print("In this format: python cli.py <filename.csv>")
    sys.exit(1)

path =  os.getcwd()

json_folder = "jsons"

folder_path = os.path.join(path, "jsons")

if not os.path.exists(folder_path):
    os.mkdir(folder_path)

with open(f"{csv_filename}.csv",  newline='') as csvfile:
    my_dataframe = pd.read_csv(csvfile)
    my_dataframe = my_dataframe.fillna(method='ffill')
    columns = my_dataframe.columns.values
    sha256_hash = []
    for index, row in my_dataframe.iterrows():
        my_dict = {}
        filename = row[columns[2]]
        for col in columns:
            my_json[col] = row[col] 
        my_json = json.dumps(my_dict)
        sha256_hash.append(hashlib.sha256(my_json.encode(('utf-8'))).hexdigest())

        with open(f"{json_folder}/{filename}.json", "w") as outfile:
            outfile.write(my_json)

    my_df = my_dataframe.assign(Sha256Hash=sha256_hash)
    my_df.to_csv(f"{csv_filename}.output.csv")