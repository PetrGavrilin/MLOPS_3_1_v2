import sys
import os

import pandas as pd

from sktime.performance_metrics.forecasting import MeanAbsolutePercentageError


import pickle
import json

if len(sys.argv) != 2:
    sys.stderr.write("Ошибка в аргументах. Пример выполнения:\n")
    sys.stderr.write("python get_features.py data_file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("models", sys.argv[2])

df = pd.read_csv(sys.argv[1], , index_col='timestamp', parse_dates=True)
y_test = df.value

mape = MeanAbsolutePercentageError(symmetric=False)

with open(sys.argv[2], "rb") as fd:
    model = pickle.load(fd)

y_pred = model.predict(y_test)

score = mape(y_test, y_pred)

prc_file = "evaluate.json"

with open(prc_file, "w") as fd:
    json.dump({"score": score}, fd)