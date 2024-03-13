# Add the code for the file counter script that you wrote in the course.
#!/usr/bin/python

import pathlib
import pprint
import csv

path = pathlib.Path.cwd()
home = pathlib.Path.home()
working_current = pathlib.Path(f"{home}/tmp/")
working_new = pathlib.Path(f"{working_current}/cleanup_dir")
count_dict = {}
data = []
headers = []

# create new dir, if it already exists dont error out just contiunu with out re-creating.
working_new.mkdir(exist_ok=True)

for filepath in working_current.iterdir():
    if filepath.is_file():
        file_suf = filepath.suffix
        if file_suf not in count_dict:
            count_dict[file_suf] = 1
        elif file_suf in count_dict:
            count_dict[file_suf] += 1
    if filepath.is_dir():
        file_suf = "directory"
        if file_suf not in count_dict:
            count_dict[file_suf] = 1
        elif file_suf in count_dict:
            count_dict[file_suf] += 1
        
with open(f"{working_current}/filecounts.txt", "a") as file_out:
    for key1 in count_dict.keys():
        data.append(count_dict[key1])
    data_str = f"{','.join(map(str, data))}\n"
    file_out.write(str(data_str))
    data = []

headers = list(count_dict.keys())
headers_str = ','.join(headers)

# Read in line 1 of the csv
# see if its the same as headers_str
# if it is then go to the append action..
# if its not either append to the first line of the csv with the headrs_str var
## or read in the existing file, and create a new one adding the headers_str var as the 1st line.
#
#with open(working_current/"filecounts.csv", "r") as csv_file_in: 
## working code to write header but not to the first line unless new file.  
#header_writer = csv.DictWriter(csv_file, fieldnames=headers)
#header_writer.writeheader()

csv_test = pathlib.Path(f"{working_current}/filecounts.csv")

if csv_test.is_file() is True:
    with open(f"{working_current}/filecounts.csv", "r") as csv_in_file:
        first_line = csv_in_file.readline()
        first_line = first_line.strip()
        all_lines = csv_in_file.readlines()
    if first_line == headers_str:
        print("The headers in the file match")
        with open(f"{working_current}/filecounts.csv", "a") as csv_file:
            count_writer = csv.writer(csv_file)
            for key in count_dict.keys():
                data.append(count_dict[key])
            count_writer.writerow(data)
    else:
        # take file read it in (all_lines) new file write new header then append (all_lines)
        print("The headers in the file do not match")
        with open(f"{working_current}/filecounts.csv", "w") as csv_file:
            header_writer = csv.DictWriter(csv_file, fieldnames=headers)
            header_writer.writeheader()
            csv_file.writelines(all_lines)
            count_writer = csv.writer(csv_file)
            for key in count_dict.keys():
                data.append(count_dict[key])
            count_writer.writerow(data)           
        
else:
    with open(f"{working_current}/filecounts.csv", "a") as csv_file:
        header_writer = csv.DictWriter(csv_file, fieldnames=headers)
        header_writer.writeheader()
        count_writer = csv.writer(csv_file)
        for key in count_dict.keys():
            data.append(count_dict[key])
        count_writer.writerow(data)

#####
# Cleanup
#####

#cleanup = input("Do you want to clean up these files in to a cleanup_dir? (Y/N): ")
#cleanup = cleanup.lower()
#
#if cleanup == 'n':
#    print("Ok please run again if you want to clean up this directory...")
#
#while cleanup == "y":
#    for fsuff in count_dict:
#        if count_dict[fsuff] > 5:
#            for fp in working_current.iterdir():
#                if fp.suffix == fsuff:
#                    nfp = working_new.joinpath(fp.name)
#                    fp.replace(nfp)
#    break