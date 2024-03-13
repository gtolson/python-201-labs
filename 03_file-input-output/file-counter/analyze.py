# Use the `csv` module to read in and count the different file types.
#!/usr/bin/python
    
# analyze.py
import csv
import pathlib

path = pathlib.Path.cwd()
home = pathlib.Path.home()
cleanup_path = pathlib.Path(home.joinpath("tmp"))
filecounts = pathlib.Path(cleanup_path.joinpath("filecounts.csv"))

with filecounts.open() as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["directory",".csv",".yml",".png",".py",".txt",".md"])
    counts = list(reader)

#print(counts)

firstrun = counts[1]["directory"]
secondrun = counts[2][".png"]
print(f"Folders in run 1: {firstrun}")
print(f"PNG files in run 2: {secondrun}") 