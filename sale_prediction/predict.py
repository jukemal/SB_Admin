from django_pandas.io import read_frame
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import datetime
from pathlib import Path
import os

RANDOM_SEED = 42

np.random.seed(RANDOM_SEED)
tf.random.set_seed(RANDOM_SEED)

n_steps_in, n_steps_out = 28, 7

CURRENT_DIR = Path(__file__).resolve(strict=True).parent

PREDICTION_MODEL_NAME = 'SalesPredictionModel'


def predict_sales(meal, orders):
    df = read_frame(orders, fieldnames=[
                    'datetime', 'qty'])

    df = df.sort_values(['datetime'])

    count = df.groupby(by=df["datetime"].dt.date).count()
    count = count[["datetime"]]
    count.rename(columns={"datetime": "Count"}, inplace=True)

    sum = df.groupby(by=df["datetime"].dt.date).sum()
    sum = sum[["qty"]]
    sum.rename(columns={"qty": "Total Quantity"}, inplace=True)

    dataset = count.join(sum)
    dataset["Total Count"] = dataset["Count"]*dataset["Total Quantity"]

    print(dataset.tail(20))

    df = dataset[["Total Count"]]

    df = df.tail(n_steps_in)
    dataset = df.tail(n_steps_in)

    f_columns = ['Total Count']

    scaler = MinMaxScaler(feature_range=(0, 1))

    dataset.loc[:, f_columns] = scaler.fit_transform(
        dataset[f_columns].to_numpy())

    scaled_data = dataset.values

    n_features = 1

    model = keras.models.load_model(
        os.path.join(CURRENT_DIR, PREDICTION_MODEL_NAME))

    x_input = scaled_data.reshape((1, n_steps_in, n_features))
    predicted_values = np.array(model.predict(x_input))

    predicted_values = scaler.inverse_transform(predicted_values[0])

    start_date = df.iloc[-1].name

    dates_array = [(start_date+pd.tseries.offsets.DateOffset(days=i)).date()
                   for i in range(1, predicted_values.shape[0]+1)]

    final_output = pd.DataFrame(predicted_values)
    final_output['datetime'] = dates_array
    final_output.columns = ['Total Count', 'datetime']

    print(df)

    print(final_output)

    real_list = []

    for index, row in df.iterrows():
        real_list.append({
            'date': index,
            'count': row['Total Count'],
        })

    predicted_list = []

    for index, row in final_output.iterrows():
        predicted_list.append({
            'date': row['datetime'],
            'count': round(row['Total Count'], 2),
        })

    data = {
        'meal': meal,
        'real': real_list,
        'predicted': predicted_list,
    }

    return real_list, predicted_list, data
