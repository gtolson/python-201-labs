# Write the file counts to a `.csv` file.
# Add the code for the file counter script that you wrote in the course.
#!/usr/bin/python

import pathlib
import pprint
import csv
import json

path = pathlib.Path.cwd()
home = pathlib.Path.home()
cleanup_path = pathlib.Path(home.joinpath("tmp"))
count_dict = {'directory': 0, '.csv': 0, '.yml': 0, '.png': 0, '.py': 0, '.txt': 0, '.md': 0}
data = []
headers = []
jsonfile = pathlib.Path(home.joinpath("workspace/codingnomads/python-201-labs/03_file-input-output/file-counter/filecounts.json"))
filecounts_txt = pathlib.Path(home.joinpath("workspace/codingnomads/python-201-labs/03_file-input-output/file-counter/filecounts.txt"))
filecounts_csv = pathlib.Path(home.joinpath("workspace/codingnomads/python-201-labs/03_file-input-output/file-counter/filecounts.csv"))

# Dynamic add file types to dict (clear out count_dict before enable)
#for filepath in cleanup_path.iterdir():
#    if filepath.is_file():
#        file_suf = filepath.suffix
#        if file_suf not in count_dict:
#            count_dict[file_suf] = 1
#        elif file_suf in count_dict:
#            count_dict[file_suf] += 1
#    if filepath.is_dir():
#        file_suf = "directory"
#        if file_suf not in count_dict:
#            count_dict[file_suf] = 1
#        elif file_suf in count_dict:
#            count_dict[file_suf] += 1
            
for filepath in cleanup_path.iterdir():
    if filepath.is_file():
        file_suf = filepath.suffix
        if file_suf in count_dict:
            count_dict[file_suf] += 1
    elif filepath.is_dir():
        file_suf = "directory"
        if file_suf in count_dict:
            count_dict[file_suf] += 1

# Write dict to filecounts.txt       
with open(filecounts_txt, "a") as file_out:
    data_str = f"{count_dict}\n"
    file_out.write(data_str)    

# Write dict as json to filecounts.json
with open(jsonfile, "r+") as file_out:
    file_data = json.load(file_out)
    file_data["counts"].append(count_dict)
    file_out.seek(0)
    json.dump(file_data, file_out, indent = 4)


headers = list(count_dict.keys())
headers_str = ','.join(headers)
csv_test = pathlib.Path("filecounts.csv")

if csv_test.is_file() is True:
    with open(filecounts_csv, "r") as csv_in_file:
        first_line = csv_in_file.readline()
        first_line = first_line.strip()
        all_lines = csv_in_file.readlines()
    if first_line == headers_str:
        #print("The headers in the file match")
        with open(filecounts_csv, "a") as csv_file:
            count_writer = csv.writer(csv_file)
            for key in count_dict.keys():
                data.append(count_dict[key])
            count_writer.writerow(data)
    else:
        # take file read it in (all_lines) new file write new header then append (all_lines)
        #print("The headers in the file do not match")
        with open(filecounts_csv, "w") as csv_file:
            header_writer = csv.DictWriter(csv_file, fieldnames=headers)
            header_writer.writeheader()
            csv_file.writelines(all_lines)
            count_writer = csv.writer(csv_file)
            for key in count_dict.keys():
                data.append(count_dict[key])
            count_writer.writerow(data)           
        
else:
    with open(filecounts_csv, "a") as csv_file:
        header_writer = csv.DictWriter(csv_file, fieldnames=headers)
        header_writer.writeheader()
        count_writer = csv.writer(csv_file)
        for key in count_dict.keys():
            data.append(count_dict[key])
        count_writer.writerow(data)
