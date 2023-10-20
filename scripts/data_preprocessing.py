import sys
import os

import numpy as np
import pandas as pd

import sktime

if len(sys.argv) != 2:
    sys.stderr.write("Ошибка в аргументах. Пример выполнения:\n")
    sys.stderr.write("python get_features.py data_file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path("datasets", "stage2", "train.csv")
os.makedirs(os.path.join("datasets","stage2"), exist_ok=True)

def process_data(fd_in, fd_out):
    data = pd.read_csv(fd_in, index_col='timestamp', parse_dates=True)
    df = data.groupby(pd.Grouper(freq='1h')).sum()
    df.to_csv(fd_out)

with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)


