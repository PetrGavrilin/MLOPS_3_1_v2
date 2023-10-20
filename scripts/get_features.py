import sys
import os

import pandas as pd

if len(sys.argv) != 2:
    sys.stderr.write("Ошибка в аргументах. Пример выполнения:\n")
    sys.stderr.write("python get_features.py data_file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path("datasets", "stage1". train.csv")
os.makedirs(os.path.join("datasets","stage1"), exist_ok=True)

def process_data(df_in, df_out):
    fd_in.readline()
    for line in df_in:
        line = line.rstrip('\n').split(',')
        timestamp = line[1]
        value = line[2]
        fd_out.write("{},{}\n".format(timestamp,value))

with io.open(f_input, fd_out) as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)
    
