import sys
import os

import pandas as pd
from sktime.forecasting.model_selection import temporal_train_test_split

import yaml

if len(sys.argv) != 2:
    sys.stderr.write("Ошибка в аргументах. Пример выполнения:\n")
    sys.stderr.write("python get_features.py data_file\n")
    sys.exit(1)

params = yaml.safe_load(open("params.yaml"))["split"]

f_input = sys.argv[1]
f_output_train = os.path.join("datasets", "stage3", "train.csv")
os.makedirs(os.path.join("datasets","stage3"), exist_ok=True)
f_output_test = os.path.join("datasets", "stage3", "test.csv")
#os.makedirs(os.path.join("datasets","stage3"), exist_ok=True)

TEST_SIZE = int(params*y.size)

y = pd.read_csv(f_input, index_col='timestamp', parse_dates=True)

y_train, y_test = temporal_train_test_split(y, test_size=TEST_SIZE)

y_train.to_csv(f_output_train)
y_test.to_csv(f_output_test)

