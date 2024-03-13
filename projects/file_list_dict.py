#!/usr/bin/python

import pathlib
import ast

path = pathlib.Path.cwd()
home = pathlib.Path.home()
working_current = pathlib.Path(f"{home}/tmp/")
line_lst = []

with open(working_current/"filecounts.txt", "r") as file_in:
    lines = file_in.readlines()
    for line in lines:
        line = ast.literal_eval(line)
        line_lst.append(line)
print(line_lst)
