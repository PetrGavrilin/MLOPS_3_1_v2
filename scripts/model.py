import sys
import os

import pandas as pd
from sktime.forecasting.naive import NaiveForecaster
from sktime.forecasting.base import ForecastingHorizon

import pickle
import json

if len(sys.argv) != 2:
    sys.stderr.write("Ошибка в аргументах. Пример выполнения:\n")
    sys.stderr.write("python get_features.py data_file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("models", sys.argv[2])

data = pd.read_csv(fd_in, index_col='timestamp', parse_dates=True)

y_train = data.value

fh = ForecastingHorizon(y_test.index, is_relative=False)

forecaster = NaiveForecaster(strategy="last")
forecaster.fit(y_train)

# Сохранение модели
with open(f_output, "wb") as file:
    pickle.dump(model, file)
